import sympy as sp
from sympy import Symbol
from representations.fuzzyI import *


# Arithmetic approximations for trapezoidal fuzzy numbers shown in:
# Jiménez & Mateos 2009
# https://doi.org/10.1007/978-3-642-01020-0_30
class TrapecioJiMa(FuzzyNumber):
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

    def suma(self, trap):
        a = self.a + trap.a
        b = self.b + trap.b
        c = self.c + trap.c
        d = self.d + trap.d
        respuesta = TrapecioJiMa(a, b, c, d)
        return respuesta

    def resta(self, trap):
        a = self.a - trap.d
        b = self.b - trap.c
        c = self.c - trap.b
        d = self.d - trap.a
        respuesta = TrapecioJiMa(a, b, c, d)
        return respuesta

    def multiplicacion(self, trap):
        a = ((3/2)*(self.b-self.a)*(trap.b-trap.a)) + (2*(trap.a*(self.b - self.a) +
                                                          self.a*(trap.b - trap.a))) + (3*trap.a*self.a) - (2*self.b*trap.b)
        b = self.b * trap.b
        c = self.c * trap.c
        d = ((3/2)*(self.d-self.c)*(trap.d-trap.c)) - (2*((self.d-self.c) *
                                                          trap.c+(trap.d-trap.c)*self.d)) + (3*self.d*trap.d) - (2*self.c*trap.c)
        return TrapecioJiMa(a, b, c, d)

    def output(self):
        return f'({self.a:.2f}, {self.b:.2f}, {self.c:.2f}, {self.d:.2f})'

    def trapezoidal(self):
        return self


    def representation(self):
        return "trapezoid"

    def toCartesian(self):
        return [float(self.a), float(self.b), float(self.c), float(self.d)]

# Arithmetic approximations for trapezoidal fuzzy numbers shown in:
# A.Taleshian & S.Rezvani 2011
# ISSN 0972-8791


class TrapecioTaRe(FuzzyNumber):
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

    def suma(self, trap):
        a = self.a + trap.a
        b = self.b + trap.b
        c = self.c + trap.c
        d = self.d + trap.d
        respuesta = TrapecioTaRe(a, b, c, d)
        return respuesta

    def resta(self, trap):
        a = self.a - trap.b
        b = self.b - trap.a
        c = self.c + trap.c
        d = self.d + trap.d
        respuesta = TrapecioTaRe(a, b, c, d)
        return respuesta

    def multiplicacion(self, trap):
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
        return "trapezoid"
    
    def toCartesian(self):
        return [float(self.a), float(self.b), float(self.c), float(self.d)]

# Interval representation shown in:
# Stefanini, Sorini & Guerra 2006
# https://doi.org/10.1016/j.fss.2006.02.002


class TrapecioSteSoGue(FuzzyNumber):
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
        self.left = (b-a)*self.alpha + a
        self.right = (c-d)*self.alpha + d

    def suma(self, intervalo):
        left = self.left + intervalo.left
        right = self.right + intervalo.right
        inter = TrapecioSteSoGue(0, 0, 0, 0)
        inter.left = left
        inter.right = right
        return inter

    def resta(self, intervalo):
        left = self.left - intervalo.right
        right = self.right - intervalo.left
        inter = TrapecioSteSoGue(0, 0, 0, 0)
        inter.left = left
        inter.right = right
        return inter

    def multiplicacion(self, intervalo):
        left = self.left * intervalo.left
        right = self.right * intervalo.right
        inter = TrapecioSteSoGue(0, 0, 0, 0)
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
        return TrapecioJiMa(float(a), float(b), float(c), float(d))

    def representation(self):
        return "trapezoid"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]

#Grzegorzewski & Mrówka, 2004
# https://doi.org/10.1016/j.fss.2004.02.015


class TrapecioGrMr(FuzzyNumber):
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
        left1 = ((1/2)*a + (1/3)*(b-a))
        left2 = (a + (1/2)*(b-a))
        right1 = ((1/2)*d + (1/3)*(c-d))
        right2 = (d + (1/2)*(c-d))
        self.t1 = -6*left1 + 4*left2
        self.t2 = 6*left1 - 2*left2
        self.t3 = 6*right1 - 2*right2
        self.t4 = -6*right1 + 4*right2

    def suma(self, trap):
        a = self.t1 + trap.t1
        b = self.t2 + trap.t2
        c = self.t3 + trap.t3
        d = self.t4 + trap.t4
        respuesta = TrapecioGrMr(0, 0, 0, 0)
        respuesta.t1, respuesta.t2, respuesta.t3, respuesta.t4 = a, b, c, d
        return respuesta

    def resta(self, trap):
        a = self.t1 - trap.t4
        b = self.t2 - trap.t3
        c = self.t3 - trap.t2
        d = self.t4 - trap.t1
        respuesta = TrapecioGrMr(0, 0, 0, 0)
        respuesta.t1, respuesta.t2, respuesta.t3, respuesta.t4 = a, b, c, d
        return respuesta

    def multiplicacion(self, trap):
        a = self.t1 * trap.t1
        b = self.t2 * trap.t2
        c = self.t3 * trap.t3
        d = self.t4 * trap.t4
        respuesta = TrapecioGrMr(0, 0, 0, 0)
        respuesta.t1, respuesta.t2, respuesta.t3, respuesta.t4 = a, b, c, d
        return respuesta

    def output(self):
        return f'({self.t1:.2f}, {self.t2:.2f}, {self.t3:.2f}, {self.t4:.2f})'

    def trapezoidal(self):
        return self

    def representation(self):
        return "trapezoid"

    def toCartesian(self):
        return [float(self.t1), float(self.t2), float(self.t3), float(self.t4)]
