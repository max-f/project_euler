#!/usr/bin/env python

import math


"""
Most optimized :D: just using the highest power of each prime occuring in range
1-20, calculated by hand:
print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)
"""


"""
Less optimized, with some more computing:
"""
def prime_sieve(limit):
    """
    Sieve of Eratosthenes
    """
    multiples = set()
    for i in range(2, limit + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, limit + 1, i))


def main():
    limit = 20

    prime_powers = list()
    for p in prime_sieve(limit):
        # Calculating max. power of the prime in given range
        power = math.floor(math.log(limit, p))
        prime_powers.append(p ** power)
    result = 1
    for x in prime_powers:
        result *= x
    print(result)

main()
