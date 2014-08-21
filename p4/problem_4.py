#!/usr/bin/env python

def is_palindrome(n):
    x = str(n)
    if x[::-1] == x:
        return True
    return False


def is_divisible(n):
    upper = 1000
    lower = 100
    x = upper
    while x >= lower:
        x -= 1
        if n % x != 0:
            continue
        y = int(n / x)
        if y <= upper and y >= lower:
            print(x, y)
            return True
    return False



def main():
    upper = 999 * 999
    lower = 100 * 100
    while upper >= lower:
        if is_palindrome(upper) and is_divisible(upper):
            print(upper)
            return
        upper -= 1

main()
