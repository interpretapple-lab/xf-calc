import re
from fuzzyCalc.visualization.calculator import fuzzyCalculator
from fuzzyCalc.visualization.report import GenerateReport

class Calculadora:
    "Calculadora General"
    isFuncionSelected = False
    operaciones = [] #Lists of operations

    def __init__(self) -> None:
        self.confidence:float
        self.confidence_str: str
    def __defineConfidence__(self, confidence):
        self.confidence_str = confidence
        if confidence == "High":
            self.confidence = 0.2
        elif confidence == "Medium":
            self.confidence = 0.5
        elif confidence == "Low":
            self.confidence = 0.8

class Operacion:
    "Calculos independientes"
    def __init__(self,xValue, operador, yValue = None):
    
        if xValue == "":
            xValue = 0

        try:
            self.x = float(xValue.value)
            self.operador = operador.value
            if yValue!=None:
                self.y = float(yValue.value)
        except:
            self.x = float(xValue)
            self.operador = operador
            if yValue!=None:
                self.y = float(yValue)
        
    def __hasYValue__(self):
        return self.y != None

    def __isTrapecio__(self):
        if self.operador == "between":
            return 0
        elif self.operador == "around":
            return 1
        elif self.operador == "atMost":
            return 2
        elif self.operador == "atLeast":
            return 3

    def __str__(self):
        if self.__isTrapecio__() == 0:
            return ""+self.operador+"("+str(self.x)+" , "+str(self.y)+")"
        else:
            return ""+self.operador+"("+str(self.x)+")"

    def __getAllValues__(self):
        if self.__isTrapecio__() == 0: #between
            a = self.x - (self.x * calc.confidence)
            b = self.x
            c = self.y
            d = self.y * (1 + calc.confidence)
        elif self.__isTrapecio__() == 1: #around
            a = self.x - (self.x * calc.confidence)
            b = self.x
            c = self.x
            d = self.x * (1 + calc.confidence)
        elif self.__isTrapecio__() == 2: #atmost
            a = -10000
            b = -10000
            c = self.x
            d = self.x + (self.x * (1+calc.confidence))
        elif self.__isTrapecio__() == 3: ##atleast
            a = self.x - (self.x * calc.confidence)
            b = self.x
            c = 10000
            d = 10000
        return (a,b,c,d)

    def __toCsvFormat__(self):
        a,b,c,d = self.__getAllValues__()
        return (self.operador,a,b,c,d)

class Valor:
    "Valor: x o y"
    def __init__(self,value):
        self.value = value 

class OperandoFuncion():
    "Operandos between, around, more, least"
    def __init__(self,value):
        self.value = value 

class OperandorSimbolo():
    "Operandos +, -, *, /"
    def __init__(self,value):
        self.value = value 


def newCalc():
    calc = Calculadora()
    return calc

calc = newCalc()


def doReport(calculator):
    lstOperaciones = calculator.operaciones

    rows = []
    for i in range(len(lstOperaciones)):
        if i%2 == 0:
            op = lstOperaciones[i].__toCsvFormat__()
            rows.append([op[0],str(op[1]),str(op[2]),str(op[3]),str(op[4])])
        else:
            rows.append(lstOperaciones[i].value)
    rows.append(calc.confidence_str)
    rows.append(calc.confidence)
    fuzzyCalculator(rows)
    report = GenerateReport("fuzzyCalc/files/data.json")
    report._generatePDF()
    

def notebookCalculator(inp, conf):
    inp = inp.replace("(", " ").replace(")", "").replace(", ", " ").replace(",", " ")
    inp = re.split("([+\-*])", inp)    
    inp = list(map(lambda x: x.strip().split(" "), inp))

    # while len(inp) >= 2:
    #     inp2= inp[:3]
    #     inp = inp[3:]
    #     print(inp2)
    #     print(inp)

    for i in range(len(inp)):
        if i%2 == 0:
            if inp[i][0] == "between":
                op = Operacion(inp[i][1], inp[i][0], inp[i][2])
            else:
                op = Operacion(inp[i][1], inp[i][0])
        else:
            op = OperandorSimbolo(inp[i][0])
        
        calc.operaciones.append(op)

    calc.__defineConfidence__(conf)
    doReport(calc)
    calc.operaciones = []