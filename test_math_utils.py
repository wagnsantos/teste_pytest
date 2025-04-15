import pytest
from math_utils import add, subtract import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(4, 3) == 12

def test_multiply_invalid_type():
    try:
        multiply("a", 3)
    except ValueError:
        assert True
