# -*- coding: utf-8 -*-


def fibonacci(n):
    """Return nth number in the fibonaci sequence."""
    num1 = 0
    num2 = 1
    for numbers in range(0, n):
        total = num1
        num1 = num2
        num2 = total + num2
    print(num2)
    return num2
