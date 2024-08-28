import sympy as sp
from fuzzyCalc.representations.fuzzyI import *


class TrapezoidJiMa(FuzzyNumber):
    """Jiménez & Mateos' Trapezoidal Representation
    This is an implementation of a trapezoidal representation for fuzzy numbers and operations, proposed
    in [1], for arithmetic calculations between fuzzy numbers.

    References:
        [1] A. Mateos and A. Jiménez, “A trapezoidal fuzzy numbers-based approach for aggregating group preferences
        and ranking decision alternatives in MCDM,” in Lecture Notes in Computer Science (including subseries Lecture
        Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 5467 LNCS. Springer, Berlin,
        Heidelberg, 2010, pp. 365-379. [Online].
        Available: https://link.springer.com/chapter/10.1007/978-3-642-01020-0_30

    """
    def __init__(self, *args):
        if len(args) == 3:
            self.a = args[0]
            self.b = args[1]
            self.c = args[1]
            self.d = args[2]
        elif len(args) == 4:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]

    def addition(self, trap):
        a = self.a + trap.a
        b = self.b + trap.b
        c = self.c + trap.c
        d = self.d + trap.d
        resp = TrapezoidJiMa(a, b, c, d)
        return resp

    def subtraction(self, trap):
        a = self.a - trap.d
        b = self.b - trap.c
        c = self.c - trap.b
        d = self.d - trap.a
        resp = TrapezoidJiMa(a, b, c, d)
        return resp

    def multiplication(self, trap):
        a = ((3 / 2) * (self.b - self.a) * (trap.b - trap.a)) + (2 * (trap.a * (self.b - self.a) +
                                                                      self.a * (trap.b - trap.a))) + (
                        3 * trap.a * self.a) - (2 * self.b * trap.b)
        b = self.b * trap.b
        c = self.c * trap.c
        d = ((3 / 2) * (self.d - self.c) * (trap.d - trap.c)) - (2 * ((self.d - self.c) *
                                                                      trap.c + (trap.d - trap.c) * self.d)) + (
                        3 * self.d * trap.d) - (2 * self.c * trap.c)
        return TrapezoidJiMa(a, b, c, d)

    def output(self):
        return f'({self.a:.2f}, {self.b:.2f}, {self.c:.2f}, {self.d:.2f})'

    def trapezoidal(self):
        return self

    def representation(self):
        return "trapezoidal"

    def toCartesian(self):
        return [float(self.a), float(self.b), float(self.c), float(self.d)]


class TrapecioTaRe(FuzzyNumber):
    """Taleshian & Rezvani's Trapezoidal Representation
    This is an implementation of a trapezoidal representation for fuzzy numbers and operations, proposed
    in [1], for arithmetic calculations between fuzzy numbers.

    References:
        [1] A. Taleshian and S. Rezvani, “Multiplication operation on trapezoidal fuzzy numbers,” Journal of Physical
        Science, vol. 15, 01 2011

    """
    
    def __init__(self, *args):
        if len(args) == 3:
            self.a = args[0]
            self.b = args[1]
            self.c = args[1]
            self.d = args[2]
        elif len(args) == 4:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]
            self.d = args[3]

    def addition(self, trap):
        a = self.a + trap.a
        b = self.b + trap.b
        c = self.c + trap.c
        d = self.d + trap.d
        resp = TrapecioTaRe(a, b, c, d)
        return resp

    def subtraction(self, trap):
        a = self.a - trap.b
        b = self.b - trap.a
        c = self.c + trap.c
        d = self.d + trap.d
        resp = TrapecioTaRe(a, b, c, d)
        return resp

    def multiplication(self, trap):
        a = self.a * trap.a
        b = self.b * trap.b
        c = self.c * trap.c
        d = self.d * trap.d

        return TrapecioTaRe(a, b, c, d)

    def output(self):
        return f'({self.a:.2f}, {self.b:.2f}, {self.c:.2f}, {self.d:.2f})'

    def trapezoidal(self):
        return self

    def representation(self):
        return "trapezoidal"

    def toCartesian(self):
        return [float(self.a), float(self.b), float(self.c), float(self.d)]


