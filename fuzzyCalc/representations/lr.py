import sympy as sp
from fuzzyCalc.representations.fuzzyI import *
from fuzzyCalc.representations.trapezoid import *

# L-R Fuzzy number representation for trapezoidal fuzzy numbers
# Fodor & Bede, 2006
# Arithmetics with fuzzy numbers: a comparative overview


class LRFoBe(FuzzyNumber):
    a = sp.symbols('a')

    def __init__(self, *args):
        if len(args) == 3:
            a = args[0]
            b = args[1]
            c = args[1]
            d = args[2]
        elif len(args) == 4:
            a = args[0]
            b = args[1]
            c = args[2]
            d = args[3]

        self.m = (b+c)/2
        self.u = self.m - c
        self.l = self.m - a
        self.r = d - self.m

    def left(self, lr, cut):
        u = self.l - cut*(self.l - self.u)
        v = lr.l - cut*(lr.l - lr.u)
        return max(u, v)

    def right(self, lr, cut):
        u = self.r - cut*(self.r - self.u)
        v = lr.r - cut*(lr.r - lr.u)
        return max(u, v)

    def addition(self, lr):
        m = self.m + lr.m
        a = m - self.left(lr, 0)
        b = m - self.left(lr, 1)
        c = m + self.right(lr, 1)
        d = m + self.right(lr, 0)
        return LRFoBe(a, b, c, d)

    def subtraction(self, lr):
        m = self.m - lr.m
        a = m - self.left(lr, 0)
        b = m - self.left(lr, 1)
        c = m + self.right(lr, 1)
        d = m + self.right(lr, 0)
        return LRFoBe(a, b, c, d)

    def multiplication(self, lr):
        m = self.m * lr.m
        a = m - self.left(lr, 0)
        b = m - self.left(lr, 1)
        c = m + self.right(lr, 1)
        d = m + self.right(lr, 0)
        return LRFoBe(a, b, c, d)

    def output(self):
        return f'[{(self.m - self.l):.2f} + {(self.l - self.u):.2f}*a, {(self.m + self.r):.2f} + {(self.u - self.r):.2f}*a]'

    def trapezoidal(self):
        left = self.m - self.l + self.a*(self.l - self.u)
        right = self.m + self.r + self.a*(self.u - self.r)
        a = left.subs(self.a, 0)
        b = left.subs(self.a, 1)
        c = right.subs(self.a, 1)
        d = right.subs(self.a, 0)
        return TrapecioJiMa(float(a), float(b), float(c), float(d))

    def representation(self):
        return "lr"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]

# Simplification of Ma et al
# Robinson & Steele, 2002 shown in Fodor & Bede, 2006
# Arithmetics with fuzzy numbers: a comparative overview


class LRRoSt(FuzzyNumber):
    a = sp.symbols('a')

    def __init__(self, *args):
        if len(args) == 3:
            a = args[0]
            b = args[1]
            c = args[1]
            d = args[2]
        elif len(args) == 4:
            a = args[0]
            b = args[1]
            c = args[2]
            d = args[3]

        self.m = (b+c)/2
        self.u = self.m - c
        self.l = self.m - a
        self.r = d - self.m

    def left(self, lr):
        return max(self.l, lr.l)

    def right(self, lr):
        return max(self.r, lr.r)

    def upper(self, lr):
        return max(self.u, lr.u)

    def addition(self, lr):
        m = self.m + lr.m
        left = self.left(lr)
        right = self.right(lr)
        upper = self.upper(lr)
        res = LRRoSt(0, 0, 0, 0)
        res.m = m
        res.l = left
        res.r = right
        res.u = upper
        return res

    def subtraction(self, lr):
        m = self.m - lr.m
        left = self.left(lr)
        right = self.right(lr)
        upper = self.upper(lr)
        res = LRRoSt(0, 0, 0, 0)
        res.m = m
        res.l = left
        res.r = right
        res.u = upper
        return res

    def multiplication(self, lr):
        m = self.m * lr.m
        left = self.left(lr)
        right = self.right(lr)
        upper = self.upper(lr)
        res = LRRoSt(0, 0, 0, 0)
        res.m = m
        res.l = left
        res.r = right
        res.u = upper
        return res

    def output(self):
        return f'({self.m:.2f}, {self.u:.2f}, {self.l:.2f}, {self.r:.2f})'

    def trapezoidal(self):
        left = self.m - self.l + self.a*(self.l - self.u)
        right = self.m + self.r + self.a*(self.u - self.r)
        a = left.subs(self.a, 0)
        b = right.subs(self.a, 1)
        c = left.subs(self.a, 1)
        d = right.subs(self.a, 0)
        return TrapecioJiMa(float(a), float(b), float(c), float(d))


    def representation(self):
        return "lr"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]
