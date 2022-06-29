from tkinter import *
import tkinter as tk 
from tkinter import ttk
import sqlite3
import tkinter.messagebox
from tkinter import scrolledtext


conn=sqlite3.connect("PRMS.db")
c=conn.cursor()

def main(frame):
    frame.tkraise()

window=Tk()
window.geometry("2500x750")

frame1=Frame(window,width=2200,height=1000,bg="white")
frame1.grid(row=0,column=0,sticky="news")

frame2=Frame(frame1,width=2200,height=1000,bg="light blue")
frame2.place(x=0,y=0)

imagehome = PhotoImage(file="pic 2.png")
w = imagehome.width()
h = imagehome.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 =Label(frame1, image=imagehome)
panel1.place(x=0,y=20)
#====================================================================tab 1 start===================================

