# -*- coding: utf-8 -*-
# flake8: noqa
# pylint: skip-file
"""nose tests for metadata."""

from .._porbase import query
from nose.tools import assert_equals, assert_raises


def test_query():
    """Test the query of metadata (porbase.org) with 'low level' queries."""
    assert_raises(Exception, query, '9781849692341')
    assert_raises(Exception, query, '9781849692343')
    assert_equals(len(repr(query('9789727576807'))) > 100, True)
    assert_equals(len(repr(query('9789720049612'))) > 100, True)
    assert_equals(len(repr(query('9789727228133'))) > 100, True)
    assert_raises(Exception, query, '9780000000')
