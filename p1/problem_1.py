#!/usr/bin/env python


def summate(n):
    return (n * (n + 1)) // 2

def main():
    bound = 999
    print(3 * summate(bound // 3 ) + 5 * summate(bound // 5) - 15 * summate(bound // 15))

main()
