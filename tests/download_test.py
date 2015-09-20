from __future__ import absolute_import
from __future__ import unicode_literals

from unittest.mock import patch

from testfixtures import ShouldRaise

import finsec
from finsec.download import construct_url
from finsec.download import download_data_from_sec
from finsec.download import get_submissions
from finsec.download import local_data_from_sec
from finsec.download import sec_file_generator


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
        download_data_from_sec('bam')


def test_download_data_from_sec_all_files():
    download_data_from_sec(construct_url(2009, 1))
    assert True


def test_sec_file_generator_raises():
    with ShouldRaise(KeyError("Invalid file name blah.txt, not in ['pre.txt', 'sub.txt', 'readme.htm', 'num.txt', 'tag.txt']")):
        data = sec_file_generator(download_data_from_sec(construct_url(2009, 1)), 'blah.txt')
        for row in data:
            print(row)


def test_sec_file_generator():
    data = sec_file_generator(download_data_from_sec(construct_url(2009, 1)), 'sub.txt')
    for row in data:
        print(row)


def test_get_submissions():
    with patch.object(finsec.download, 'download_data_from_sec', return_value=local_data_from_sec('tests/example/2009q3.zip')):
        data = get_submissions(2009, 3, '10-K')
        form = next(data)
        assert form.cik == '1002638'
        assert form.filed == '20090821'


def test_get_submissions_real():
    data = get_submissions(2011, 2, '10-K')
    for form in data:
        print(form.values)
