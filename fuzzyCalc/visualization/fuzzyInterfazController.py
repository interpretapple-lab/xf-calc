from visualization.calculator import fuzzyCalc
from visualization.report import GenerateReport


class Calculadora:
    "Calculadora General"
    isFuncionSelected = False
    operaciones = [] #Listas de operaciones

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

        self.x = float(xValue.value)
        self.operador = operador.value
        if yValue!=None:
            self.y = float(yValue.value)
        
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


def doCSV(calculator):
    lstOperaciones = calculator.operaciones
    op1 = lstOperaciones[0].__toCsvFormat__()
    operadorSimbolo = lstOperaciones[1].value
    op2 = lstOperaciones[2].__toCsvFormat__()    
    values1 = [op1[0],str(op1[1]),str(op1[2]),str(op1[3]),str(op1[4])]
    values2 = [op2[0],str(op2[1]),str(op2[2]),str(op2[3]),str(op2[4])]
    rows = [values1, operadorSimbolo, values2, calc.confidence_str, calc.confidence]
    fuzzyCalc(rows)
    report = GenerateReport("fuzzyCalc/files/data.json")
    report._generatePDF()
    