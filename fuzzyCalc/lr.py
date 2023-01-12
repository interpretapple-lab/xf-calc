import sympy as sp
from fuzzyI import *
from trapezoid import *

#L-R Fuzzy number representation for trapezoidal fuzzy numbers
# Fodor & Bede, 2006
#Proceedings of the 4th Slovakian-Hungarian Joint Symposium on Applied Machine Intelligence (pp. 54-68)
class LRFoBe(FuzzyNumber):
    alpha = sp.symbols('α')
    def __init__(self, *args):
        if len(args)==3:
            a = args[0]
            b = args[1]
            c = args[1]
            d = args[2]
        elif len(args)==4:
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

    def suma(self, lr):
        m = self.m + lr.m
        a = m - self.left(lr, 0)
        b = m - self.left(lr, 1)
        c = m + self.right(lr, 1)
        d= m + self.right(lr, 0)
        return LRFoBe(a, b, c, d)

    def resta(self, lr):
        m = self.m - lr.m
        a = m - self.left(lr, 0)
        b = m - self.left(lr, 1)
        c = m + self.right(lr, 1)
        d= m + self.right(lr, 0)
        return LRFoBe(a, b, c, d)

    def multiplicacion(self, lr):
        m = self.m * lr.m
        a = m - self.left(lr, 0)
        b = m - self.left(lr, 1)
        c = m + self.right(lr, 1)
        d= m + self.right(lr, 0)
        return LRFoBe(a, b, c, d)

    def imprimir(self):
        left = self.m - self.l + self.alpha*(self.l - self.u)
        right = self.m + self.r + self.alpha*(self.u - self.r)
        print("[", left, ",", right, "]")
    
    def trapezoidal(self):
        left = self.m - self.l + self.alpha*(self.l - self.u)
        right = self.m + self.r + self.alpha*(self.u - self.r)
        a = left.subs(self.alpha, 0)
        b = left.subs(self.alpha, 1)
        c = right.subs(self.alpha, 1)
        d = right.subs(self.alpha, 0)
        return TrapecioJiMa(float(a), float(b), float(c), float(d))

    def lista(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]

#Simplificacion de Ma et al
# Robinson & Steele, 2002 mostrado en Fodor & Bede, 2006
#Proceedings of the 4th Slovakian-Hungarian Joint Symposium on Applied Machine Intelligence (pp. 54-68)
class LRRoSt(FuzzyNumber):
    alpha = sp.symbols('α')
    def __init__(self, *args):
        if len(args)==3:
            a = args[0]
            b = args[1]
            c = args[1]
            d = args[2]
        elif len(args)==4:
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

    def suma(self, lr):
        m = self.m + lr.m
        left = self.left(lr)
        right = self.right(lr)
        upper = self.upper(lr)
        res = LRRoSt(0,0,0,0)
        res.m = m
        res.l = left
        res.r = right
        res.u = upper
        return res

    def resta(self, lr):
        m = self.m - lr.m
        left = self.left(lr)
        right = self.right(lr)
        upper = self.upper(lr)
        res = LRRoSt(0,0,0,0)
        res.m = m
        res.l = left
        res.r = right
        res.u = upper
        return res

    def multiplicacion(self, lr):
        m = self.m * lr.m
        left = self.left(lr)
        right = self.right(lr)
        upper = self.upper(lr)
        res = LRRoSt(0,0,0,0)
        res.m = m
        res.l = left
        res.r = right
        res.u = upper
        return res

    def imprimir(self):
        left = self.m - self.l + self.alpha*(self.l - self.u)
        right = self.m + self.r + self.alpha*(self.u - self.r)
        print(left, ",", right)

    def trapezoidal(self):
        left = self.m - self.l + self.alpha*(self.l - self.u)
        right = self.m + self.r + self.alpha*(self.u - self.r)
        a = left.subs(self.alpha, 0)
        b = right.subs(self.alpha, 1)
        c = left.subs(self.alpha, 1)
        d = right.subs(self.alpha, 0)
        return TrapecioJiMa(float(a), float(b), float(c), float(d))

    def lista(self):
        trap = self.trapezoidal()
        return [trap.a, trap.b, trap.c, trap.d]