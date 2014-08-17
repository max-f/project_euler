#!/usr/bin/env python
import math

bound = 4000000

"""
Using explicit formula of Moivre-Binet
def fib(n):
    return  (1/math.sqrt(5) * (((1 + math.sqrt(5))/2) ** n - ((1 +
        math.sqrt(5))/2) ** n))
"""


def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def main():
    all_fibs = list()
    for x in fib():
        if x > bound:
            break
        all_fibs.append(x)
    print(sum(list(filter((lambda x: x % 2 == 0), all_fibs))))

main()
