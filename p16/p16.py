#!/usr/bin/env python

import time

start = time.time()

def main():
    n = 2 ** 1000
    n_str_list = list(str(n))
    n_int_list = [int(x) for x in n_str_list]
    print('Calculated {0} in {1} seconds'.format(sum(n_int_list), time.time() -
        start))

main()
