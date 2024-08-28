from fuzzyCalc.representations.trapezoid import *


class TriangularKauGu(FuzzyNumber):
    """Kaufmann and Gupta's Triangular Representation
    This is an implementation of a triangular representation for fuzzy numbers and operations, proposed by Kaufmann and
    Gupta, for arithmetic calculations between fuzzy numbers [1].

    References:
        [1] A. Kaufmann and M. Gupta, Introduction to Fuzzy Arithmetic: Theory
        and Applications, ser. Electrical-Computer Science and Engineering
        Series. Van Nostrand Reinhold Company, 1985.

    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, triangular):
        a = self.x + triangular.x
        b = self.y + triangular.y
        c = self.z + triangular.z
        return TriangularKauGu(a, b, c)

    def subtraction(self, triangular):
        a = self.x - triangular.z
        b = self.y - triangular.y
        c = self.z - triangular.x
        return TriangularKauGu(a, b, c)

    def multiplication(self, triangular):
        a = self.x * triangular.x
        b = self.y * triangular.y
        c = self.z * triangular.z
        return TriangularKauGu(a, b, c)

    def output(self):
        return f'({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'

    def trapezoidal(self):
        return TrapezoidJiMa(float(self.x), float(self.y), float(self.y), float(self.z))

    def representation(self):
        return "triangular"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]


class TriangularGiaYo(FuzzyNumber):
    """Giachetti & Young's Triangular Representation
    This is an implementation of a triangular representation for fuzzy numbers and operations, proposed in [1], for
    arithmetic calculations between fuzzy numbers.

    References:
        [1] R. E. Giachetti and R. E. Young, “A parametric representation of fuzzy numbers and their arithmetic
        operators,” Fuzzy Sets and Systems, vol. 91, no. 2, pp. 185-202, oct 1997

    """

    alpha = sp.symbols('a')

    def __init__(self, x, y, z, lamda, rho, n):
        self.x = x
        self.y = y
        self.z = z
        self.left = (y - x) * self.alpha + x
        self.right = (y - z) * self.alpha + z
        self.lamda = lamda
        self.rho = rho
        self.n = n

    # multiplication
    def tauLeft(self, lamda, n):
        res = 0.568 * lamda + 0.11 * n - 0.859
        return res

    def tauRight(self, rho, n):
        res = -1.85 * rho + 0.144 * n + 1.19
        return res

    def corrPolynomial(self, alpha, n):
        result = 0
        for i in range(n, 0, -1):
            if i % 2 == 0:
                result += alpha ** i
            else:
                result -= alpha ** i
        return result

    def prodLeft(self, parametric):
        res = (self.x * parametric.x) * \
              (((parametric.lamda * self.lamda - 1) * self.alpha) + 1)
        return res

    def prodRight(self, parametric):
        res = (self.z * parametric.z) * \
              (((parametric.rho * self.rho - 1) * self.alpha) + 1)
        return res

    def resProdLeft(self, parametric):

        num = self.n + parametric.n

        lamda = ((self.lamda ** self.n) *
                 (parametric.lamda ** parametric.n)) ** (1 / num)
        polynomial = self.corrPolynomial(self.alpha, num)

        prodLeft = self.prodLeft(parametric)

        left = prodLeft + (polynomial * self.tauLeft(num, lamda)
                           * (self.y * parametric.y - self.x * parametric.x))

        return left

    def resProdRight(self, parametric):
        num = self.n + parametric.n
        polynomial = self.corrPolynomial(self.alpha, num)
        rho = ((self.rho ** self.n) * (parametric.rho ** parametric.n)) ** (1 / num)
        prodRight = self.prodRight(parametric)
        right = prodRight + polynomial * \
                self.tauRight(num, rho) * (self.z *
                                           parametric.z - self.y * parametric.y)

        return right

    def multiplication(self, parametric):
        left = self.resProdLeft(parametric)
        right = self.resProdRight(parametric)
        a = left.subs(self.alpha, 0)
        b = left.subs(self.alpha, 1)
        c = right.subs(self.alpha, 0)
        num = self.n + parametric.n
        rho = ((self.rho ** self.n) * (parametric.rho ** parametric.n)) ** (1 / num)
        lamda = ((self.lamda ** self.n) *
                 (parametric.lamda ** parametric.n)) ** (1 / num)
        return TriangularGiaYo(a, b, c, lamda, rho, num)

    # addition
    def addition(self, parametric):
        num = max(self.n, parametric.n)
        lamda = ((self.lamda ** self.n) *
                 (parametric.lamda ** parametric.n)) ** (1 / num)
        rho = ((self.rho ** self.n) * (parametric.rho ** parametric.n)) ** (1 / num)
        a = self.x + parametric.x
        b = self.y + parametric.y
        c = self.z + parametric.z
        return TriangularGiaYo(a, b, c, lamda, rho, num)

    # subtraction
    def subtraction(self, parametric):
        num = max(self.n, parametric.n)
        if parametric.rho == 0:
            parametric.rho = 0.0001
        if parametric.lamda == 0:
            parametric.lamda = 0.0001

        lamda = ((self.lamda ** self.n) / (parametric.rho ** parametric.n)) ** (1 / num)
        rho = ((self.rho ** self.n) / (parametric.lamda ** parametric.n)) ** (1 / num)
        a = self.x - parametric.z
        b = self.y - parametric.y
        c = self.z - parametric.x
        return TriangularGiaYo(a, b, c, lamda, rho, num)

    def output(self):
        return f'({self.x:.2f}, {self.y:.2f}, {self.z:.2f}, {self.lamda:.2f}, {self.rho:.2f}, {self.n})'

    def trapezoidal(self):
        return TrapezoidJiMa(float(self.x), float(self.y), float(self.y), float(self.z))

    def representation(self):
        return "triangular"

    def toCartesian(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]
