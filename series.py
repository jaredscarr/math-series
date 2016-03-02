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


def sum_series(n, num1=0, num2=1):
    """Return nth number in sequence of two given numbers."""
    num1 = num1
    num2 = num2
    for numbers in range(0, n):
        total = num1
        num1 = num2
        num2 += total
    return num1


if __name__ == "__main__":
    """This module defines functions that implement mathematical series."""
    print("This module defines functions that implement mathematical series.")
    print("The fibonacci method returns the nth number in the sequence")
    print("fibonacci(8) is", fibonacci(8))
    print("The lucus method returns the nth number in the sequence")
    print("lucas(10) is", lucas(10))
    print("The sum_series method returns the nth number of two given numbers.")
    print("sum_series(39, 23, 67) ", sum_series(39, 23, 67))