class TrapezoidSteSoGue(FuzzyNumber):
    """Stefanini, Sorini & Guerra's Trapezoidal Representation
    This is an implementation of a trapezoidal representation for fuzzy numbers and operations, proposed in [1], for
    arithmetic calculations between fuzzy numbers.

    References:
        [1] L. Stefanini, L. Sorini, and M. L. Guerra, “Parametric representation of fuzzy numbers and application to
        fuzzy calculus,” Fuzzy Sets and Systems, vol. 157, no. 18, pp. 2423–2455, sep 2006

    """

    alpha = sp.symbols('a')

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
        self.left = (b - a) * self.alpha + a
        self.right = (c - d) * self.alpha + d

    def addition(self, interval):
        left = self.left + interval.left
        right = self.right + interval.right
        inter = TrapezoidSteSoGue(0, 0, 0, 0)
        inter.left = left
        inter.right = right
        return inter

    def subtraction(self, interval):
        left = self.left - interval.right
        right = self.right - interval.left
        inter = TrapezoidSteSoGue(0, 0, 0, 0)
        inter.left = left
        inter.right = right
        return inter

    def multiplication(self, interval):
        left = self.left * interval.left
        right = self.right * interval.right
        inter = TrapezoidSteSoGue(0, 0, 0, 0)
        inter.left = left
        inter.right = right
        return inter

    def output(self):
        return f'[{self.left} , {self.right}]'

    def trapezoidal(self):
        a = self.left.subs(self.alpha, 0)
        b = self.left.subs(self.alpha, 1)
        c = self.right.subs(self.alpha, 1)
        d = self.right.subs(self.alpha, 0)
        return TrapezoidJiMa(float(a), float(b), float(c), float(d))

    def representation(self):
        return "trapezoidal"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]


class TrapezoidGrMr(FuzzyNumber):
    """Grzegorzewski & Mrówka's Trapezoidal Representation
    This is an implementation of a trapezoidal representation for fuzzy numbers and operations, proposed in [1], for
    arithmetic calculations between fuzzy numbers.

    References:
        [1] P. Grzegorzewski and E. Mrówka, “Trapezoidal approximations of fuzzy numbers,” Fuzzy Sets and Systems,
        vol. 153, no. 1, pp. 115–135, jul 2005.

    """

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
        left1 = ((1 / 2) * a + (1 / 3) * (b - a))
        left2 = (a + (1 / 2) * (b - a))
        right1 = ((1 / 2) * d + (1 / 3) * (c - d))
        right2 = (d + (1 / 2) * (c - d))
        self.t1 = -6 * left1 + 4 * left2
        self.t2 = 6 * left1 - 2 * left2
        self.t3 = 6 * right1 - 2 * right2
        self.t4 = -6 * right1 + 4 * right2

    def addition(self, trap):
        a = self.t1 + trap.t1
        b = self.t2 + trap.t2
        c = self.t3 + trap.t3
        d = self.t4 + trap.t4
        resp = TrapezoidGrMr(0, 0, 0, 0)
        resp.t1, resp.t2, resp.t3, resp.t4 = a, b, c, d
        return resp

    def subtraction(self, trap):
        a = self.t1 - trap.t4
        b = self.t2 - trap.t3
        c = self.t3 - trap.t2
        d = self.t4 - trap.t1
        resp = TrapezoidGrMr(0, 0, 0, 0)
        resp.t1, resp.t2, resp.t3, resp.t4 = a, b, c, d
        return resp

    def multiplication(self, trap):
        a = self.t1 * trap.t1
        b = self.t2 * trap.t2
        c = self.t3 * trap.t3
        d = self.t4 * trap.t4
        resp = TrapezoidGrMr(0, 0, 0, 0)
        resp.t1, resp.t2, resp.t3, resp.t4 = a, b, c, d
        return resp

    def output(self):
        return f'({self.t1:.2f}, {self.t2:.2f}, {self.t3:.2f}, {self.t4:.2f})'

    def trapezoidal(self):
        return self

    def representation(self):
        return "trapezoidal"

    def toCartesian(self):
        return [float(self.t1), float(self.t2), float(self.t3), float(self.t4)]
