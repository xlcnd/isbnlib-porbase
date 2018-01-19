# -*- coding: utf-8 -*-
"""Query the porbase.org service for metadata."""

import logging
from xml.dom.minidom import parseString

from isbnlib.dev import stdmeta
from isbnlib.dev._bouth23 import u
from isbnlib.dev._exceptions import (NoDataForSelectorError, RecordMappingError)
from isbnlib.dev.webquery import query as wquery

LOGGER = logging.getLogger(__name__)
UA = 'isbnlib (gzip)'
SERVICE_URL = 'http://urn.porbase.org/isbn/dc/xml?id={isbn}'


def _get_text(topnode):
    """Get the text values in the child nodes."""
    text = ""
    for node in topnode.childNodes:
        if node.nodeType == node.TEXT_NODE:
            text = text + node.data
    return text


def parser_porbase(xml):
    """Parse the response from the porbase service."""
    if '<error>' in xml:
        return {}
    dom = parseString(xml)
    keys = ('Title', 'Authors', 'Publisher', 'Year', 'Language')
    fields = ('dc:title', 'dc:creator', 'dc:publisher', 'dc:date',
              'dc:language')
    recs = {}
    for key, field in zip(keys, fields):
        nodes = dom.getElementsByTagName("dc")[0].getElementsByTagName(field)
        txt = '|'.join([_get_text(node) for node in nodes])
        recs[key] = u(txt)
    recs['Publisher'] = recs.get('Publisher', u('')).split('|')[0]
    recs['Authors'] = recs.get('Authors', u([])).split('|')
    recs['Year'] = ''.join([
        c for c in recs.get('Year', u(''))
        if c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    ])
    return recs


def _mapper(isbn, records):
    """Map: canonical <- records."""
    # canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    if not records:  # pragma: no cover
        LOGGER.debug('NoDataForSelectorError for %s', isbn)
        raise NoDataForSelectorError(isbn)
        return {}
    try:
        canonical = {}
        canonical['ISBN-13'] = u(isbn)
        canonical['Title'] = records.get('Title',
                                         u('')).replace(' :', ':').replace(
                                             '<', '').replace('>', '')
        canonical['Authors'] = records.get('Authors', u([]))
        canonical['Publisher'] = records.get('Publisher', u(''))
        canonical['Year'] = records.get('Year', u(''))
        canonical['Language'] = records.get('Language', u(''))
    except:  # pragma: no cover
        LOGGER.debug("RecordMappingError for %s with data %s", isbn, records)
        raise RecordMappingError(isbn)
    # call stdmeta for extra cleanning and validation
    return stdmeta(canonical)


def query(isbn):
    """Query the porbase.org service for metadata."""
    data = wquery(
        SERVICE_URL.format(isbn=isbn), user_agent=UA, parser=parser_porbase)
    if not data:  # pragma: no cover
        LOGGER.debug('No data from porbase.org for isbn %s', isbn)
    return _mapper(isbn, data)
