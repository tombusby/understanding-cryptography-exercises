#!/usr/bin/env python

from gf import Mod2Polynomial

if __name__ == "__main__":
    # smallest power (x^0) on the left, largest on the right
    mod = Mod2Polynomial([1, 1, 0, 1])
    def all_poss_vectors():
        # ordering reversal counters the lowest-power-first input to Mod2Polynomial and
        # ensures that the ordering of the for loop below is not nonsensical
        return [[c,b,a] for a in [0,1] for b in [0,1] for c in [0,1]]
    for (a, b) in [(a, b) for a in all_poss_vectors() for b in all_poss_vectors()]:
        a = Mod2Polynomial(a)
        b = Mod2Polynomial(b)
        print str(a), "*", str(b), "\n=", str((a * b) % mod), "\n"
