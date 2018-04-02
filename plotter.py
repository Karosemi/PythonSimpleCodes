import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from tkinter import *
import sys
import wykres
import numpy

class Plotter(tk.Frame):
    def __init__(self,master = None):
        self.master=master
        super().__init__(master)
        self.pack()
        self.a=0
        self.canvas()
        self.create_widgets()
        self.create_symbolButtons()
        self.create_functionButtons()         
              
    def create_widgets(self):
        self.group = LabelFrame(self, text = "Funkcja")
        self.group.grid(row=0,column=6,columnspan=7, rowspan=1)
        self.val = Entry(self.group)
        self.val.grid(row=0,column=0)
        self.grid_columnconfigure(1, weight=1)
        self.rangx = LabelFrame(self, text = "Dziedzina")
        self.rangx.grid(row=2,column=3,columnspan=7)
        self.valuexx = Entry(self.rangx)
        self.valuexx.grid(row=2,column=0)
        self.rangy = LabelFrame(self, text = "Zakres")
        self.rangy.grid(row=2,column=10,columnspan=7)
        self.valueyy = Entry(self.rangy)
        self.valueyy.grid(row=2,column=1,columnspan=7)        
        self.labelx = LabelFrame(self, text = "Etykieta osi 0X")
        self.labelx.grid(row=3,column=3,columnspan=7)
        self.valuex = Entry(self.labelx)
        self.valuex.grid() 
        self.labely = LabelFrame(self, text = "Etykieta osi 0Y")
        self.labely.grid(row=3,column=10,columnspan=7)
        self.valuey = Entry(self.labely)
        self.valuey.grid()
        self.title = LabelFrame(self, text = "Tytuł",height = 1, width = 2)
        self.title.grid(row=4,column=3,columnspan=7)
        self.titl = Entry(self.title)
        self.titl.grid()        
        self.Draw_button = Button(self,text = "Rysuj")
        self.Draw_button["command"]=self.plot 
        self.Draw_button.grid(row=5,column=9,pady=10,columnspan=3)
        self.legend = Checkbutton(self,text="Legenda",command=self.legend)
        self.legend.grid(row=4, column=10, columnspan=4)
        self.exit = Button(self,text="Zakoncz",command=sys.exit)
        self.exit.place()        
    def canvas(self):
        self.canvas = Canvas(self.master, width=500, height=400)
        self.canvas.pack(side=RIGHT)
        self.filename = PhotoImage(file = "clear.png")
        imag = self.canvas.create_image(20,0, anchor=NW, image=self.filename)  
    def plot(self):
        self.val.focus()
        self.function = self.val.get()
        self.function = str(self.function).replace('^','**')
        self.function = self.function.replace('tg','tan')
        self.function = self.function.replace('ln','log') 
        self.function = self.function.replace('ctan','1/tan')
        self.fun = self.function.split(';')
        self.valuexx.focus()
        self.ran = self.valuexx.get()
        self.ran = self.ran.replace('pi',str(numpy.pi))
        self.ran = self.ran.replace('e',str(numpy.e))
        self.ran = self.ran.split(';')
        
        self.valueyy.focus()
        self.rany = self.valueyy.get()
        self.rany = self.rany.replace('pi',str(numpy.pi))
        self.rany = self.rany.replace('e',str(numpy.e))
        self.rany = self.rany.replace(',','.')
        self.rany = self.rany.split(';')      
        self.finRange = [eval(self.ran[0]),eval(self.ran[1])]
        self.finRangey = [eval(self.rany[0]),eval(self.rany[1])]
        self.valuex.focus()
        self.valuey.focus()
        X = self.valuex.get()
        Y= self.valuey.get()
        self.titl.focus()
        Title = self.titl.get()
        wykres.Draw_plot(self.fun,self.finRange,self.finRangey,self.a,X,Y,Title)
        self.a=0
        self.canvas.delete("all")
        self.filename = PhotoImage(file = "filename.png")
        imag = self.canvas.create_image(20,0, anchor=NW, image=self.filename)    
    def legend(self):
        self.a=1
    def create_symbolButtons(self):
        self.Plus_button = Button(self,text = '+',command=self.Plus_command) 
        self.Plus_button.grid(row=1,column=0)
        self.Minus_button = Button(self,text = "-",command=self.Minus_command)
        self.Minus_button.grid(row=1,column=1)
        self.Product_button = Button(self,text = "·",command=self.Product_command)
        self.Product_button.grid(row=1,column=2) 
        self.Divisor_button = Button(self,text = "/",command=self.Divisor_command)
        self.Divisor_button.grid(row=1,column=3) 
        self.Lbracket_button = Button(self,text = "(",command=self.Lbracket_command)
        self.Lbracket_button.grid(row=1,column=4)     
        self.Rbracket_button = Button(self,text = ")",command=self.Rbracket_command)
        self.Rbracket_button.grid(row=1,column=5)  
        self.Sqrt_button = Button(self,text = "√",command=self.Sqrt_command)
        self.Sqrt_button.grid(row=1,column=6)  
        self.Coma_button = Button(self,text = ",",command=self.Coma_command)
        self.Coma_button.grid(row=1,column=7)
        self.Pi_button = Button(self,text = "π",command=self.Pi_command)
        self.Pi_button.grid(row=1,column=8)       
        self.Exp_button = Button(self,text = "e",command=self.Exp_command)
        self.Exp_button.grid(row=1,column=9)   
    def create_functionButtons(self):
        self.Sinus_button = Button(self,text = 'sin(x)',command=self.Sinus_command) 
        self.Sinus_button.grid(row=1,column=10)
        self.cosSinus_button = Button(self,text = 'cos(x)',command=self.cosSinus_command) 
        self.cosSinus_button.grid(row=1,column=11)      
        self.Tangens_button = Button(self,text = 'tg(x)',command=self.Tangens_command) 
        self.Tangens_button.grid(row=1,column=12)  
        self.cotTangens_button = Button(self,text = 'ctg(x)',command=self.cotTangens_command) 
        self.cotTangens_button.grid(row=1,column=13)
        self.Exponens_button = Button(self,text = 'e^x',command=self.Exponens_command) 
        self.Exponens_button.grid(row=1,column=14)
        self.LOG_button = Button(self,text = 'ln(x)',command=self.LOG_command) 
        self.LOG_button.grid(row=1,column=15)      
    def Plus_command(self):
        self.val.insert(END,'+')
    def Minus_command(self):
        self.val.insert(END,'-')
    def Product_command(self):
        self.val.insert(END,'*')
    def Divisor_command(self):
        self.val.insert(END,'/')
    def Lbracket_command(self):
        self.val.insert(END,'(')
    def Rbracket_command(self):
        self.val.insert(END,')')
    def Sqrt_command(self):
        self.val.insert(END,'sqrt()')
    def Coma_command(self):
        self.val.insert(END,',')
    def Pi_command(self):
        self.val.insert(END,'pi')
    def Exp_command(self):
        self.val.insert(END,'e')
    def Sinus_command(self):
        self.val.insert(END,'sin(x)')
    def cosSinus_command(self):
        self.val.insert(END,'cos(x)')   
    def Tangens_command(self):
        self.val.insert(END,'tg(x)')   
    def cotTangens_command(self):
        self.val.insert(END,'ctg(x)')   
    def Exponens_command(self):
        self.val.insert(END,'e^x')   
    def LOG_command(self):
        self.val.insert(END,'ln(x)')   
        
        
        
root = Tk()       
        
tit = Plotter(master = root)        


tit.mainloop()
