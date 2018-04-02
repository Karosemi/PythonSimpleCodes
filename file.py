import os
#funkcja "pakuje" w jeden plik kilka plikow tekstowych z wybranego katalogu
def harchi(path,dirfile):
    mylist=[]
    mylist1=[]
    for dirpaths, dirs,files in os.walk(path):
        for f in files:
            fn=os.path.join(dirpaths, f)
            mylist1.append(f)
            mylist.append(fn)
    return mylist,mylist1
def archive_file(path,dirfile):
    mylist=harchi(path,dirfile)[0]
    mylist1=harchi(path,dirfile)[1]
    for i in range(len(mylist)):
        plik=open(dirfile+'.txt','a').write("\n"+ "File_"+str(i)+"\n"+mylist1[i]+"\n")
        plik=open(dirfile+'.txt','a').write(open(mylist[i]).read())