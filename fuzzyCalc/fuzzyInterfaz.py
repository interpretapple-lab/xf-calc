from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as MessageBox

from fuzzyInterfazController import *

root = Tk()
root.config(bg="white")

valor = StringVar()
valor.set("")


def integrate(funct):
    x = valueX.get()
    y = valueY.get()
    xValue = Valor(x)
    yValue = Valor(y)
    opFuncion = OperandoFuncion(funct)
    if funct == "between":
        operacion = Operacion(xValue,opFuncion,yValue)
    else:
        operacion = Operacion(xValue,opFuncion)
            
    calc.operaciones.append(operacion)
    valor.set(valor.get()+operacion.__str__())
    calc.isFuncionSelected = False


def doBetween():
    integrate("between")

def around():
    integrate("around")

def most():
    integrate("most")

def atLeast():
    integrate("atLeast")

def calculate():
    confidence = modo.get()
    calc.__defineConfidence__(confidence)
    if len(calc.operaciones) == 3:
        if type(calc.operaciones[1]) == OperandorSimbolo and type(calc.operaciones[0]) == Operacion and type(calc.operaciones[2]) == Operacion :
            doCSV(calc)
        else:
            MessageBox.showinfo("Error", "Debe ingresar el operador correctamente") # título, mensaje
    else:
        MessageBox.showinfo("Error", "Debe ingresar únicamente dos operandos y un operador") # título, mensaje

def delete():
    line = ""
    if len(calc.operaciones) != 0:
        calc.operaciones.pop()
        for op in calc.operaciones:
            if type(op) != OperandorSimbolo:
                operador = op.operador
                x = op.x
                if operador == "between":
                    y = op.y
                    line += operador + "(" + str(x) + " , " + str(y) + ") "
                else:
                    line += operador + "(" + str(x) + ") "
            else:
                line += " " + op.value + " "
    valor.set(line)


def restart():
    valor.set("")
    calc.operaciones = []

def joinValue(value):
    operador = OperandorSimbolo(value)
    calc.operaciones.append(operador)
    valor.set(valor.get()+" "+operador.value+" ")

def funcionSelected(functionValue):
    calc.isFuncionSelected = True
    if functionValue == 0:
        doBetween()
    elif functionValue == 1:
        around()
    elif functionValue == 2:
        most()
    elif functionValue == 3: 
        atLeast()


frm_numerico4 = Frame(bg="white", colormap="new", width=320,height=50)
frm_numerico4.pack(side=BOTTOM)

frm_numerico3 = Frame(bg="white", colormap="new", width=320,height=50)
frm_numerico3.pack(side=BOTTOM)

frm_numerico2 = Frame(bg="white", colormap="new", width=320,height=50)
frm_numerico2.pack(side=BOTTOM)

frm_numerico1 = Frame(bg="white", colormap="new", width=320,height=50)
frm_numerico1.pack(side=BOTTOM)

frm_funciones = Frame(bg="white", colormap="new")
frm_funciones.pack(side=BOTTOM)

frm_flechas = Frame(bg="white", colormap="new")
frm_flechas.pack(side=BOTTOM)

frm_result = Frame(bg="lightblue", colormap="new", width=220,height=50)
frm_result.pack(side=BOTTOM, padx=20, pady=20)

frm_modo = Frame(bg="white", colormap="new")
frm_modo.pack(side=BOTTOM)

frm_Xvalues = Frame(master=frm_modo, bg="lightblue", colormap="new", width=50,height=25)
frm_Xvalues.pack(side=RIGHT, padx=5)

frm_Xlabel = Frame(master=frm_modo, bg="lightblue", colormap="new", width=50,height=25)
frm_Xlabel.pack(side=RIGHT, padx=5)

frm_Yvalues = Frame(master=frm_modo, bg="lightblue", colormap="new", width=50,height=25)
frm_Yvalues.pack(side=RIGHT, padx=5)

frm_Ylabel = Frame(master=frm_modo, bg="lightblue", colormap="new", width=50,height=25)
frm_Ylabel.pack(side=RIGHT, padx=5)

pantalla = Label(master=frm_result, textvariable=valor, bg="lightblue", width=50,height=5)
pantalla.pack(side=RIGHT)


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

button = Button(master=frm_flechas, text=" < ", command=lambda: left())
button.pack(side=LEFT, padx=10)
button = Button(master=frm_flechas, text=" > ", command=lambda: right())
button.pack(side=LEFT, padx=10)

button = Button(master=frm_funciones, text="between(x,y)", command=lambda: funcionSelected(0))
button.pack(side=LEFT)
button = Button(master=frm_funciones, text="around(x)", command=lambda: funcionSelected(1))
button.pack(side=LEFT)
button = Button(master=frm_funciones, text="most(x)", command=lambda: funcionSelected(2))
button.pack(side=LEFT)
button = Button(master=frm_funciones, text="atLeast(x)", command=lambda: funcionSelected(3))
button.pack(side=LEFT)

label = Label(master=frm_modo, text="Confianza: ", bg="white")
label.pack(side=LEFT, padx=10)

modo = ttk.Combobox(master=frm_modo, state="readonly",values=["Alta", "Media", "Baja"])
modo.set("Media")
modo.pack(side=LEFT, padx=10)


button = Button(master=frm_funciones, text="Record", command=lambda: calculate(), border = 10, bg='red')
button.pack(side=RIGHT, padx=10, pady=10)

button = Button(master=frm_numerico1, text="9", command=lambda: joinValue(9), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico1, text="8", command=lambda: joinValue(8), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico1, text="7", command=lambda: joinValue(7), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico1, text="DEL", command=lambda: delete(), width=5)
button.pack(side=LEFT, padx=15, pady=10)
button = Button(master=frm_numerico1, text="AC", command=lambda: restart(), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico2, text="6", command=lambda: joinValue(6), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico2, text="5", command=lambda: joinValue(5), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico2, text="4", command=lambda: joinValue(4), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico2, text="+", command=lambda: joinValue("+"), width=5)
button.pack(side=LEFT, padx=15, pady=10)
button = Button(master=frm_numerico2, text="-", command=lambda: joinValue("-"), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico3, text="3", command=lambda: joinValue(3), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico3, text="2", command=lambda: joinValue(2), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico3, text="1", command=lambda: joinValue(1), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico3, text="*", command=lambda: joinValue("*"), width=5)
button.pack(side=LEFT, padx=15, pady=10)
button = Button(master=frm_numerico3, text="/", command=lambda: joinValue("/"), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico4, text="0", command=lambda: joinValue(0), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico4, text=".", command=lambda: joinValue(), width=5)
button.pack(side=LEFT, padx=5, pady=10)
button = Button(master=frm_numerico4, text="=", command=lambda: calculate(), width=5)
button.pack(side=LEFT, padx=5, pady=10)

button = Button(master=frm_numerico4, text="=", command=lambda: calculate(), width=10)
button.pack(side=LEFT, padx=25, pady=10)

root.mainloop()