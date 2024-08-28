from fuzzyCalc.representations.fuzzyI import FuzzyNumber


class Gauss(FuzzyNumber):
    """Leandry, Sosoma, & Koloseni's Gaussian Representation
    This is an implementation of a Gaussian representation for gaussian fuzzy numbers and operations, proposed in [1],
    for arithmetic calculations between fuzzy numbers.

    References:
        [1] L. Leandry, I. Sosoma, and D. Koloseni, “Basic fuzzy arithmetic operations using α-cut for the gaussian
        membership function,” Journal of Fuzzy Extension and Applications, vol. 3, no. 4, pp. 337-348, 2022. [Online].
        Available: https://www.journal-fea.com/article 153240.html
    """
    def __init__(self, *args):
        self.m = args[0]
        self.σ = args[1]

    def addition(self, gaussian):
        m = self.m + gaussian.m
        σ = self.σ + self.σ
        return Gauss(m, σ)

    def subtraction(self, gaussian):
        m = self.m - gaussian.m
        σ = self.σ
        return Gauss(m, σ)

    def multiplication(self, gaussian):
        m = self.m * gaussian.m
        σ = self.σ
        return Gauss(m, σ)

    def output(self):
        return f'[{self.m} - {self.σ}*sqrt(-2ln(a)), {self.m} + {self.σ}*sqrt(-2ln(a))]'

    def representation(self):
        return "gaussian"

    def toCartesian(self):
        return [self.m, self.σ]
