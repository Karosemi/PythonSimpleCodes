import urllib.request as url
#Funkcja przelicza wartosc
def calculate(how,fromm,too):
   
    result = how*fromm/too
    return result
#Funkcja pobiera dane ze strony NBP i zamienia je na string
def load():    
    try:
        html = url.urlopen("http://www.nbp.pl/kursy/xml/LastA.xml").read()
        source = open('nowy.txt','wb').write(html)
        source = open('nowy.txt').close()
        source = open('nowy.txt').read()
    except OSError:
        source = open('nowy.txt').read()
    return source

listofw = ('THB', 'USD', 'AUD', 'HKD','CAD','NZD','SGD','EUR','HUF','CHF','GBP','UAH','JPY','CZK','DKK','ISK','NOK','SEK','HRK','RON','BGN','TRY','ILS','CLP','PHP'\
 ,'MXN','ZAR','BRL','MYR','RUB','IDR','INR','KRW','CNY','XDR')
ourStr = load()
#slownik przechowujacy w kluczu kod kursu majacy w wartosci kurs wybranej waluty
dictt={}
dictt['PLN']=1
for i in listofw:
    a=ourStr.find(i)
    numberwithcoma1 = ourStr[a+36:a+42]
    number = float(numberwithcoma1.replace(',','.'))
    dictt[i]=number
    
#Funkcja przelicza wartosc waluty
def waluta(string1,string2,howmany):
        mytuple = ('JPY','ISK','CLP','INR','KRW')
        Mystr = 'IDR'
        if string1 in mytuple:
            result = calculate(howmany,dictt[string1],dictt[string2])/100
        elif string2 in mytuple: #niektore kursy podane sa dla 100 lub 1000 jednostek wybranej waluty
            result = calculate(howmany,dictt[string1],dictt[string2])*100
        elif string1==Mystr:
            result = calculate(howmany,dictt[string1],dictt[string2])/1000
        elif string2==Mystr:
            result = calculate(howmany,dictt[string1],dictt[string2])*1000
        else:
            result = calculate(howmany,dictt[string1],dictt[string2])
        return result
    
