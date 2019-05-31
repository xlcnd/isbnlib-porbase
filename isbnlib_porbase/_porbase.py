# -*- coding: utf-8 -*-
"""Query the urn.porbase.org service for metadata."""

import logging
from xml.dom.minidom import parseString

from isbnlib.dev import stdmeta
from isbnlib.dev._bouth23 import u
from isbnlib.dev.webquery import query as wquery

LOGGER = logging.getLogger(__name__)
UA = 'isbnlib (gzip)'
SERVICE_URL = 'http://urn.porbase.org/isbn/dc/xml?id={isbn}'


def _get_text(topnode):
    """Get the text values in the child nodes."""
    text = ""
    for node in topnode.childNodes:
        if node.nodeType == node.TEXT_NODE:  # pragma: no cover
            text = text + node.data
    return text


def parser_porbase(xml):
    """Parse the response from the porbase service."""
    # handle special case
    if '<error>' in xml:
        return {}
    # parse xml and extract canonical fields
    dom = parseString(xml)
    keys = ('Title', 'Authors', 'Publisher', 'Year', 'Language')
    fields = ('dc:title', 'dc:creator', 'dc:publisher', 'dc:date',
              'dc:language')
    recs = {}
    try:
        for key, field in zip(keys, fields):
            nodes = dom.getElementsByTagName("dc")[0]\
                .getElementsByTagName(field)
            txt = '|'.join([_get_text(node) for node in nodes])
            recs[key] = u(txt)
        # cleanning
        recs['Publisher'] = recs['Publisher'].split('|')[0]
        recs['Authors'] = recs['Authors'].split('|')
        recs['Year'] = u(''.join(c for c in recs['Year'] if c.isdigit())[:4])
        recs['Title'] = recs['Title'].replace(': romance', '')\
            .replace(' :', ':').replace('<', '').replace('>', '')
    except Exception as exc:
        LOGGER.debug(
            'Check the parsing for porbase.org (%r)', exc, exc_info=True)
    return recs


def _mapper(isbn, records):
    """Make records canonical.

    canonical: ISBN-13, Title, Authors, Publisher, Year, Language
    """
    # handle special case
    if not records:  # pragma: no cover
        return {}
    # add ISBN-13
    records['ISBN-13'] = u(isbn)
    # call stdmeta for extra cleanning and validation
    return stdmeta(records)


def query(isbn):
    """Query the urn.porbase.org service for metadata."""
    data = wquery(
        SERVICE_URL.format(isbn=isbn), user_agent=UA, parser=parser_porbase)
    if not data:  # pragma: no cover
        LOGGER.debug('No data from porbase.org for isbn %s', isbn)
        return {}
    return _mapper(isbn, data)
