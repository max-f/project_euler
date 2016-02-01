#!/usr/bin/env python


def sum_of_squares(n):
    """Closed form: https://en.wikipedia.org/wiki/Square_pyramidal_number"""
    return (n ** 3 / 3) + (n ** 2 / 2) + (n / 6)


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


def main():
    n = 100
    print(square_of_sum(n) - sum_of_squares(n))

main()
