from numpy import log as ln
import sympy as sp

from representations.fuzzyI import FuzzyNumber
from representations.trapezoid import TrapecioJiMa


class Gauss(FuzzyNumber):
    alpha = sp.symbols('α')

    def __init__(self, *args):
        self.m = args[0]
        self.σ = args[1]

    def suma(self, gaussian):
        m = self.m + gaussian.m
        σ = self.σ + self.σ
        return Gauss(m, σ)

    def resta(self, gaussian):
        m = self.m - gaussian.m
        σ = self.σ
        return Gauss(m, σ)

    def multiplicacion(self, gaussian):
        m = self.m * gaussian.m
        σ = self.σ
        return Gauss(m, σ)

    def imprimir(self):
        left = self.m - self.l + self.alpha*(self.l - self.u)
        right = self.m + self.r + self.alpha*(self.u - self.r)
        print("[", left, ",", right, "]")

    def trapezoidal(self):
        # Cambiar
        left = self.m - self.l + self.alpha*(self.l - self.u)
        right = self.m + self.r + self.alpha*(self.u - self.r)
        a = left.subs(self.alpha, 0)
        b = left.subs(self.alpha, 1)
        c = right.subs(self.alpha, 1)
        d = right.subs(self.alpha, 0)
        return TrapecioJiMa(float(a), float(b), float(c), float(d))

    def representation(self):
        return "gaussian"

    def lista(self):
        return [self.m, self.σ]
