import sympy as sp
from representations.fuzzyI import *
from representations.trapezoid import *

# Standard approximation shown in:
# Giachetti & Young 1997
# https://doi.org/10.1016/S0165-0114(97)00140-1


class TriangularZadeh(FuzzyNumber):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def suma(self, triangular):
        a = self.x + triangular.x
        b = self.y + triangular.y
        c = self.z + triangular.z
        return TriangularZadeh(a, b, c)

    def resta(self, triangular):
        a = self.x - triangular.z
        b = self.y - triangular.y
        c = self.z - triangular.x
        return TriangularZadeh(a, b, c)

    def multiplicacion(self, triangular):
        a = self.x * triangular.x
        b = self.y * triangular.y
        c = self.z * triangular.z
        return TriangularZadeh(a, b, c)

    def imprimir(self):
        print(f'({self.x}, {self.y}, {self.z})')

    def trapezoidal(self):
        return TrapecioJiMa(float(self.x), float(self.y), float(self.y), float(self.z))

    def representation(self):
        return "triangle"

    def lista(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]

# Arithmetic approximations for triangular fuzzy numbers shown in:
# Giachetti & Young 1997
# https://doi.org/10.1016/S0165-0114(97)00140-1


class TriangularGiaYo(FuzzyNumber):
    alpha = sp.symbols('α')

    def __init__(self, x, y, z, lamda, rho, n):
        self.x = x
        self.y = y
        self.z = z
        self.left = (y-x)*self.alpha + x
        self.right = (y-z)*self.alpha + z
        self.lamda = lamda
        self.rho = rho
        self.n = n

# multiplicacion
    def tauLeft(self, lamda, n):
        res = 0.568 * lamda + 0.11 * n - 0.859
        return res

    def tauRight(self, rho, n):
        res = -1.85 * rho + 0.144 * n + 1.19
        return res

    def polinomialGeneralizado(self, alpha, n):
        if n == 2:
            return alpha**2 - alpha
        elif n == 3:
            return alpha**2 - alpha
        elif n == 4:
            return alpha**4 - alpha ** 3 + alpha**2 - alpha
        elif n == 5:
            return alpha**4 - alpha ** 3 + alpha**2 - alpha
        elif n == 6:
            return alpha**6 - alpha**5 + alpha**4 - alpha ** 3 + alpha**2 - alpha

    def prodLeft(self, parametrico):
        res = (self.x*parametrico.x) * \
            (((parametrico.lamda*self.lamda - 1) * self.alpha) + 1)
        return res

    def prodRight(self, parametrico):
        res = (self.z*parametrico.z) * \
            (((parametrico.rho*self.rho - 1) * self.alpha) + 1)
        return res

    def resProdLeft(self, parametrico):

        num = self.n + parametrico.n

        lamda = ((self.lamda**self.n) *
                 (parametrico.lamda**parametrico.n))**(1/num)
        polinomial = self.polinomialGeneralizado(self.alpha, num)

        prodLeft = self.prodLeft(parametrico)

        left = prodLeft + (polinomial * self.tauLeft(num, lamda)
                           * (self.y * parametrico.y - self.x * parametrico.x))

        return left

    def resProdRight(self, parametrico):
        num = self.n + parametrico.n
        polinomial = self.polinomialGeneralizado(self.alpha, num)
        rho = ((self.rho**self.n)*(parametrico.rho**parametrico.n))**(1/num)
        prodRight = self.prodRight(parametrico)
        right = prodRight + polinomial * \
            self.tauRight(num, rho) * (self.z *
                                       parametrico.z - self.y * parametrico.y)

        return right

    def multiplicacion(self, parametrico):
        left = self.resProdLeft(parametrico)
        right = self.resProdRight(parametrico)
        a = left.subs(self.alpha, 0)
        b = left.subs(self.alpha, 1)
        c = right.subs(self.alpha, 0)
        num = self.n + parametrico.n
        rho = ((self.rho**self.n)*(parametrico.rho**parametrico.n))**(1/num)
        lamda = ((self.lamda**self.n) *
                 (parametrico.lamda**parametrico.n))**(1/num)
        return TriangularGiaYo(a, b, c, lamda, rho, num)

# suma
    def suma(self, parametrico):
        num = max(self.n, parametrico.n)
        lamda = ((self.lamda**self.n) *
                 (parametrico.lamda**parametrico.n))**(1/num)
        rho = ((self.rho**self.n)*(parametrico.rho**parametrico.n))**(1/num)
        a = self.x + parametrico.x
        b = self.y + parametrico.y
        c = self.z + parametrico.z
        return TriangularGiaYo(a, b, c, lamda, rho, num)

# resta
    def resta(self, parametrico):
        num = max(self.n, parametrico.n)
        if parametrico.rho == 0:
            parametrico.rho = 0.0001
        if parametrico.lamda == 0:
            parametrico.lamda = 0.0001

        lamda = ((self.lamda**self.n)/(parametrico.rho**parametrico.n))**(1/num)
        rho = ((self.rho**self.n)/(parametrico.lamda**parametrico.n))**(1/num)
        a = self.x - parametrico.z
        b = self.y - parametrico.y
        c = self.z - parametrico.x
        return TriangularGiaYo(a, b, c, lamda, rho, num)

    def imprimir(self):
        print(f'({self.x}, {self.y}, {self.z})')

    def trapezoidal(self):
        return TrapecioJiMa(float(self.x), float(self.y), float(self.y), float(self.z))

    def representation(self):
        return "triangle"

    def lista(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]
