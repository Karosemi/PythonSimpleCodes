#Zad.2
#funkcja pobiera wartosc w postaci nazwy pliku podane w postaci: "lokalizaacja pliku/nazwapliku.rozszerzenie"
#rozmiary miniatury oraz nazwe pliku wyjsciowego w postaci: "lokalizaacja pliku/nazwapliku.rozszerzenie"	
def miniature(name,height,width,newname):
    import PIL
    from PIL import Image
    im=Image.open(name)
    im.thumbnail((width,height))
    im.save(newname,"JPEG")
    
oname=input('podaj nazwe pliku: ') #nazwa naszego pliku-najlepiej podac cala sciezke
owidth=int(input('podaj szerokość miniatury: '))
oheight=int(input('podaj wysokosc miniatury: '))
onewname=input('podaj nazwe miniatury: ') #nasza now nazwa-rowniezz podejamy sciezke 
#jezeli chcemy zapisac w konsretnym miejscu. W innym wypadku program zapisze miniature w swoim folderze domyslnym
miniature(oname,oheight,owidth,onewname)
print("miniatura została zapisana")
#wyswietla apisa o pomyslnym utworzeniu miniatury
#przykladowe : D://piesel.jpg, 120,90,D://malypiesel.jpg
#moduł Miniature
