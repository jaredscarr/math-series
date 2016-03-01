# -*- coding: utf-8 -*-
import pytest


FIB_NUMS = [
    (0, 0),
    (1, 1),
    (2, 1),
]

LUCAS = [
    (0, 2),
    (1, 1),
    (2, 3),
]

OPTIONS = [
    (0, 47, 23, 47),
    (0, 1, 10, 1),
    (0, 4, 78, 4),
]


@pytest.mark.parametrize('n, result', FIB_NUMS)
def test_fibonacci(n, result):
    """Test fibonacci method."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS)
def test_lucas_nums(n, result):
    """Test lucas method."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, num1, num2, result', OPTIONS)
def test_sum_series(n, num1, num2, result):
    """Test sum_series method to see which series is selected."""
    from series import sum_series
    assert sum_series(n, num1, num2) == result
