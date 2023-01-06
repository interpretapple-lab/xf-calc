from trapezoid import *
from triangle import *
from lr import *
from pdf import *

if __name__ == "__main__":
    
    trap1 = TrapecioJiMa(1, 5, 9)
    trap2 = TrapecioJiMa(2, 3, 8)
    res = trap1.multiplicacion(trap2)
    res.imprimir()

    trap1 = TrapecioTaRe(0, 2, 4, 6)
    trap2 = TrapecioTaRe(2, 3, 8)
    res = trap1.multiplicacion(trap2)
    res.imprimir()

    inter1 = TrapecioSteSoGue(1, 5, 9)
    inter2 = TrapecioSteSoGue(2, 3, 8)
    res = inter1.multiplicacion(inter2)
    #res.imprimir()
    res = res.trapezoidal()
    res.imprimir()

    lr1 = TrapecioGrMr(1, 5, 9)
    lr2 = TrapecioGrMr(2, 3, 8)
    res = lr1.multiplicacion(lr2)
    res = res.trapezoidal()
    res.imprimir()

    inter1 = TriangularSteSoGue(1, 5, 9)
    inter2 = TriangularSteSoGue(2, 3, 8)
    res = inter1.multiplicacion(inter2)
    #res.imprimir()
    res = res.trapezoidal()
    res.imprimir()

    trap1 = TriangularZadeh(1, 5, 9)
    trap2 = TriangularZadeh(2, 3, 8)
    res = trap1.multiplicacion(trap2)
    res = res.trapezoidal()
    res.imprimir()

    param = TriangularGiaYo(1, 5, 9, 5/1, 5/9, 1)
    param2 = TriangularGiaYo(2, 3, 8, 3/2, 3/8, 1)
    res = param.multiplicacion(param2)
    res = res.trapezoidal()
    res.imprimir()

    lr1 = LRFoBe(1, 5, 9)
    lr2 = LRFoBe(2, 3, 8)
    res = lr1.multiplicacion(lr2)
    res = res.trapezoidal()
    res.imprimir()

    lr1 = LRRoSt(1, 5, 9)
    lr2 = LRRoSt(2, 3, 8)
    res = lr1.multiplicacion(lr2)
    res = res.trapezoidal()
    res.imprimir()

'''
    lr1 = LRFoBe(0, 2, 4, 6)
    lr2 = LRFoBe(2, 3, 3, 8)
    res = lr1.multiplicacion(lr2)
    res.imprimir()
    res.trapezoidal().imprimir()

    lr1 = LRRoSt(0, 2, 4, 6)
    lr2 = LRRoSt(2, 3, 3, 8)
    res = lr1.multiplicacion(lr2)
    res.imprimir()
    res.trapezoidal().imprimir()
'''

'''
Fig. 1 depicts the highest preference for values “between b and c” and the lowest preference for values “below a” and values “above d”
alpha depends on the confidence level.
'''