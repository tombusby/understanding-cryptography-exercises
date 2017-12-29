#!/usr/bin/env python

class Mod2Polynomial:

    def __init__(self, vector):
        self.vector = [0] * len(vector)
        i = 0
        for p in vector:
            self.vector[i] = int(bool(p))
            i += 1

    def __str__(self):
        def monomial_str(order):
            if order > 0:
                return "x^{}".format(order)
            else:
                return "1"
        indexed_coefficients = zip(self.vector, range(0, len(self.vector)))
        polynomial_string = [monomial_str(o) if c else "" for c, o in indexed_coefficients]
        return " + ".join(reversed(filter(bool, polynomial_string)))

    def __add__(self, polynomial):
        size = max(self.get_order(), polynomial.get_order()) + 1
        a = self.vector + [0] * (size - len(self.vector))
        b = polynomial.vector + [0] * (size - len(polynomial.vector))
        return Mod2Polynomial([(ac + bc) % 2 for ac, bc in zip(a, b)])

    def __radd__(self, polynomial):
        return self.__add__(polynomial)

    def __mul__(self, polynomial):
        vector = [0] * (self.get_order() + polynomial.get_order() + 2)
        i1 = 0
        for p1 in self.vector:
            i2 = 0
            for p2 in polynomial.vector:
                vector[i1 + i2] = (vector[i1 + i2] + (p1 * p2)) % 2
                i2 += 1
            i1 += 1
        return Mod2Polynomial(vector)

    def __rmul__(self, polynomial):
        return self.__mul__(polynomial)

    def __mod__(self, divisor):
        def make_monomial(n):
            vector = [0] * (n+1)
            vector[n] = 1
            return Mod2Polynomial(vector)
        dividend = Mod2Polynomial(self.vector[:])
        quotient = Mod2Polynomial([0] * (max(self.get_order(), divisor.get_order()) + 1))
        divisor_order = divisor.get_order()
        while divisor_order < dividend.get_order():
            monomial = make_monomial(dividend.get_order() - divisor_order)
            quotient += monomial
            dividend += (monomial * divisor)
        return dividend

    def __rmod__(self, polynomial):
        return self.__mod__(polynomial)

    def get_order(self):
        i = 0
        order = 0
        for p in self.vector:
            if p: order = i
            i += 1
        return order

if __name__ == "__main__":
    # smallest power (x^0) on the left, largest on the right
    a = Mod2Polynomial([0, 0, 1])
    b = Mod2Polynomial([1, 0, 1])
    mod = Mod2Polynomial([1, 1, 0, 1])
    print (a * b) % mod
