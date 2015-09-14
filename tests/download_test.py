from __future__ import absolute_import
from __future__ import unicode_literals

from testfixtures import ShouldRaise

from finsec.download import construct_url


def test_construct_url_raises_with_greater_than_range():
    with ShouldRaise(ValueError('quarter: 5 not in range 1-4.')):
        construct_url(2015, 5)


def test_construct_url_raises_with_less_than_range():
    with ShouldRaise(ValueError('quarter: 0 not in range 1-4.')):
        construct_url(2015, 0)


def test_construct_url_raises_with_incorrect_year_type():
    with ShouldRaise(TypeError("year<class 'str'> not int.")):
        construct_url('2015', 3)


def test_construct_url_raises_with_incorrect_quarter_type():
    with ShouldRaise(TypeError("quarter<class 'str'> not int.")):
        construct_url(2015, '3')


def test_construct_url_returns_proper_string():
    expected = 'http://www.sec.gov/data/financial-statements/2015q2.zip'
    assert construct_url(2015, 2) == expected
