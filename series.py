def fibonacci(n):
    """
    This function returns the fibonacci number at the index provided
     """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_iter(n):
    """
    This function returns the fibonacci number at the index provided
    :param n: index
    :return: value at index n
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    idx = 2
    first = 0
    second = 1
    total = 1
    while idx <= n:
        total = first + second
        first = second
        second = total
        idx += 1
    return total

def lucas(n):
    """
    This function returns the lucas number at the index provided
    :param n: index
    :return: value at index n
    """
    if n < 0:
        return -1

    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n, idx_zero = 0, idx_one = 1):
    """
    This function returns the element at position n of a sequence,
    where each element in the sequence is the sum of the previous
    two elements. Optionally takes 2 starting values.
    :param n: index to be returned
    :param idx_zero: value at index 0 (default value 0)
    :param idx_one: value at index 1 (default value 1)
    :return: value at index n
    """

    if n == 0:
        return idx_zero

    if n == 1:
        return idx_one

    return sum_series(n - 1, idx_zero, idx_one) + sum_series(n - 2, idx_zero, idx_one)
