#!/usr/bin/env python

import time


def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def summate(lines, n):
    """
    Summates just the first n positions of numbers
    """
    return sum([int(l[:n]) for l in lines])


def main():
    """
    Only the first 11 digits can possibly influence the first 10 digits of
    the final sum.
    """
    filename = 'numbers.txt'
    lines = read_file(filename)
    sum = summate(lines, 11)
    print('First 10 digits of the sum: %s' % str(sum)[:10])

if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
