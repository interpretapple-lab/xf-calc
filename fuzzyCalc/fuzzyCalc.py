import csv
import json
from trapezoid import *
from triangle import *
from lr import *

def fuzzyCalc():
    csvFile = open('fuzzyValues.csv', 'r')
    csvReader = csv.reader(csvFile)
    rows = list(csvReader)

    val1 = values(rows[0])
    val2 = values(rows[2])

    fuzzy1 = list(map(lambda x : float(x), rows[0][1:]))
    fuzzy2 = list(map(lambda x : float(x), rows[2][1:]))
    input = {
        "operacion":rows[1][0],
        "valor1":val1,
        "valor2":val2
    }

    JiMa1 = TrapecioJiMa(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    JiMa2 = TrapecioJiMa(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    JiMa = operation(rows[1][0], JiMa1, JiMa2)

    TaRe1 = TrapecioTaRe(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    TaRe2 = TrapecioTaRe(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    TaRe = operation(rows[1][0], TaRe1, TaRe2)
    
    SteSoGue1 = TrapecioSteSoGue(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    SteSoGue2 = TrapecioSteSoGue(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    SteSoGue = operation(rows[1][0], SteSoGue1, SteSoGue2)

    GrMr1 = TrapecioGrMr(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    GrMr2 = TrapecioGrMr(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    GrMr = operation(rows[1][0], GrMr1, GrMr2)

    FoBe1 = LRFoBe(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    FoBe2 = LRFoBe(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    FoBe = operation(rows[1][0], FoBe1, FoBe2)

    RoSt1 = LRRoSt(fuzzy1[0], fuzzy1[1], fuzzy1[2], fuzzy1[3])
    RoSt2 = LRRoSt(fuzzy2[0], fuzzy2[1], fuzzy2[2], fuzzy2[3])
    RoSt = operation(rows[1][0],RoSt1, RoSt2)


    top1 = (fuzzy1[1] + fuzzy1[2])/2
    top2 = (fuzzy2[1] + fuzzy2[2])/2

    Zadeh1 = TriangularZadeh(fuzzy1[0], top1, fuzzy1[3])
    Zadeh2 = TriangularZadeh(fuzzy2[0], top2, fuzzy2[3])
    Zadeh = operation(rows[1][0], Zadeh1, Zadeh2)


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
    GiaYo = operation(rows[1][0], GiaYo1, GiaYo2)
    output = {
        "JiMa":JiMa.lista(),
        "TaRe":TaRe.lista(),
        "SteSoGue":SteSoGue.lista(),
        "GrMr":GrMr.lista(),
        "FoBe":FoBe.lista(),
        "RoSt":RoSt.lista(),
        "Zadeh":Zadeh.lista(),
        "GiaYo":GiaYo.lista()
    }

    jsonData = {
        "input": input,
        "output": output
    }

    jsonObject = json.dumps(jsonData, indent=4)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonObject)
    jsonFile.close()
    csvFile.close()

def values(rows):
    if rows[0] == "between":
        val = "between"+"("+rows[2]+","+rows[3]+")"
    elif rows[0] == "most":
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