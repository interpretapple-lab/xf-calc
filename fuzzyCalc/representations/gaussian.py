from numpy import log as ln
import sympy as sp

from fuzzyCalc.representations.fuzzyI import FuzzyNumber
from fuzzyCalc.representations.trapezoid import TrapecioJiMa


class Gauss(FuzzyNumber):

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

    def output(self):
        return f'[{self.m} - {self.σ}*sqrt(-2ln(a)), {self.m} + {self.σ}*sqrt(-2ln(a))]'

    def representation(self):
        return "gaussian"

    def toCartesian(self):
        return [self.m, self.σ]
