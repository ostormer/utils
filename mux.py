# In practice, this is just a number-base changer, where the number not in base 10 is represented as an array.
# Created to transform binary output arrays of a multilabel classifier into a single base 10 int.

def mux(array, array_base=2):
    """Multiplex array containing digits of given base into base-10 int

    Args:
        array (numpy.ndarray): 1-d array of digits of base "base".
        base (int, optional): Base of digits in array. Defaults to 2.

    Returns:
        int: multiplexed number 
    """
    s = 0
    for i, digit in enumerate(array):
        exponent = len(array) - 1 - i
        s += digit * array_base ** exponent
    return s


def demux(x, n_classes, array_base=2):
    """Demultiplex a single base-10 int into an array of length n_classes

    Args:
        x (int): base-10 int to demux into array
        n_classes (int): length of output array. Must be greater than
        array_base (int, optional): base of digits in output array. Defaults to 2.

    Returns:
        numpy.ndarray: demuxed array, a base-"base" representation of x represented as an array
    """
    assert x < n_classes ** array_base, "\
        n_classes too small for x, minimum size is {:d}".format(ceil(log(x, 2)))
    # I could have done this using builtin
    array = np.zeros(n_classes)
    s = x  # Sum to hold remainder of x 
    for i in range(n_classes - 1, 0, -1):
        digit = s // (array_base ** i)
        array[i] = digit
        s -= array_base ** digit
    assert s == 0, "Remainder sum after demux is not 0, it is {:d}".format(s)
    return array
