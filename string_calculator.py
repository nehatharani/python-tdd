from string_calculator_exceptions import ValueTooSmallError
from utility_functions import check_constraints


def add(input_str, delim=","):
    result = 0

    if check_constraints(input_str): return result

    chars = input_str.split(delim)
    for c in chars:
        if c.lstrip("-").isdigit():
            number = int(c)
            if number < 0:
                raise ValueTooSmallError(number)
            elif number <= 100:
                result += number  
    return result