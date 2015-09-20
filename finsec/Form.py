from __future__ import absolute_import
from __future__ import unicode_literals


class Form(object):

    def __init__(self, dictionary):
        self.data = {}
        self.functions = _load_computed_value_functions()

        for k, v in dictionary.items():
            setattr(self, k, v)

    def values(self, financial_list):
        for value in financial_list:
            self.data[value['tag']] = value

        compute_values(self.data, self.functions)


def compute_values(data, functions):
    failed = []
    completed = []

    last_completed_length = 0
    current_completed_length = 0

    while True:
        for function in functions.values():
            print(function.args)
            # The variable exists we don't need to compute
            if data.get(function.name):
                completed.append(function)
            else:
                # do we have all the input needed to compute?
                if set(function.args) in set(data):
                    args = {}
                    for arg in function.args:
                        args[arg] = data[arg]
                    function(**args)
                    completed.append(function)
                    current_completed_length += 1
                else:
                    failed.append(function)
        if last_completed_length == current_completed_length:
            break
        else:
            last_completed_length == current_completed_length
    return data


def _load_computed_value_functions():
    import types
    import finsec.computed_values as computed_values
    from inflection import camelize
    from collections import namedtuple

    functions = [
        computed_values.__dict__.get(function) for function in dir(computed_values)
        if isinstance(computed_values.__dict__.get(function), types.FunctionType)
    ]

    functions_detail = {}
    Function = namedtuple('Function', ['name', 'args', 'function'])
    for function in functions:
        name = camelize(function.__name__)
        args = tuple(camelize(variable) for variable in function.__code__.co_varnames)
        func_tuple = Function(name=name, args=args, function=function)
        functions_detail[func_tuple.name] = func_tuple

    return functions_detail
