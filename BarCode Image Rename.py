# pip install pyzbar
# pip install pillow

# from tkinter import messagebox
import os
import sys
from pathlib import Path
from PIL import Image
from pyzbar.pyzbar import decode

def getSN(imagefilepath):
    sr = []
    img = Image.open(imagefilepath)
    sr = decode(img)
  
    if len(sr) == 0:
        return sr
    
    for v in sr:
        print("files ",v[0].decode('utf-8', 'ignore'))

    rensn(imagefilepath,sr[0][0].decode('utf-8','ignore'))
    return sr[0][0].decode('utf-8','ignore')

def rensn(path,namestr):
    temp = path
    ps = path.parent
    pp = path.suffix
    a=0
    while True:
        a+=1
        pat = str(ps)+'\\'+ namestr+'('+ str(a) +')' +str(pp)
        if not Path(pat).is_file():
            os.rename(str(temp),str(pat))
            break

def file1(ps):
    tts =['.jpg','.png','.bmp']
    if ps.suffix in tts:
        getSN(ps)
    else:
        print("non-image files")

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

input()
# messagebox.showinfo("pause","pause")
# decode(Image.open('pyzbar/tests/code128.png'))