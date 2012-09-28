#/usr/bin/env python
#coding=utf8

from math import factorial, sqrt


def binomial_coefficient(a, b):
    '''Return the binomial coefficient of a and b.'''
    return factorial(a) / (factorial(b) * factorial(a - b))


def fibonacci(limit):
    '''Yield Fibonacci sequence up to limit.'''
    a, b = 0, 1
    while a < limit:
        a, b = b, a + b
        yield a


def nth_fibonacci(n):
    '''Return nth Fibonacci element.'''
    phi = (1 + math.sqrt(5)) / 2
    return math.floor(pow(phi, 2) / math.sqrt(5) + float(1) / 2)


def is_palindrome(item):
    '''Return True if item is palindromic, otherwise return False.'''
    item = str(item)
    return item == item[::-1]
