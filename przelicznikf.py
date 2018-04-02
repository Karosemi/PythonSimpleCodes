import tkinter as tk
import urllib.request as url
from tkinter import Tk, ttk, END
import sys
import waluta


#Klasa przechowujaca dane o interfejsie
class Currency_rate(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.value = ('PLN- zloty','THB- bat (Tajlandia)', 'USD- dolar amerykanski', 'AUD- dolar australijski', 'HKD- dolar Hongkongu','CAD- dolar kanadyjski','NZD- dolar nowozelandzki','SGD- dolar singapurski','EUR- euro' \
        ,'HUF- forint (Wegry)','CHF- frank szwajcarski','GBP- funt szterling','UAH- hrywna (Ukraina)','JPY- jen (Japonia)','CZK- korona czeska','DKK- korona dunska','ISK- korona islandzka','NOK- korona norweska'\
        ,'SEK- korona szwedzka','HRK- kuna (Chorwacja)','RON- lej rumunski','BGN- lew (Bulgaria)','TRY- lira turecka','ILS- nowy izraelski szekel','CLP- peso chilijskie'\
        ,'PHP- peso filipinskie','MXN- peso meksykanskie','ZAR- rand (Republika Poludniowej Afryki)','BRL- real (Brazylia)','MYR- ringgit (Malezja)','RUB- rubel rosyjski'\
        ,'IDR- rupia indonezyjska','INR- rupia indyjska','KRW- won poludniowokoreanski','CNY- yuan renminbi (Chiny)','XDR- SDR (MFW)')
        self.create_widgets()
    def create_widgets(self):
        self.group = tk.LabelFrame(self, text = "Kwota",height = 1, width = 2)
        self.group.grid(row = 0, column = 0)
        self.group.pack(padx = 100, pady = 20)
        self.val = tk.Entry(self.group)
        self.val.pack()   
        firstlistLabel = tk.Label(self, text = "Przelicz z")
        firstlistLabel.pack()
        self.firstlist=tk.ttk.Combobox(self, width = 25)
        self.firstlist['values'] = self.value
        self.firstlist.pack()        
        secondlistLabel = tk.Label(self, text = "Przelicz na")
        secondlistLabel.pack()
        self.secondlist = tk.ttk.Combobox(self, width = 25)
        self.secondlist['values'] = self.value
        self.secondlist.pack()   
        self.click_button = tk.Button(self,text = "Oblicz")
        self.click_button["command"]=self.finalcalculate
        self.click_button.pack(padx = 100, pady = 10)  
        self.listbox = tk.Listbox(self,height = 1,width = 15)
        self.listbox.pack(padx = 50, pady = 10)
        self.close_button = tk.Button(text='Zakoncz',command=sys.exit)
        self.close_button.pack(padx = 100, pady = 10)   
    def finalcalculate(self):
        self.val.focus()
        finalAm = self.val.get()
        finalAm1 = (str(finalAm)).replace(',','.')
        self.firstlist.focus()
        firstlista = self.firstlist.get()
        firstlist1 = str(firstlista)
        firstlist2 = firstlist1[:3]
        self.secondlist.focus()
        secondlista = self.secondlist.get()
        secondlist1 = str(secondlista)
        secondlist2 = secondlist1[:3]
        result = (round(100*(waluta.waluta(firstlist2,secondlist2,float(finalAm1)))))/100
        self.listbox.delete(0,END)
        self.listbox.insert(END,result)
        
       
root = tk.Tk()
tit = Currency_rate(master = root)
tit.master.title('Przelicznik walut')
root.iconbitmap("symbol_dollar.ico")
tit.mainloop()
