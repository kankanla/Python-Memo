# PythonでWindowsの音声合成を使う
#   pywin32ライブラリのインストールが必要
#       インストール方法）pip install pywin32
# 文字列をしゃべらせる
# print(voice.Speak("だが断る"))
# 準備

import os
import win32com.client as wincl

voice = wincl.Dispatch("SAPI.SpVoice")
while True:
    os.system('ipcmd recv /msgfile=t.txt')
    f = open('t.txt','r',encoding='utf-8')
    s = f.readline()
    s = f.readline()
    s = f.readline()
    s = f.readline()

    while True:
        s=f.readline()
        if s:
            print(voice.Speak(s))
        else:
            f.close()
            break
        
os.system('pause')



