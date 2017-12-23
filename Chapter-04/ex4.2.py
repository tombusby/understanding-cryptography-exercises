#!/usr/bin/env python
from pprint import pprint

def generate_addition_table(n):
    row = [0] * 7
    table = [row[:] for i in range(0, n)]
    for a, b, c in [(a, b,  (a+b) % 7) for a in range(0,n) for b in range(0,n)]:
        table[a][b] = c
    return table

def generate_multiplication_table(n):
    row = [0] * 7
    table = [row[:] for i in range(0, n)]
    for a, b, c in [(a, b, (a*b) % 7) for a in range(0,n) for b in range(0,n)]:
        table[a][b] = c
    return table

if __name__ == "__main__":
    n = 7
    print "Addition Table GF({}):".format(n)
    pprint(generate_addition_table(7))
    print "Multiplication Table GF({}):".format(n)
    pprint(generate_multiplication_table(7))
