#!/usr/bin/env python

import time


def main():
    # a < b < c
    a = 0
    b = 0
    c = 0
    s = 1000
    for a in range(1, int(s / 3) + 1):  # a < (s / 3)
        for b in range(a + 1, int(s / 2) + 1):  # b < (s / 2)
            c = s - a - b
            if (c ** 2 == a ** 2 + b ** 2):
                print('Pythagorean triplet a = %d, '
                      'b = %d, and c = %d' % (a, b, c))
                print('Product: abc = %d' % (a * b * c))
                return

if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
