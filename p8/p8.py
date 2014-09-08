#!/usr/bin/env python

from itertools import islice

i = 13

def n_grams(a, i):
    z = (islice(a, x, None) for x in range(i))
    return zip(*z)

def main():
    a = list()
    with open('number.txt', 'r') as f:
        for line in f:
            line = line.strip('\n')
            a.extend(list(str(line)))
    search_space = n_grams(a, i)
    # search_space = [int(x) for x in search_space]
    max = 0
    for n_gram in search_space:
        n_gram = [int(x) for x in n_gram]
        m = 1
        for y in n_gram:
            m *= y
        if m > max:
            max = m
    print(max)

main()
