from fpdf import FPDF
import matplotlib.pyplot as plt
import json
from matplotlib.backends.backend_pdf import PdfPages


class GenerateReport():
    def __init__(self, file:str):
        self.jsonFile = file
        self.jsonDict = self.__getJsonDict(file)
        self.output = dict(self.jsonDict.get("output"))
        self.input = dict(self.jsonDict.get("input"))


    def __saveResults(self):
        fig = plt.figure(figsize=(12, 12), dpi=100) 
        fig.tight_layout()
        index = 1
        for clave, valor in self.output.items():
            try:
                x = list(valor)
                min = int(x[0]-1)
                max = int(x[3]+2)
                
                if (max>=1000):
                    if (min <= -1000):
                        max = 5
                        min = -5
                    else:
                        max = int(x[1]) + 5
                    
                    if (max >= 1000):
                        max = int(x[0]) + 10
                
                if(min <= -1000):
                    min = int(x[2]) - 5
                    if min <= -1000:
                        min = int(x[3]) - 10

                if (max-min)<=12 and (max-min) > 2:
                    spacing = 1

                elif(max-min) <= 2:
                    min = 0
                    max = 5
                    spacing = 1
                else:
                    spacing = int((max-min)//12)
                
            except:
                x = [0,0,0,0]
                min = 0
                max = 5
                spacing = 1

            print(x)
            y = [0,1,1,0]
            ax = plt.subplot(3,3,index)
            ax.plot(x,y)
            plt.scatter(x, y)
            plt.xlim(min, max)
            plt.xticks(range(min,max,spacing))
            ax.set_title(clave,fontsize=18)
            
            for xy in zip(x, y):
                plt.annotate('(%.2f)' % xy[0], xy=xy)
            
            index +=1
        
        plt.savefig("results.png")


    def __getNumberPlots(self):
        keys =  self.output.keys()
        return len(keys)

    def __getJsonDict(self, jsonFile:str):
        with open(jsonFile) as json_file:
            data = json.load(json_file)
        return dict(data)

    def _generatePDF(self, day="12/01/2022", filename="report.pdf"):
        self.__saveResults()
        WIDTH = 210
        HEIGHT = 400
        
        pdf = FPDF() # A4 (210 by 297 mm)


        ''' First Page '''
        pdf.add_page()
        self.__createTitle(day, pdf,"FUZZY NUMBERS")
        self.__addInputInfo(pdf)
        pdf.image("results.png", 0, 50, WIDTH-5)
        

        pdf.output(filename, 'F')

    def __createTitle(self,day, pdf:FPDF,title):
        pdf.set_font('Arial', '', 12)  
        pdf.ln(2)
        pdf.write(4, f'{day}')
        pdf.ln(10)
        pdf.set_font('Arial', '', 16)
        pdf.write(5,f'{title}')


    def __addInputInfo(self,pdf:FPDF):
        text = self.input["valor1"] +" "+ self.input["operacion"] + " " +self.input["valor2"]
        pdf.set_font('Arial', '', 14)  
        pdf.ln(15)
        pdf.cell(0, 0, txt = text, ln = 1, align = 'C')
    