import json

from fuzzyCalc.representations.gaussian import *
from fuzzyCalc.representations.lr import *
from fuzzyCalc.representations.trapezoid import *
from fuzzyCalc.representations.triangle import *


def fuzzyCalculator(rows):
    val1 = values(rows[0])
    val2 = values(rows[2])
    conf = rows[-1]
    fuzzy1 = list(map(lambda x: float(x), rows[0][1:]))
    fuzzy2 = list(map(lambda x: float(x), rows[2][1:]))
    inp = {
        "confidence": rows[-2],
        "operacion": rows[1][0],
        "valor1": val1,
        "fuzzy1": fuzzy1,
        "valor2": val2,
        "fuzzy2": fuzzy2
    }

    output, cartesian_values = calculation(fuzzy1, fuzzy2, rows[1], conf)

    jsonData = {
        "input": inp,
        "output": output,
        "cartesian_values": cartesian_values
    }

    jsonObject = json.dumps(jsonData, indent=4)
    jsonFile = open("fuzzyCalc/files/data.json", "w")
    jsonFile.write(jsonObject)
    jsonFile.close()


def values(rows):
    if rows[0] == "between":
        val = "between"+"("+rows[2]+","+rows[3]+")"
    elif rows[0] == "atMost":
        val = "atMost "+"("+rows[3]+")"
    else:
        val = rows[0]+"("+rows[2]+")"
    return val


def operation(op, val1, val2):
    if op == '+':
        res = val1.suma(val2)
    elif op == '-':
        res = val1.resta(val2)
    elif op == '*':
        res = val1.multiplicacion(val2)

    return res


def calculation(fuzzy1, fuzzy2, op, conf):
    JiMa1 = TrapecioJiMa(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    JiMa2 = TrapecioJiMa(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    JiMa = operation(op, JiMa1, JiMa2)

    TaRe1 = TrapecioTaRe(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    TaRe2 = TrapecioTaRe(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    TaRe = operation(op, TaRe1, TaRe2)

    SteSoGue1 = TrapecioSteSoGue(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    SteSoGue2 = TrapecioSteSoGue(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    SteSoGue = operation(op, SteSoGue1, SteSoGue2)

    GrMr1 = TrapecioGrMr(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    GrMr2 = TrapecioGrMr(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    GrMr = operation(op, GrMr1, GrMr2)

    FoBe1 = LRFoBe(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    FoBe2 = LRFoBe(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    FoBe = operation(op, FoBe1, FoBe2)

    RoSt1 = LRRoSt(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    RoSt2 = LRRoSt(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    RoSt = operation(op, RoSt1, RoSt2)

    top1 = (fuzzy1[1] + fuzzy1[2])/2
    top2 = (fuzzy2[1] + fuzzy2[2])/2

    Zadeh1 = TriangularZadeh(fuzzy1[0], top1, fuzzy1[3])
    Zadeh2 = TriangularZadeh(fuzzy2[0], top2, fuzzy2[3])
    Zadeh = operation(op, Zadeh1, Zadeh2)

    left1 = fuzzy1[0]
    right1 = fuzzy1[3]
    left2 = fuzzy2[0]
    right2 = fuzzy2[3]
    if left1 == 0:
        left1 = 0.0001
    if left2 == 0:
        left2 = 0.0001
    if right1 == 0:
        right1 = 0.0001
    if right2 == 0:
        right2 = 0.0001
    if top1 == 0:
        top1 = 0.0001
    if top2 == 0:
        top2 == 0.0001

    GiaYo1 = TriangularGiaYo(left1, top1, right1, top1/left1, top1/right1, 1)
    GiaYo2 = TriangularGiaYo(left2, top2, right2, top2/left2, top2/right2, 1)
    GiaYo = operation(op, GiaYo1, GiaYo2)

    Gauss1 = Gauss(top1, conf)
    Gauss2 = Gauss(top2, conf)
    GaussF = operation(op, Gauss1, Gauss2)

    output = {
        "JiMa": JiMa.output(),
        "TaRe": TaRe.output(),
        "SteSoGue": SteSoGue.output(),
        "GrMr": GrMr.output(),
        "FoBe": FoBe.output(),
        "RoSt": RoSt.output(),
        "Zadeh": Zadeh.output(),
        "GiaYo": GiaYo.output(),
        "Gauss": GaussF.output(),
    }

    cartesian_values = {
        "JiMa": JiMa.toCartesian(),
        "TaRe": TaRe.toCartesian(),
        "SteSoGue": SteSoGue.toCartesian(),
        "GrMr": GrMr.toCartesian(),
        "FoBe": FoBe.toCartesian(),
        "RoSt": RoSt.toCartesian(),
        "Zadeh": Zadeh.toCartesian(),
        "GiaYo": GiaYo.toCartesian(),
        "Gauss": GaussF.toCartesian(),
    }
    return output, cartesian_values
