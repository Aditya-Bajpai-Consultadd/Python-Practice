import pytest
from Ass7Q2 import add, subtract, multiply, divide


def test_add():
    assert add(3, 2) == 5
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0
    assert add(10**6, 10**6) == 2 * 10**6
    assert add(0.1, 0.2) == 0.3
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(5, 0) == 5
    assert subtract(5, -5) == 10
    assert subtract(10**6, 10**5) == 900000
    assert subtract(2.5, 1.1) == 1.4
    assert subtract(3.7, 2.3) == 1.4

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(0, 10) == 0
    assert multiply(10, 0) == 0
    assert multiply(-1, 5) == -5
    assert multiply(10**3, 10**3) == 10**6
    assert multiply(0.1, 0.2) == 0.02
    assert multiply(1.5, 2.5) == 3.75


def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 2) == -3
    assert divide(6, -2) == -3
    assert divide(-6, -2) == 3
    assert divide(10, 1) == 10
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
    assert divide(10**6, 10**3) == 1000
    assert divide(10**6, 10**6) == 1

def test_LargeNumbers():
    assert add(10**12, 10**12) == 2 * 10**12
    assert subtract(10**12, 10**11) == 9 * 10**11
    assert multiply(10**6, 10**6) == 10**12
    assert divide(10**12, 10**6) == 10**6