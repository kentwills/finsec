from __future__ import absolute_import
from __future__ import unicode_literals

from testfixtures import ShouldRaise

from finsec.download import construct_url
from finsec.download import download_data_from_sec_url
from finsec.download import get_10Ks
from finsec.download import submission_generator


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


def test_download_data_from_sec_url_validates_files():
    with ShouldRaise(ValueError('url does not contain a valid url: bam')):
        download_data_from_sec_url('bam')


def test_download_data_from_sec_url_all_files():
    download_data_from_sec_url(construct_url(2009, 1))
    assert True


def test_submission_generator_raises():
    with ShouldRaise(KeyError("Invalid file name blah.txt, not in ['pre.txt', 'sub.txt', 'readme.htm', 'num.txt', 'tag.txt']")):
        data = submission_generator(download_data_from_sec_url(construct_url(2009, 1)), 'blah.txt')
        for row in data:
            print(row)


def test_submission_generator():
    data = submission_generator(download_data_from_sec_url(construct_url(2009, 1)), 'sub.txt')
    for row in data:
        print(row)


def test_get_10Ks():
    data = get_10Ks(2009, 3)
    for row in data:
        print(row)
