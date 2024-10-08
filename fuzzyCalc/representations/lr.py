from fuzzyCalc.representations.trapezoid import *


class LRFoBe(FuzzyNumber):
    """Fodor & Bede's L-R Representation
    This is an implementation of an L-R representation for trapezoidal fuzzy numbers and operations, proposed in [1],
    for arithmetic calculations between fuzzy numbers.

    References:
        [1] J. Fodor and B. Bede, “Arithmetics with fuzzy numbers: a comparative overview,” 2006.

    """

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
        return TrapezoidJiMa(float(a), float(b), float(c), float(d))

    def representation(self):
        return "L-R"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]


class LRWiRoSt(FuzzyNumber):
    """Williams, Robinson & Steele's L-R Representation
     This is an implementation of an L-R representation for trapezoidal fuzzy numbers and operations, proposed by
     Williams, Robinson & Steele, for arithmetic calculations between fuzzy numbers [1].

     References:
        [1] J. Williams, H. Robinson, and N. Steele, “Applying ma et al’s new fuzzy
        arithmetic to triangular and trapezoidal fuzzy numbers,” Proceedings of
        the 4th International Conference on Recent Advances in Soft Computing,
        2002.

    """

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
        res = LRWiRoSt(0, 0, 0, 0)
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
        res = LRWiRoSt(0, 0, 0, 0)
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
        res = LRWiRoSt(0, 0, 0, 0)
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
        return TrapezoidJiMa(float(a), float(b), float(c), float(d))


    def representation(self):
        return "L-R"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]
