
class Mod2Polynomial:

    def __init__(self, vector):
        while len(vector) and not vector[-1]:
            vector.pop()
        self.vector = [0] * len(vector)
        i = 0
        for p in vector:
            self.vector[i] = int(bool(p))
            i += 1

    def __str__(self):
        def monomial_str(order):
            if order == 1:
                return "x"
            elif order > 0:
                return "x^{}".format(order)
            else:
                return "1"
        indexed_coefficients = zip(self.vector, range(0, len(self.vector)))
        polynomial_string = filter(bool, [monomial_str(o) if c else "" for c, o in indexed_coefficients])
        return " + ".join(reversed(polynomial_string)) if polynomial_string else "0"

    def __add__(self, polynomial):
        size = max(self.get_order(), polynomial.get_order()) + 1
        a = self.vector + [0] * (size - len(self.vector))
        b = polynomial.vector + [0] * (size - len(polynomial.vector))
        return Mod2Polynomial([(ac + bc) % 2 for ac, bc in zip(a, b)])

    def __mul__(self, polynomial):
        if self.is_zero() or polynomial.is_zero():
            return Mod2Polynomial([])
        vector = [0] * (self.get_order() + polynomial.get_order() + 2)
        i1 = 0
        for p1 in self.vector:
            i2 = 0
            for p2 in polynomial.vector:
                vector[i1 + i2] = (vector[i1 + i2] + (p1 * p2)) % 2
                i2 += 1
            i1 += 1
        return Mod2Polynomial(vector)

    def __mod__(self, divisor):
        def make_monomial(n):
            vector = [0] * (n+1)
            vector[n] = 1
            return Mod2Polynomial(vector)
        dividend = Mod2Polynomial(self.vector[:])
        quotient = Mod2Polynomial([0] * (max(self.get_order(), divisor.get_order()) + 1))
        divisor_order = divisor.get_order()
        if not divisor_order:
            raise ZeroDivisionError
        while divisor_order <= dividend.get_order():
            monomial = make_monomial(dividend.get_order() - divisor_order)
            quotient += monomial
            dividend += (monomial * divisor)
        return dividend

    def get_order(self):
        i = 0
        order = 0
        for p in self.vector:
            if p: order = i
            i += 1
        return order

    def is_zero(self):
        return not any(self.vector)
