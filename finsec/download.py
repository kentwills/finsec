from __future__ import absolute_import
from __future__ import unicode_literals

import csv
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

BASE_SEC_URL = 'http://www.sec.gov/data/financial-statements/'
SEC_FILES = ['pre.txt', 'sub.txt', 'readme.htm', 'num.txt', 'tag.txt']


def construct_url(year, quarter):
    """takes a year(int) and quarter(int) 1-4 and constructs a sec url"""

    if not isinstance(year, int):
        raise TypeError('year{} not int.'.format(type(year)))
    if not isinstance(quarter, int):
        raise TypeError('quarter{} not int.'.format(type(quarter)))
    if quarter < 1 or quarter > 4:
        raise ValueError('quarter: {} not in range 1-4.'.format(quarter))
    return BASE_SEC_URL + '{0}q{1}.zip'.format(year, quarter)


def download_data_from_sec_url(url):
    """takes a url and downloads the data into memory"""

    if BASE_SEC_URL not in url:
        raise ValueError('url does not contain a valid url: {}'.format(url))

    url = urlopen(url)
    zipfile = ZipFile(BytesIO(url.read()))

    if set(zipfile.namelist()) != set(SEC_FILES):
        raise ValueError('Downloaded file set {0} does not match expected {1}'.format(zipfile.namelist(), SEC_FILES))
    else:
        return zipfile


def submission_generator(zipfile, name):
    """yields generator for file in SEC dataset"""

    if name not in set(SEC_FILES):
        raise KeyError('Invalid file name {0}, not in {1}'.format(name, SEC_FILES))

    with zipfile.open(name, 'r') as tsv:
        csv_reader = csv.reader(utf_8_decoder(tsv), dialect=csv.excel_tab)
        for row in csv_reader:
            yield row


def utf_8_decoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.decode('utf-8')
