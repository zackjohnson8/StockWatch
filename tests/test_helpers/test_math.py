import pytest

import src.stock_watch_app.helpers.math as math


def test_sum_positive_numbers():
    try:
        math.sum_value(1, 2)
        assert True
    except TypeError:
        pytest.fail("Should not raise TypeError")


def test_sum_negative_numbers():
    try:
        math.sum_value(-1, -2)
        assert True
    except TypeError:
        pytest.fail("Should not raise TypeError")


def test_sum_mixed_numbers():
    try:
        math.sum_value(1, -2)
        assert True
    except TypeError:
        pytest.fail("Should not raise TypeError")


def test_sum_strings():
    try:
        math.sum_value("dog", "cat")
        assert False
    except TypeError:
        assert True
