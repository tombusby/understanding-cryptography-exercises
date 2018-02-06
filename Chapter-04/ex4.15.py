#!/usr/bin/env python
# coding: utf-8
from gf import Mod2Polynomial

if __name__ == "__main__":
    template = u"R[{}] = {} = {}₂ = {}₁₆"
    reduction_polynomial = Mod2Polynomial([1, 1, 0, 1, 1, 0, 0, 0, 1])
    poly = Mod2Polynomial([1])
    p02 = Mod2Polynomial([0, 1])
    print template.format(1, poly, poly.get_binary_representation(), "01")
    for i in range(2, 11):
        previous = poly
        poly = (previous * p02) % reduction_polynomial
        bin_rep = poly.get_binary_representation()
        print template.format(i, poly, bin_rep, hex(int(bin_rep, 2)).lstrip("-0x").zfill(2).upper())
