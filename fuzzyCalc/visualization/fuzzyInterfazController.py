import re
from .calculator import fuzzyCalculator
from .report import GenerateReport

class Calculadora:
    """General Calculator"""
    isFunctionSelected = False
    operations = []  # Lists of operations

    def __init__(self) -> None:
        self.confidence: float = 0.5  # Default confidence value
        self.confidence_str: str

    def __defineConfidence__(self, confidence: float):
        self.confidence_str = confidence
        if 0 <= confidence <= 1:
            self.confidence = float(confidence)
        else:
            raise ValueError("Confidence must be between 0 and 1")

class Operation:
    """Independent calculations"""

    def __init__(self, xValue, operator, yValue=None):
        if xValue == "":
            xValue = 0

        try:
            self.x = float(xValue.value)
            self.operator = operator.value
            if yValue is not None:
                self.y = float(yValue.value)
        except:
            self.x = float(xValue)
            self.operator = operator
            if yValue is not None:
                self.y = float(yValue)

    def __hasYValue__(self):
        return hasattr(self, 'y')

    def __isTrapecio__(self):
        if self.operator == "between":
            return 0
        elif self.operator == "around":
            return 1
        elif self.operator == "atMost":
            return 2
        elif self.operator == "atLeast":
            return 3

    def __str__(self):
        if self.__isTrapecio__() == 0:
            return f"{self.operator}({self.x} , {self.y})"
        else:
            return f"{self.operator}({self.x})"

    def __getAllValues__(self):
        if self.__isTrapecio__() == 0:  # between
            a = self.x - (self.x * calc.confidence)
            b = self.x
            c = self.y
            d = self.y * (1 + calc.confidence)
        elif self.__isTrapecio__() == 1:  # around
            a = self.x - (self.x * calc.confidence)
            b = self.x
            c = self.x
            d = self.x * (1 + calc.confidence)
        elif self.__isTrapecio__() == 2:  # atMost
            a = -10000
            b = -10000
            c = self.x
            d = self.x + (self.x * (1 + calc.confidence))
        elif self.__isTrapecio__() == 3:  # atLeast
            a = self.x - (self.x * calc.confidence)
            b = self.x
            c = 10000
            d = 10000
        return (a, b, c, d)

    def __toCsvFormat__(self):
        a, b, c, d = self.__getAllValues__()
        return (self.operator, a, b, c, d)

class Valor:
    "Values: x or y"

    def __init__(self, value):
        self.value = value

class OperationTerm:
    "Operands between, around, more, least"

    def __init__(self, value):
        self.value = value

class OperationSymbol:
    "Operands +, -, *, /"

    def __init__(self, value):
        self.value = value

def newCalc():
    calc = Calculadora()
    return calc

calc = newCalc()

def doReport(calculator):
    operationsList = calculator.operations

    rows = []
    for i in range(len(operationsList)):
        if i % 2 == 0:
            op = operationsList[i].__toCsvFormat__()
            rows.append([op[0], str(op[1]), str(op[2]), str(op[3]), str(op[4])])
        else:
            rows.append(operationsList[i].value)
    rows.append(calc.confidence_str)
    rows.append(calc.confidence)
    fuzzyCalculator(rows)
    report = GenerateReport("xf-calc/fuzzyCalc/files/data.json")
    report._generatePDF()

def notebookCalculator(inp, conf):
    inp = inp.replace("(", " ").replace(")", "").replace(", ", " ").replace(",", " ")
    inp = re.split(r"([+\-*])", inp)
    inp = list(map(lambda x: x.strip().split(" "), inp))

    for i in range(len(inp)):
        if i % 2 == 0:
            if inp[i][0] == "between":
                op = Operation(inp[i][1], inp[i][0], inp[i][2])
            else:
                op = Operation(inp[i][1], inp[i][0])
        else:
            op = OperationSymbol(inp[i][0])

        calc.operations.append(op)

    calc.__defineConfidence__(conf)
    doReport(calc)
    calc.operations = []

