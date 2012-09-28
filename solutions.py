#/usr/bin/env python
#coding=utf8

from math import factorial
from subprocess import check_output
from sys import argv
from time import time
from tools import *


def problem_1():
    return sum(x for x in xrange(1000) if not x % 3 or not x % 5)


def problem_2():
    return sum(x for x in fibonacci(4000000) if not x % 2)


def problem_3():
    return check_output('factor 600851475143', shell=True).split()[-1]


def problem_4():
    return max(filter(is_palindrome, (x * y for x in xrange(999, 99, -1)
                                            for y in xrange(999, 99, -1))))

def problem_6():
    return abs(sum(pow(x, 2) for x in xrange(101))
               - pow(sum(x for x in xrange(101)), 2))


def problem_7():
    return [p for p in primes(10001)][-1]


def problem_10():
    return sum(primes_under(2000000))


def problem_15():
    return binomial_coefficient(40, 20)


def problem_16():
    return sum(int(x) for x in str(pow(2, 1000)))


def problem_20():
    return sum(int(x) for x in str(factorial(100)))


def problem_29():
    return len(set(pow(a, b) for a in xrange(2, 101) for b in xrange(2, 101)))


def problem_48():
    return str(sum(pow(n, n) for n in xrange(1, 1001)))[-10:]


def main():
    solved = [1, 2, 3, 4, 6, 7, 10, 15, 16, 20, 29, 48]
    if len(argv) > 0:
        args = argv[1:]
    for problem in solved:
        print 'Problem #%s' % problem
        t = time()
        solution = globals()['problem_%s' % problem]()
        timing = float(time() - t)
        if '-s' in args:
            print 'Solution: %s' % solution
        print 'Time: %.6f s\n' % timing


if __name__ == '__main__':
    main()
