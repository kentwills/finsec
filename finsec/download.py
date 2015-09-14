from __future__ import absolute_import
from __future__ import unicode_literals
BASE_SEC_URL = 'http://www.sec.gov/data/financial-statements/'


def construct_url(year, quarter):
    """Takes a year(int) and quarter(int) 1-4 and constructs a sec url"""

    if not isinstance(year, int):
        raise TypeError('year{} not int.'.format(type(year)))
    if not isinstance(quarter, int):
        raise TypeError('quarter{} not int.'.format(type(quarter)))
    if quarter < 1 or quarter > 4:
        raise ValueError('quarter: {} not in range 1-4.'.format(quarter))
    return BASE_SEC_URL + '{0}q{1}.zip'.format(year, quarter)
