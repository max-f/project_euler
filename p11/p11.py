#!/usr/bin/env python

import time

#import numpy as np

#def window_stack(a, stepsize=1, width=4):
#    return np.hstack( a[i:1+i-width or None:stepsize] for i in range(0,width) )

start = time.time()

def main():
    max_p = 0
    M = list()
    with open('grid.txt', 'r') as f:
        for line in f.readlines():
            i = line.split()
            M.append([int(j) for j in i])

    # M: 20x20 matrix
    for i in range(20):
        for j in range(17):
            # horizontal:
            p = M[i][j] * M[i][j+1] * M[i][j+2] * M[i][j+3]
            if p > max_p:
                max_p = p
            # vertical:
            p = M[j][i] * M[j+1][i] * M[j+2][i] * M[j+3][i]
            if p > max_p:
                max_p = p

    # diagonal:
    # upper right - bottom left
    for i in range(3,20):
        for j in range(17):
            p = M[i][j] * M[i-1][j+1] * M[i-2][j+2] * M[i-3][j+3]
            if p > max_p:
                max_p = p
    # upper left - bottom right
    for i in range(17):
        for j in range(17):
            p = M[i][j] * M[i+1][j+1] * M[i+2][j+2] * M[i+3][j+3]
            if p > max_p:
                max_p = p

    print('Calulated {0} in {1} seconds'.format(max_p, time.time() - start))

main()
