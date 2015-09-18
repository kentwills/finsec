from __future__ import absolute_import
from __future__ import unicode_literals

import csv
from io import BytesIO
from io import TextIOWrapper
from urllib.request import urlopen
from zipfile import ZipFile

from finsec.Form import Form

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


def sec_file_generator(zipfile, name):
    """yields generator for file in SEC dataset"""

    if name not in set(SEC_FILES):
        raise KeyError('Invalid file name {0}, not in {1}'.format(name, SEC_FILES))

    with zipfile.open(name, 'r') as tsv:
        csv_reader = csv.DictReader(TextIOWrapper(tsv, encoding='utf-8'), dialect=csv.excel_tab)
        for row in csv_reader:
            yield row


def get_submissions(year, quarter, form):
    """
    Get SEC Submissions, for a full list of options see: http://www.sec.gov/forms
    year -- the year of the filing,  2009-2015 
    quarter -- select forms durin a specific quarter, 1-4
    form -- form type, 10-K, 10-Q etc.
    """
    # get numerical data
    numerical_data = get_numerical_data(year,quarter)

    # get submission data
    data = sec_file_generator(download_data_from_sec_url(construct_url(year, quarter)), 'sub.txt')
    for row in data:
        if row.get('form') == form:
            new_form = Form(row)
            new_form.financials(numerical_data.get(row.get('adsh')))
            yield new_form


def get_numerical_data(year, quarter):
    data_dict = {}
    data = sec_file_generator(download_data_from_sec_url(construct_url(year, quarter)), 'num.txt')
    for row in data:
        adsh = row['adsh']
        if data_dict.get(adsh):
            data_dict[adsh].append(row)
        else:
            data_dict[adsh] = [row]
    return data_dict
