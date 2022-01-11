# pip install pyzbar  You can find Visual C++ Redistributable Packages for Visual Studio 2013 here
# pip install pillow

# from tkinter import messagebox
import os
import sys
import csv
import sqlite3
from pathlib import Path
from PIL import Image
from pyzbar.pyzbar import decode

def getSN(imagefilepath):
    sr = []
    img = Image.open(imagefilepath,mode='r')
    sr = decode(img)
    img.close()
  
    print(imagefilepath.name)
    if len(sr) == 0:
        print('     none code')
        print('')
        return sr
    
    for v in sr:
        print("     >>code: ",v[0].decode('utf-8', 'ignore')+'   >>type:' + v.type)
    print('')
    rensn(imagefilepath,sr[0][0].decode('utf-8','ignore'))
    return sr[0][0].decode('utf-8','ignore')

def rensn(path,namestr):
    temp = path
    ps = path.parent
    pp = path.suffix
    a=0
    while True:
        a+=1
        pat = str(ps)+'\\'+ namestr+' ('+ str(a) +')' +str(pp)
        if not Path(pat).is_file():
            os.rename(str(temp),str(pat))
            addcsvfile(str(ps.name),namestr,str(pat))
            sql3(str(ps.name),namestr,str(pat))
            break

def addcsvfile(basena,barcode,folder):
    filename = 'SNList.txt'
    f = open(filename,'a+',newline='')
    cw = csv.writer(f)
    data = [str('\''+basena),str('\''+barcode),'=HYPERLINK("'+ str(Path(folder).parent) +'")']
    cw.writerow(data)
    f.close()
    pass

def sql3(basena,barcode,folder):
    dbname = 'Serial.db'
    if not Path(dbname).is_file():
        crt="CREATE TABLE IF NOT EXISTS Serial (id INTEGER PRIMARY KEY,basena TEXT,barcode TEXT,folder TEXT)"
        con = sqlite3.connect(dbname)
        con.execute(crt)
        con.commit()
        con.close()
    else:
        con = sqlite3.connect(dbname)
        intr = "insert into Serial(basena,barcode,folder)values(\"{}\",\"{}\",\"=HYPERLINK(\"\"{}\"\")\")".format(str('\''+basena),str('\''+barcode),str(Path(folder).parent))

        con.execute(intr)
        con.commit()
        con.close()

def file1(ps):
    tts =['.JPG','.PNG','.BMP','.jpg','.png','.bmp']
    if ps.suffix in tts:
        getSN(ps)
    else:
        print(ps.name)
        print('')

def dir1(ps):
    flist=ps.glob('*')
    __file__
    for f in flist:
        file1(f)

def xx():
    if Path.is_file(arpath):
        file1(arpath)
    if Path.is_dir(arpath):
        dir1(arpath)

if len(sys.argv) > 1 :
    arpath=Path(sys.argv[1])
    xx()
else:
    print('')
    print('==============================')
    print('Image File BarCode decode v1.2')
    print('powered by ZPower')
    print('Produced by ZPower')
    print('==============================')

print('.end')
input()
# messagebox.showinfo("pause","pause")
# decode(Image.open('pyzbar/tests/code128.png'))