# -*- coding: utf-8 -*-


def fibonacci(n):
    """Return nth number in the Fibonaci sequence."""
    num1 = 0
    num2 = 1
    for numbers in range(0, n):
        total = num1
        num1 = num2
        num2 += total
    return num1


def lucas(n):
    """Return nth number in the Lucas sequence."""
    num1 = 2
    num2 = 1
    for numbers in range(0, n):
        total = num1
        num1 = num2
        num2 += total
    return num1
