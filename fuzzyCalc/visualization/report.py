from fpdf import FPDF
import matplotlib.pyplot as plt
import json
from datetime import datetime
import numpy as np
from scipy.stats import norm


class GenerateReport():
    def __init__(self, file: str):
        self.jsonFile = file
        self.jsonDict = self.__getJsonDict(file)
        self.cartesian_values = dict(self.jsonDict.get("cartesian_values"))
        self.input = dict(self.jsonDict.get("input"))

    def __saveResultsPlots(self):
        xPlots = 3
        yPlots = self.__getNumberYPlots(xPlots)
        size = 4

        fig = plt.figure(figsize=(xPlots*size, yPlots*size), dpi=100)
        fig.set_constrained_layout(True)

        index = 1
        for clave, valor in self.cartesian_values.items():
            try:
                x = list(valor)

                min, max = self.graphInfinites(x)

                if(max-min) <= 2:
                    min = 0
                    max = 5

            except:
                x = [0, 0, 0, 0]
                min = 0
                max = 5
            if clave != "Gauss":

                y = [0, 1, 1, 0]
                ax = plt.subplot(yPlots, xPlots, index)
                plt.setp(ax.spines.values(), color='gray')
                ax.plot(x, y)
                plt.scatter(x, y)
                plt.xlim(min, max)


                for xy in zip(x, y):
                    if xy[0] >= 1000 or xy[0] <= -1000:
                        plt.annotate('(%.2f)' % xy[1], xy=xy, fontsize=15)
                    else:
                        plt.annotate('(%.2f)' % xy[0], xy=xy, fontsize=15)
            if clave == "Gauss":
                ax = plt.subplot(yPlots, xPlots, index)
                x = list(valor)
                match x[1]:
                    case 1.6:
                        y = [0, 0.25, 0]
                        ax.set_yticks([0.0, 0.05, 0.1, 0.15, 0.2, 0.25])
                    case 1.0:
                        y = [0, 0.4, 0]
                        ax.set_yticks([0.0, 0.08, 0.16, 0.24, 0.32, 0.4])
                    case 0.8:
                        y = [0, 0.5, 0]
                        ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
                    case 0.5:
                        y = [0, 0.8, 0]
                        ax.set_yticks([0.0, 0.16, 0.32, 0.48, 0.64, 0.8])
                    case 0.4:
                        y = [0, 1, 0]
                        ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
                    case 0.2:
                        y = [0, 2.0, 0]
                        ax.set_yticks([0.0, 0.4, 0.8, 1.2, 1.6, 2.0])
                    case _:
                        y = [0, 1, 0]
                        ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])

                ax.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
                plt.setp(ax.spines.values(), color='gray')
                s = np.linspace(x[0] - (3*x[1]), x[0] + (3*x[1]), 100)
                ax.plot(s, norm.pdf(s, x[0], x[1]))
                x = [x[0] - (3*x[1]), x[0], x[0] + (3*x[1])]
                for xy in zip(x, y):
                    if xy[0] >= 1000 or xy[0] <= -1000:
                        plt.annotate('(∞)', xy=xy, fontsize=15)
                    if xy[0]:
                        plt.annotate('(%.2f)' % xy[0], xy=xy, fontsize=15)
            index += 1
        plt.savefig("fuzzyCalc/files/results.png")

    def __saveInputPlots(self):
        xPlots = 2
        yPlots = 1
        size = 4

        xfuzzy1 = self.input["fuzzy1"]
        min1, max1 = self.graphInfinites(xfuzzy1)

        y = [0, 1, 1, 0]

        fig = plt.figure(figsize=(xPlots*size, yPlots*size), dpi=100)
        fig.set_constrained_layout(True)

        # Graph of Input 1
        ax = plt.subplot(yPlots, xPlots, 1)
        ax.set_title(self.input["valor1"], fontsize=18)
        plt.setp(ax.spines.values(), color='green')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.plot(xfuzzy1, y)
        plt.scatter(xfuzzy1, y)
        plt.xlim(min1, max1)
        for xy in zip(xfuzzy1, y):
            plt.annotate('(%.2f)' % xy[0], xy=xy, fontsize=15)

        # Graph of Input 2
        xfuzzy2 = self.input["fuzzy2"]
        min2, max2 = self.graphInfinites(xfuzzy2)
        ax = plt.subplot(yPlots, xPlots, 2)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.setp(ax.spines.values(), color='green')
        ax.set_title(self.input["valor2"], fontsize=18)
        ax.plot(xfuzzy2, y)
        plt.scatter(xfuzzy2, y)
        plt.xlim(min2, max2)
        for xy in zip(xfuzzy2, y):
            plt.annotate('(%.2f)' % xy[0], xy=xy, fontsize=15)

        plt.savefig("fuzzyCalc/files/input.png")

    def __getNumberYPlots(self, numberXPlots: int):
        keys = self.cartesian_values.keys()
        numberPlots = len(keys)
        math = numberPlots / numberXPlots
        if (math <= 1):
            return 1
        elif (math <= 2):
            return 2
        elif (math <= 3):
            return 3
        else:
            return 4

    def __getJsonDict(self, jsonFile: str):
        with open(jsonFile) as json_file:
            data = json.load(json_file)
        return dict(data)

    def _generatePDF(self, filename="fuzzyCalc/files/report"+datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")+".pdf", dateTime=datetime.now()):
        self.__saveResultsPlots()
        self.__saveInputPlots()
        WIDTH = 210
        HEIGHT = 297

        pdf = FPDF()  # A4 (210 by 297 mm)

        ''' First Page '''
        pdf.add_page()
        self.__createTitle(pdf, "FUZZY NUMBERS - CALCULATOR RESUME", dateTime)
        pdf.image("fuzzyCalc/files/input.png", 62, 25, 90, 45)
        pdf.image("fuzzyCalc/files/results.png", 5, 78, WIDTH-8, HEIGHT-95)
        self.__addInputInfo(pdf)

        pdf.output(filename, 'F')

    def __createTitle(self, pdf: FPDF, title, dateTime: datetime):
        now = dateTime.strftime("%d/%m/%Y  %H:%M:%S")
        pdf.set_font('Arial', '', 12)
        pdf.cell(5, 4, txt=f'{now}', ln=1, align='L')
        pdf.set_font('Arial', '', 14)
        pdf.cell(5, 10, txt=f'{title}', ln=1, align='L')

    def __addInputInfo(self, pdf: FPDF):
        text = self.input["operacion"]
        pdf.set_font('Arial', '', 16)
        pdf.cell(0, 11, txt=text, ln=1, align='C')

    def graphInfinites(self, x):
        min = int(x[0]-1)
        max = int(x[3]+2)

        if (max >= 1000):
            if (min <= -1000):
                max = 5
                min = -5
            else:
                max = int(x[1]) + 5

            if (max >= 1000):
                max = int(x[2]+2)

        if(min <= -1000):
            min = int(x[2]) - 5
            if min <= -1000:
                min = int(x[1]-1)

        return min, max
