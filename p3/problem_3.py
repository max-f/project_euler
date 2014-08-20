#!/usr/bin/env python

import math
"""
Using Fermat's factorization method to find prime factorization of an uneven n.
"""


def fermat(n, prime_factors):
    # Method only works for uneven numbers!
    assert n % 2 != 0
    x = math.ceil(math.sqrt(n))
    r = x ** 2 - n
    while math.sqrt(r) != int(math.sqrt(r)):
        r += 2 * x + 1
        x += 1
    y = int(math.sqrt(r))
    a = x + y
    b = x - y
    if b == 1:
        prime_factors.append(a)
        return
    fermat(a, prime_factors)
    fermat(b, prime_factors)


def main():
    n = 600851475143
    prime_factors = list()
    fermat(n, prime_factors)
    print(prime_factors)

main()
