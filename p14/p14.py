#!/usr/bin/env python

import time


def collatz_gen(n):
    if n == 1:
        return 1
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        yield n


def wrapper(n):
    if n in memo:
        return memo[n]
    for i, x in enumerate(collatz_gen(n)):
        if x == 1:
            memo[n] = i + 2
            return
        elif x in memo:
            memo[n] = memo[x] + i + 1
            return


def main():
    """
    Using memoization
    """
    global memo
    memo = {}
    for n in range(1, 1000000):
        wrapper(n)
    n_longest_seq = max(iter(memo), key=(lambda key: memo[key]))
    print('n under 1 000 000 with longest collatz chain: %d' % n_longest_seq)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
