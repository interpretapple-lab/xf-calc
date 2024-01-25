from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox

from fuzzyCalc.visualization.fuzzyInterfazController import *

root = Tk()
root.config(bg="white")

valor = StringVar()
valor.set("")


def integrate(funct):
    x = valueX.get()
    y = valueY.get()
    xValue = Valor(x)
    yValue = Valor(y)
    opFunction = OperationTerm(funct)
    if funct == "between":
        operation = Operation(xValue, opFunction, yValue)
    else:
        operation = Operation(xValue, opFunction)

    calc.operations.append(operation)
    valor.set(valor.get() + operation.__str__())
    calc.isFunctionSelected = False


def doBetween():
    integrate("between")


def around():
    integrate("around")


def most():
    integrate("atMost")


def atLeast():
    integrate("atLeast")


def calculate():
    confidence = modo.get()
    calc.__defineConfidence__(confidence)
    if len(calc.operations) == 3:
        if type(calc.operations[1]) == OperationSymbol and type(calc.operations[0]) == Operation and type(
                calc.operations[2]) == Operation:
            doReport(calc)
        else:
            MessageBox.showinfo(
                "Error", "Debe ingresar el operador correctamente")
    else:
        MessageBox.showinfo(
            "Error", "Debe ingresar únicamente dos operandos y un operador")


def delete():
    line = ""
    if len(calc.operations) != 0:
        calc.operations.pop()
        for op in calc.operations:
            if type(op) != OperationSymbol:
                operator = op.operator
                x = op.x
                if operator == "between":
                    y = op.y
                    line += operator + "(" + str(x) + " , " + str(y) + ") "
                else:
                    line += operator + "(" + str(x) + ") "
            else:
                line += " " + op.value + " "
    valor.set(line)


def restart():
    valor.set("")
    calc.operations = []


def joinValue(value):
    operator = OperationSymbol(value)
    calc.operations.append(operator)
    valor.set(valor.get() + " " + operator.value + " ")


def funcionSelected(functionValue):
    calc.isFunctionSelected = True
    if functionValue == 0:
        doBetween()
    elif functionValue == 1:
        around()
    elif functionValue == 2:
        most()
    elif functionValue == 3:
        atLeast()


frm_operaciones2 = Frame(bg="white", colormap="new", width=320, height=50)
frm_operaciones2.pack(side=BOTTOM)

frm_operaciones1 = Frame(bg="white", colormap="new", width=320, height=50)
frm_operaciones1.pack(side=BOTTOM)

frm_funciones = Frame(bg="white", colormap="new")
frm_funciones.pack(side=BOTTOM)

frm_XY = Frame(bg="white", colormap="new")
frm_XY.pack(side=BOTTOM)

frm_result = Frame(bg="lightblue", colormap="new", width=220, height=50)
frm_result.pack(side=BOTTOM, padx=20, pady=20)

frm_modo = Frame(bg="white", colormap="new")
frm_modo.pack(side=BOTTOM)

frm_Xvalues = Frame(master=frm_XY, bg="lightblue",
                    colormap="new", width=50, height=25)
frm_Xvalues.pack(side=RIGHT, padx=5)

frm_Xlabel = Frame(master=frm_XY, bg="lightblue",
                   colormap="new", width=50, height=25)
frm_Xlabel.pack(side=RIGHT, padx=5)

frm_Yvalues = Frame(master=frm_XY, bg="lightblue",
                    colormap="new", width=50, height=25)
frm_Yvalues.pack(side=RIGHT, padx=5)

frm_Ylabel = Frame(master=frm_XY, bg="lightblue",
                   colormap="new", width=50, height=25)
frm_Ylabel.pack(side=RIGHT, padx=5)

screen = Label(master=frm_result, textvariable=valor,
               bg="lightblue", width=50, height=5)
screen.pack(side=RIGHT)

valorY = StringVar()
valorY.set("Y =")
Label(master=frm_Xlabel, textvariable=valorY).pack(side=BOTTOM)

valueY = tk.Entry(master=frm_Xvalues, width=5)
valueY.insert(0, "0")
valueY.pack(side=RIGHT)

valorX = StringVar()
valorX.set("X =")
Label(master=frm_Ylabel, textvariable=valorX).pack(side=RIGHT)

valueX = tk.Entry(master=frm_Yvalues, width=5)
valueX.insert(0, "0")
valueX.pack(side=RIGHT)

button = Button(master=frm_funciones, text="Between(x,y)",
                command=lambda: funcionSelected(0))
button.pack(side=LEFT)
button = Button(master=frm_funciones, text="Around(x)",
                command=lambda: funcionSelected(1))
button.pack(side=LEFT)
button = Button(master=frm_funciones, text="atMost(x)",
                command=lambda: funcionSelected(2))
button.pack(side=LEFT)
button = Button(master=frm_funciones, text="atLeast(x)",
                command=lambda: funcionSelected(3))
button.pack(side=LEFT)

label = Label(master=frm_modo, text="Confidence: ", bg="white")
label.pack(side=LEFT, padx=10)

modo = ttk.Combobox(master=frm_modo, state="readonly",
                    values=["High", "Medium", "Low"])
modo.set("Medium")
modo.pack(side=LEFT, padx=10)

button = Button(master=frm_funciones, text="=",
                command=lambda: calculate(), border=10, bg='red')
button.pack(side=RIGHT, padx=10, pady=10)

button = Button(master=frm_operaciones1, text="+",
                command=lambda: joinValue("+"), width=5)
button.pack(side=LEFT, padx=10, pady=10)
button = Button(master=frm_operaciones1, text="-",
                command=lambda: joinValue("-"), width=5)
button.pack(side=LEFT, padx=10, pady=10)

button = Button(master=frm_operaciones1, text="*",
                command=lambda: joinValue("*"), width=5)
button.pack(side=LEFT, padx=10, pady=10)
button = Button(master=frm_operaciones1, text="",
                width=5)
button.pack(side=LEFT, padx=10, pady=10)

button = Button(master=frm_operaciones1, text="AC",
                command=lambda: restart(), width=5)
button.pack(side=LEFT, padx=10, pady=10)

button = Button(master=frm_operaciones2, text="",
                width=10)
button.pack(side=LEFT, padx=30, pady=10)

button = Button(master=frm_operaciones2, text="DEL",
                command=lambda: delete(), width=5)
button.pack(side=LEFT, padx=15, pady=10)

root.mainloop()
