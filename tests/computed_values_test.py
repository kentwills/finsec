from __future__ import absolute_import
from __future__ import unicode_literals

from finsec.computed_values import days_of_inventory_on_hand
from finsec.computed_values import days_of_sales_outstanding
from finsec.computed_values import inventory_turnover
from finsec.computed_values import receivables_turnover


def test_receivables_turnover():
    result = receivables_turnover(10, 5)
    assert result == 2


def test_days_of_sales_outstanding():
    result = days_of_sales_outstanding(10)
    assert result == 36.5


def test_inventory_turnover():
    result = inventory_turnover(11, 2)
    assert result == 5.5


def test_days_of_inventory_on_hand():
    result = days_of_inventory_on_hand(10)
    assert result == 36.5
