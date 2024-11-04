from .add import my_add


def shout_and_repeat(text):
    """
    Describe here what this function does,
    its input parameters, and what it returns.

    In this example the function converts the input string
    to uppercase and repeats it once.
    """
    t = _shout(text)
    result = my_add(t, t)
    return result


# the underscore signals that this function is not to be used outside this
# module
def _shout(text):
    """
    Describe here what this function does,
    its input parameters, and what it returns.

    In this example the function converts the input string
    to uppercase.
    """
    result = text.upper()
    return result

def ex_function1(argument1):
    return argument1

def ex_function2(argument2):
    return argument2