import pytest
from series import fibonacci

def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected
