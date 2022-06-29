from tkinter import *
import tkinter as tk
from tkinter import ttk,font
import sqlite3
from tkinter import ttk
import tkinter.messagebox

window=Tk()
window.geometry("2000x750")
window.configure(bg="powder blue")




frame1=Frame(window,bg="black",width=1280,height=700)
frame1.place(x=40,y=18)

frame2=Frame(frame1,bg="white",width=1230,height=560)
frame2.place(x=28,y=40)

frame3=Frame(frame2,bg="gray",width=1230,height=50)
frame3.place(x=0,y=100)

frame4=Frame(frame1,width=2000,height=100,bg="gray")
frame4.place(x=0,y=600)

###labels
l1=Label(frame4,text="ADDRESS\nArua district\nNear Barifa Forest",fg="white",width=30,height=6,bg="gray")
l1.place(x=0,y=0)

l1=Label(frame4,text="BUSINESS HOUR\nMonday_Friday 8:00AM-5:00PM\nSaturay 9:00Am-4:00PM\nSunday Closed",fg="white",width=30,height=4,bg="gray")
l1.place(x=400,y=0)

l1=Label(frame4,text="TELEHONE\n0788465289\n075980575857",fg="white",width=30,height=6,bg="gray")
l1.place(x=800,y=0)
#muni
image1 = PhotoImage(file="room.jfif")
w = image1.width()
h = image1.height()
panel1 =Label(frame1, image=image1)
panel1.place(x=30,y=194)


window.mainloop()
