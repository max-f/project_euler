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
    # Arbitrary high limit which should include the 10001st prime
    limit = 200000
    wanted_prime_number = 10001

    for i, x in enumerate(prime_sieve(limit)):
        if i == (wanted_prime_number - 1):
            print('10001st prime number is: %d' % x )
            break

if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
