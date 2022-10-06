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
    """
    if n < 0:
        return -1

    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)

