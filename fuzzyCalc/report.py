from fpdf import FPDF
import matplotlib.pyplot as plt
import json
from datetime import datetime


class GenerateReport():
    def __init__(self, file:str):
        self.jsonFile = file
        self.jsonDict = self.__getJsonDict(file)
        self.output = dict(self.jsonDict.get("output"))
        self.input = dict(self.jsonDict.get("input"))


    def __saveResultsPlots(self):
        xPlots = 3 #Recommended , number of columns  that will enter in A4 sheet
        yPlots = self.__getNumberYPlots(xPlots) # number of rows
        size = 4 #recomended size
        
        fig = plt.figure(figsize=(xPlots*size, yPlots*size), dpi=100) 
        fig.set_constrained_layout(True)
        
        index = 1
        for clave, valor in self.output.items():
            try:
                x = list(valor)                
            except:
                x = [0,0,0,0]

            y = [0,1,1,0]

            ax = plt.subplot(yPlots,xPlots,index)
            
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            plt.setp(ax.spines.values(), color='gray')
            ax.plot(x,y)

            ax.set_title(clave,fontsize=18)
            
            for xy in zip(x, y):
                plt.annotate('(%.2f)' % xy[0], xy=xy,fontsize=15)
    
            index +=1

        plt.savefig("results.png")

    def __saveInputPlots(self):
        xPlots = 2 
        yPlots = 1
        size = 4 #recomended size

        xfuzzy1 = self.input["fuzzy1"]
        xfuzzy2 = self.input["fuzzy2"]
        y = [0,1,1,0]

        fig = plt.figure(figsize=(xPlots*size, yPlots*size), dpi=100) 
        fig.set_constrained_layout(True)
        
        ax = plt.subplot(yPlots,xPlots,1)
        ax.set_title(self.input["valor1"] ,fontsize=18)
        plt.setp(ax.spines.values(), color='green')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.plot(xfuzzy1,y)

        for xy in zip(xfuzzy1, y):
            plt.annotate('(%.2f)' % xy[0], xy=xy,fontsize=15)

        ax = plt.subplot(yPlots,xPlots,2)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.setp(ax.spines.values(), color='green')
        ax.set_title(self.input["valor2"],fontsize=18)
        ax.plot(xfuzzy2,y)

        for xy in zip(xfuzzy2, y):
            plt.annotate('(%.2f)' % xy[0], xy=xy,fontsize=15)

        plt.savefig("input.png")

    def __getNumberYPlots(self ,numberXPlots:int):
        keys =  self.output.keys()
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

    def __getJsonDict(self, jsonFile:str):
        with open(jsonFile) as json_file:
            data = json.load(json_file)
        return dict(data)

    def _generatePDF(self, filename="report"+datetime.strftime(datetime.now(),"%d%m%Y_%H%M%S")+".pdf",dateTime = datetime.now()):
        self.__saveResultsPlots()
        self.__saveInputPlots()
        WIDTH = 210
        HEIGHT = 297
        
        pdf = FPDF() # A4 (210 by 297 mm)

        ''' First Page '''
        pdf.add_page()
        self.__createTitle(pdf,"FUZZY NUMBERS - CALCULATOR RESUME",dateTime)
        pdf.image("input.png", 62, 25, 90,45)
        pdf.image("results.png", 5, 78, WIDTH-8,HEIGHT-95)
        self.__addInputInfo(pdf)
        

        pdf.output(filename, 'F')

    def __createTitle(self,pdf:FPDF,title,dateTime:datetime):
        now = dateTime.strftime("%d/%m/%Y  %H:%M:%S")
        pdf.set_font('Arial', '', 12)
        pdf.cell(5, 4, txt =f'{now}', ln = 1,align = 'L')  
        pdf.set_font('Arial', '', 14)
        pdf.cell(5, 10, txt =f'{title}',ln = 1, align = 'L')  
        


    def __addInputInfo(self,pdf:FPDF):
        text = self.input["operacion"] 
        pdf.set_font('Arial', '', 16)  
        pdf.cell(0, 11, txt = text, ln = 1, align = 'C')
    