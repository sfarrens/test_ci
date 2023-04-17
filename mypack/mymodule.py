"""MyModule.

This is my module. Here is more info...

"""


def myfunc(val1, val2):
    """MyFunc.

    This is my function.

    Parameters
    ----------
    val1 : float
        First value
    val2 : float
        Second value

    Returns
    -------
    float
        Division of the two input values

    Raises
    ------
    ValueError
        If ``val2`` is equal to zero
    """
    if val2 == 0:
        raise ValueError("val2 cannot be zero.")

    return val1 / val2
