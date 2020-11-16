import numpy as np


def func_argument_decorator(function):
    def wrapper(arg):
        if isinstance(arg, list):
            list_values = []
            for value in arg:
                list_values.append(function(value))

            return list_values

        if isinstance(arg, np.ndarray):
            for value in arg:
                if not isinstance(value, (np.float, np.int)):
                    raise ValueError(f"O tipo do argumento está incorreto: {arg} {type(arg)}")

        if isinstance(arg, (int, float, np.ndarray)):
            return function(arg)

        raise ValueError(f"O tipo do argumento está incorreto: {arg} {type(arg)}")

    return wrapper
