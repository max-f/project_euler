#!/usr/bin/env python

def summate(n):
    return (n * (n + 1)) / 2

def main():
    n = 100
    sum_of_squares = sum([x ** 2 for x in range(1,101)])
    total_sum = summate(n)
    square_of_sum = total_sum ** 2
    print(square_of_sum - sum_of_squares)

main()
