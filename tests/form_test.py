from __future__ import absolute_import
from __future__ import unicode_literals

from finsec.Form import _load_computed_value_functions


def test_load_computed_value_function():
    functions = _load_computed_value_functions()
    assert 'DebtToCapitalRatio' in set(functions)
    assert functions['DebtToCapitalRatio'].args == tuple(('TotalDebt', 'TotalCapital'))
