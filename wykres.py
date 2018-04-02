#Skrypt rysujacy wykres
from matplotlib import *
from pylab import *
import numpy


def Draw_plot(function, rang, rangy, a=0,xlab='',ylab='',titl=''):
    start = rang[0]
    end = rang[1]
    starty = rangy[0]
    endy = rangy[1]    
    x=linspace(start,end,100)
    fig, ax = plt.subplots(figsize=(5,4))
    for i in function:
        i=i.replace('ctg','1/tan')
        i = i.replace('sqrt()','**(1/2)')
        c = i.replace('**','^')
        fin = "$"+c+"$"
        t=str(i)
        y=eval(i)
        ax.plot(x, y, label=fin)
        
        ax.grid(True)
     
    ax.plot([0,0],[starty, endy],'k')
    ax.plot([start,end],[0,0],'k')

    if len(function)>1 or a==1:
            ax.legend(loc=2,fontsize = 10)
    xlabel(xlab,fontsize=7)
    ylabel(ylab,fontsize=7)
    title(titl,fontsize=14)
    ax.axis('tight') 
    ylim([starty, endy])   
    
            
    
    #show()
    fig.savefig("filename.png")
    

    
#Draw_plot(['sin(x)/cos(x)','sqrt(x)','ctan(x)'],[-4,4],[-4,4],xlab='g')
