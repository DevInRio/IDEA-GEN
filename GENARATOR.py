from logging import root
from multiprocessing.connection import wait
from pydoc import text
from random import randint
from re import X
import time
import tkinter as tk
import tkinter.messagebox
from turtle import bgcolor, position, width
from typing import Text



#Reads the txt foe words to put into genaration# 
f = open("models.txt")
models = f.readlines()
q = open("styles.txt")
stlyes = q.readlines()


top = tkinter.Tk()
top.geometry("1280x720")
top['background']='#856ff8'
top.title("IDEA GEN")






def helloCallBack():
   tkinter.messagebox.showinfo("Result", models[randint (0, len(models)-1)]+", "+stlyes[randint (0, len(stlyes)-1)])

B = tkinter.Button(top, text ="Generate", command = helloCallBack, width = 30, height = 20, bg='#4974a5', fg='White', borderwidth=0).pack(pady=200)
button1 = tkinter.Button( text ="monkey", width = 30, height = 20, bg='#4974a5', fg='White',  borderwidth=0)



button1.pack(side=tk.RIGHT)


top.mainloop()




