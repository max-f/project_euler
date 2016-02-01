#!/usr/bin/env python

import time


def prime_sieve(limit):
    """
    Sieve of Eratosthenes
    """
    multiples = set()
    for x in range(2, limit + 1):
        if x not in multiples:
            yield x
            multiples.update(range(x * x, limit + 1, x))

def main():
    limit = 2000000 - 1
    primes = [x for x in prime_sieve(limit)]
    print('Sum of all prime numbers below two million: %d' % sum(primes))


if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
