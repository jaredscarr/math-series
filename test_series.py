# -*- coding: utf-8 -*-
import pytest


FIB_NUMS = [
    (0, 1),
    (1, 1),
    (2, 2),
]


@pytest.mark.parametrize('n, result', FIB_NUMS)
def test_fibonacci(n, result):
    """Test fibonacci method."""
    from series import fibonacci
    assert fibonacci(n) == result

