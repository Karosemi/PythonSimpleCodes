import datetime
import re
import time
import os
import shutil

def backup(path,ext,dirpath):
    a=datetime.datetime.now()
    d="%s.%s.%s" %(a.day,a.month,a.year)
    newdir=os.path.join(dirpath, "Backup")
    if not os.path.exists(newdir):
        os.mkdir(newdir,755)
    newdir1=os.path.join(newdir,"copy-"+d)
    if not os.path.exists(newdir1):
        os.mkdir(newdir1,755)
    for dirpaths,dirs,files in os.walk(path):
        for f in files:
            match=str(f).endswith(str(ext))
            if match is True:
                timeinsec=3600*24*3
                time3dago=time.time()-timeinsec
                s=os.path.join(path,f)
                if os.path.getmtime(s)>=time3dago:
                    shutil.copy(s,newdir1)
                
                