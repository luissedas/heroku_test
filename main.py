"""Added Docstrings"""
import math

def func1(param_a, param_b) -> str:
    """_summary_

    Args:
        param_a (_type_): _description_
        param_b (_type_): _description_

    Returns:
        str: _description_
    """
    return math.floor(param_a + param_b)

def func2(param_a, param_b, param_c) -> int:
    """_summary_

    Args:
        param_a (_type_): _description_
        param_b (_type_): _description_
        param_c (_type_): _description_

    Returns:
        int: _description_
    """
    return math.floor(param_a + param_b + param_c)

def func3(name):
    """_summary_

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f"Hello {name}"
