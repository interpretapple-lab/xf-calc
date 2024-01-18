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

    fuzzy_values = []
    operations = []
    for i in range(len(rows[:-2])):
        if i % 2 == 0:
            fuzzy = list(map(lambda x: float(x), rows[i][1:]))
            fuzzy_values.append(fuzzy)
        else:
            operations.append(rows[i])

    results = calculation(fuzzy_values, operations, conf)

    output, cartesian_values = toJson(results)

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
        val = "between" + "(" + rows[2] + "," + rows[3] + ")"
    elif rows[0] == "atMost":
        val = "atMost " + "(" + rows[3] + ")"
    else:
        val = rows[0] + "(" + rows[2] + ")"
    return val


def operation(op, val1, val2):
    if op == '+':
        res = val1.suma(val2)
    elif op == '-':
        res = val1.resta(val2)
    elif op == '*':
        res = val1.multiplicacion(val2)

    return res


def calculation(fuzzy_values, operations, conf):
    fuzzy1 = fuzzy_values[0]
    fuzzy2 = fuzzy_values[1]
    op = operations[0]
    JiMas = [TrapecioJiMa(fuzzy[0], fuzzy[1], fuzzy[2], fuzzy[3]) for fuzzy in fuzzy_values]
    JiMa = JiMas[0]
    for op, JiMa1 in zip(operations, JiMas[1:]):
        JiMa = operation(op, JiMa, JiMa1)

    # JiMa1 = TrapecioJiMa(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    # JiMa2 = TrapecioJiMa(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    # JiMa = operation(op, JiMa1, JiMa2)

    TaRes = [TrapecioTaRe(fuzzy[0], fuzzy[1], fuzzy[2], fuzzy[3]) for fuzzy in fuzzy_values]
    TaRe = TaRes[0]
    for op, TaRe1 in zip(operations, TaRes[1:]):
        TaRe = operation(op, TaRe, TaRe1)

    # TaRe1 = TrapecioTaRe(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    # TaRe2 = TrapecioTaRe(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    # TaRe = operation(op, TaRe1, TaRe2)

    SteSoGues = [TrapecioSteSoGue(fuzzy[0], fuzzy[1], fuzzy[2], fuzzy[3]) for fuzzy in fuzzy_values]
    SteSoGue = SteSoGues[0]
    for op, SteSoGue1 in zip(operations, SteSoGues[1:]):
        SteSoGue = operation(op, SteSoGue, SteSoGue1)

    # SteSoGue1 = TrapecioSteSoGue(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    # SteSoGue2 = TrapecioSteSoGue(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    # SteSoGue = operation(op, SteSoGue1, SteSoGue2)

    GrMrs = [TrapecioGrMr(fuzzy[0], fuzzy[1], fuzzy[2], fuzzy[3]) for fuzzy in fuzzy_values]
    GrMr = GrMrs[0]
    for op, GrMr1 in zip(operations, GrMrs[1:]):
        GrMr = operation(op, GrMr, GrMr1)

    # GrMr1 = TrapecioGrMr(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    # GrMr2 = TrapecioGrMr(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    # GrMr = operation(op, GrMr1, GrMr2)

    FoBes = [LRFoBe(fuzzy[0], fuzzy[1], fuzzy[2], fuzzy[3]) for fuzzy in fuzzy_values]
    FoBe = FoBes[0]
    for op, FoBe1 in zip(operations, FoBes[1:]):
        FoBe = operation(op, FoBe, FoBe1)

    # FoBe1 = LRFoBe(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    # FoBe2 = LRFoBe(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    # FoBe = operation(op, FoBe1, FoBe2)

    RoSts = [LRRoSt(fuzzy[0], fuzzy[1], fuzzy[2], fuzzy[3]) for fuzzy in fuzzy_values]
    RoSt = RoSts[0]
    for op, RoSt1 in zip(operations, RoSts[1:]):
        RoSt = operation(op, RoSt, RoSt1)

    # RoSt1 = LRRoSt(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    # RoSt2 = LRRoSt(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    # RoSt = operation(op, RoSt1, RoSt2)

    Zadehs = [TriangularZadeh(fuzzy[0], (fuzzy[1] + fuzzy[2]) / 2, fuzzy[3]) for fuzzy in fuzzy_values]
    Zadeh = Zadehs[0]
    for op, Zadeh1 in zip(operations, Zadehs[1:]):
        Zadeh = operation(op, Zadeh, Zadeh1)

    top1 = (fuzzy1[1] + fuzzy1[2]) / 2
    top2 = (fuzzy2[1] + fuzzy2[2]) / 2

    # Zadeh1 = TriangularZadeh(fuzzy1[0], top1, fuzzy1[3])
    # Zadeh2 = TriangularZadeh(fuzzy2[0], top2, fuzzy2[3])
    # Zadeh = operation(op, Zadeh1, Zadeh2)

    GiaYos = [TriangularGiaYo(limit(fuzzy[0]), limit((fuzzy[1] + fuzzy[2]) / 2), limit(fuzzy[3]),
                              limit((fuzzy[1] + fuzzy[2]) / 2) / limit(fuzzy[0]),
                              limit((fuzzy[1] + fuzzy[2]) / 2) / limit(fuzzy[3]),
                              1) for fuzzy in fuzzy_values]
    GiaYo = GiaYos[0]
    for op, GiaYo1 in zip(operations, GiaYos[1:]):
        GiaYo = operation(op, GiaYo, GiaYo1)

    # left1 = fuzzy1[0]
    # right1 = fuzzy1[3]
    # left2 = fuzzy2[0]
    # right2 = fuzzy2[3]
    # if left1 == 0:
    #     left1 = 0.0001
    # if left2 == 0:
    #     left2 = 0.0001
    # if right1 == 0:
    #     right1 = 0.0001
    # if right2 == 0:
    #     right2 = 0.0001
    # if top1 == 0:
    #     top1 = 0.0001
    # if top2 == 0:
    #     top2 == 0.0001

    # GiaYo1 = TriangularGiaYo(left1, top1, right1, top1/left1, top1/right1, 1)
    # GiaYo2 = TriangularGiaYo(left2, top2, right2, top2/left2, top2/right2, 1)
    # GiaYo = operation(op, GiaYo1, GiaYo2)

    Gausss = [Gauss((fuzzy[1] + fuzzy[2]) / 2, conf) for fuzzy in fuzzy_values]
    GaussF = Gausss[0]
    for op, Gauss1 in zip(operations, Gausss[1:]):
        GaussF = operation(op, GaussF, Gauss1)

    # Gauss1 = Gauss(top1, conf)
    # Gauss2 = Gauss(top2, conf)
    # GaussF = operation(op, Gauss1, Gauss2)

    return [JiMa, TaRe, SteSoGue, GrMr, FoBe, RoSt, Zadeh, GiaYo, GaussF]


def toJson(results):
    output = {
        "JiMa": results[0].output(),
        "TaRe": results[1].output(),
        "SteSoGue": results[2].output(),
        "GrMr": results[3].output(),
        "FoBe": results[4].output(),
        "RoSt": results[5].output(),
        "Zadeh": results[6].output(),
        "GiaYo": results[7].output(),
        "Gauss": results[8].output(),
    }

    cartesian_values = {
        "JiMa": results[0].toCartesian(),
        "TaRe": results[1].toCartesian(),
        "SteSoGue": results[2].toCartesian(),
        "GrMr": results[3].toCartesian(),
        "FoBe": results[4].toCartesian(),
        "RoSt": results[5].toCartesian(),
        "Zadeh": results[6].toCartesian(),
        "GiaYo": results[7].toCartesian(),
        "Gauss": results[8].toCartesian(),
    }
    return output, cartesian_values


def limit(value):
    if value == 0:
        return 0.0001
    else:
        return value
