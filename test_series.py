import pytest
from series import fibonacci
from series import fib_iter
from series import lucas
from series import sum_series

# Fibonacci Tests
def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fib_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


# Fib_iter Tests
def test_fib_iter_zero():
    actual = fib_iter(0)
    expected = 0
    assert actual == expected


def test_fib_iter_one():
    actual = fib_iter(1)
    expected = 1
    assert actual == expected


def test_fib_iter_two():
    actual = fib_iter(2)
    expected = 1
    assert actual == expected


def test_fib_iter_five():
    actual = fib_iter(5)
    expected = 5
    assert actual == expected


def test_fib_iter_seven():
    actual = fib_iter(7)
    expected = 13
    assert actual == expected

# Lucas Tests


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_two():
    assert lucas(2) == 3


def test_lucas_five():
    assert lucas(5) == 11


def test_lucas_seven():
    assert lucas(7) == 29


# Sum_series Tests

def test_default_start_zero():
    assert sum_series(0) == 0


def test_default_start_one():
    assert sum_series(1) == 1


def test_default_start_six():
    assert sum_series(6) == 8


def test_lucas_start_four():
    assert sum_series(4, 2, 1) == 7


def test_negative_start_four():
    assert sum_series(4, -1, -2) == -8


def test_advanced_start_four():
    assert sum_series(4, 10, 11) == 53
