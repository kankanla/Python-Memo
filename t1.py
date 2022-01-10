# -*- coding:utf-8 -*-

import tkinter as tk

root = tk.Tk()

# ボタンが押されたときのコールバック関数
def callback(ii):
    print("callback" + str(ii))
    pass
# ボタンを格納するリストを定義
buttons = []
for i in range(5):
    # リストにボタンを追加
    buttons.append(tk.Button(root,text=i,command=callback(i)))
    # リストのインデックスを使用して、ボタンを配置
    buttons[i].pack(fill="x")

root.mainloop()