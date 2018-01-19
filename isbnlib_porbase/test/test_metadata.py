# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from nose.tools import assert_equals, assert_raises
from isbnlib import meta
from .._porbase import query


def test_query():
    """Test the query of metadata (porbase.org) with 'low level' queries."""
    assert_raises(Exception, query, '9781849692341')
    assert_raises(Exception, query, '9781849692343')
    assert_equals(len(repr(query('9789727576807'))) > 100, True)
    assert_equals(len(repr(query('9789720049612'))) > 100, True)
    assert_equals(len(repr(query('9789727228133'))) > 100, True)
    assert_raises(Exception, query, '9780000000')


# def test_ext_meta():
#    """Test the query of metadata (porbase.org) with 'high level' meta function."""
#    # test meta from core
#    assert_equals(len(repr(meta('9789727576807', 'porbase'))) > 100, True)
