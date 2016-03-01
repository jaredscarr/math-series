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
