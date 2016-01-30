#!/usr/bin/env python

import math
import time


def divisors(n):
    divisors = 0
    sqrt = math.floor(math.sqrt(n))
    for x in range(1, sqrt):
        if n % x == 0:
            divisors += 2
    if n == sqrt * sqrt:
        divisors -= 1
    return divisors


def main():
    n = 0
    i = 1
    while divisors(n) < 500:
        n += i
        i += 1
    print('First n with over 500 divisors: %d' % n)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
