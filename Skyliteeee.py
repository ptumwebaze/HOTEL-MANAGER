from tkinter import *
import tkinter.messagebox 
import sqlite3
from tkinter import ttk
import tkinter as tk
import time
import datetime
import random



def handle(frame):
    frame.tkraise()

window=Tk()
window.geometry('10000x10000')
frame1 = Frame(window,bg= 'pink',width = 10000,height= 1000)
frame2 = Frame(window,bg= 'pink',width = 10000,height= 1000)

window.title("Skylite hotel")
window.config(bg="pink")
#=======================================================================
tab_control = ttk.Notebook(window,width=1000,height=1000)
tab_control.place(x=150,y=10)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

tab_control.add(tab1, text='      Home         ')
tab_control.add(tab2, text='      About us    ')
tab_control.add(tab3, text='      Services Available         ')
tab_control.add(tab4, text='      Room Services     ')
tab_control.add(tab5, text='      Restuarant Services       ')
tab_control.add(tab6, text='      Boook Now                           ')

#===================================================================

start1=Label(tab1,text='WELCOME TO SKYLITE HOTEL!!',width="30",height=1,bg="purple",fg="red",font=("lucida calligraphy",30))
start1.place(x=100,y=30)

imagehome = PhotoImage(file="image.png")
w = imagehome.width()
h = imagehome.height()
start1 =Label(tab1,image=imagehome)
start1.place(x=100,y=100)

start2=Label(tab2,text="Welcome to SKYLITE\n HOTEL\n \nThe ultimate place for you and your loved ones, \n come relax and have fun out of home\n Contact us on:\n+256786813872 \n +256756522695\n email: skylite@gmail.com ",bg="white",fg="blue",font=("Lucida Calligraphy",20))
start2.place(x=100,y=30)

start3=Label(tab3,text='Services Available!!\n Room Services & \n Restuarant Services',bg="white",fg="red",font=("lucida calligraphy",30))
start3.place(x=100,y=30)
      
           

mainloop()
    
