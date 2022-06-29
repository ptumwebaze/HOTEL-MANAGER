from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys
import tkinter as tk
import os
import sqlite3
from tkinter import Tk, Frame, Menu
#acc=0  
window = Tk()
#window.geometry("800x900")
#window.title("BABY COACH ")

#window.config(bg="purple")

#=========================================================================================================
tab_control = ttk.Notebook(window,width='1000',height='2000')
tab_control.place(x=90,y=10)
#tab_control.config(bg="purple")
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

line1=tab_control.add(tab1, text='HOME                                          ')
line1=Frame(tab1,bg='light blue', width=2050, height=1000) 
line1.place(x=1, y=10)
line2=tab_control.add(tab2, text='TIME AND DESTINATION                          ')
line2=Frame(tab2,bg='light blue', width=2050, height=1000) 
line2.place(x=1, y=10)
line3=tab_control.add(tab3, text='BOOKING                                       ')
line3=Frame(tab3,bg='light blue', width=2050, height=1000) 
line3.place(x=1, y=10)
line4=tab_control.add(tab4, text='SELECT A SEAT                                 ')
line4=Frame(tab4,bg='light blue', width=2050, height=1000) 
line4.place(x=1, y=10)
line5=tab_control.add(tab5, text='PAYMENT                                       ')
line5=Frame(tab5,bg='light blue', width=2050, height=1000) 
line5.place(x=1, y=10)
line6=tab_control.add(tab6, text='OTHER SERVICES                                ')
line6=Frame(tab6,bg='light blue', width=2050, height=1000) 
line6.place(x=1, y=10)
#====================================================================tab 1 start===================================
image2home = PhotoImage(file="C:\\Users\\KEITH NAMU\\Desktop\\kato\\22 - Copy.png")
w = image2home.width()
h = image2home.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 =Label(tab1, image=image2home)
panel1.place(x=120,y=110)

panel1.image = image2home
#====================================================================tab 1 start===================================
start1=Tk()
start1=Label(tab1,text='BABY COACH LIMITED',width="18",height=1,bg="light blue",fg="red",font=("BERLIN SANS FB DEMI ",20))
start1.place(x=420,y=12)
Ftab1=Label(tab1,text='Your Journey Begins Here',width = '30', height = 2, bg = 'light blue', fg ='red',font="algerian 16 underline bold")
Ftab1.place(x=5, y=40)

Btab1=Label(tab1,text='GENERAL LINE:',width = '15', height = 1, bg='light BLUE', fg ='red',font=("BERLIN SANS FB DEMI ",17))
Btab1.place(x=600, y=70)
Btab2=Label(tab1,text='0786399796/0756031094',width = '20', height = 1, bg='light BLUE',fg='black',font=("BERLIN SANS FB DEMI",17))
Btab2.place(x=600, y=110)
Btab4=Label(tab1,text='PARCEL/CARGO:',width = '15', height = 1,bg='light BLUE', fg='red',font=("Calibri light",17))
Btab4.place(x=600, y=150)
Btab5=Label(tab1,text='0788173609/0703260470',width = '20', height = 1,bg='light BLUE', fg='BLACK',font=("BERLIN SANS FB DEMI",17))
Btab5.place(x=600, y=180)
#CARGO
Xtab1=Label(tab1,text='Terms & Conditions For Cargo:',width = '30', height = 1, bg='light BLUE', fg ='red',font=("algerian",15))
Xtab1.place(x=20, y=440)
Xtab2=Label(tab1,text='1.We do not carry unpaid cargo',width = '26', height = 1, bg='light BLUE',fg='BLACK',font=("Calibri light",13))
Xtab2.place(x=20, y=470)
Xtab3=Label(tab1,text='2.Goods overdue by 2 days will\n  be finned.1000\= per day',width = '27',bg='light BLUE', height = 2, fg='BLACK',font=("Calibri light",13))
Xtab3.place(x=17, y=495)
Xtab4=Label(tab1,text='3.We are not responsible for any damages\n to the package during transit',width = '35',bg='light BLUE', height = 2, fg='black',font=("Calibri light",13))
Xtab4.place(x=20, y=550)
#CARGO
Etab4=Label(tab1, text='EMAIL ADDRESS:',width='15', height=1, bg='light BLUE', fg='red', font=('BERLIN SANS FB DEMI ',17))
Etab4.place(x=20, y=290)
Etab6=Label(tab1,text='babycoachbuses@gmail.com',width = '25', height = 1,bg='light BLUE', fg='BLACK',font=("Calibri light",17))
Etab6.place(x=15, y=320)
Ctab1=Label(tab1, text='CUSTOMER CARE CENTRE:',width='23', height=1, bg='light blue', fg='red', font=('BERLIN SANS FB DEMI',17))
Ctab1.place(x=600, y=215)
Ctab2=Label(tab1,text='0777421959/0752215307',width = '20', height = 1,bg='light BLUE', fg='BLACK',font=("BERLIN SANS FB DEMI",17))
Ctab2.place(x=600, y=245)
#LOCATION
Ltab1=Label(tab1, text='LOCATION',width='15', height=1, bg='light BLUE', fg='red', font=('BERLIN SANS FB DEMI',17))
Ltab1.place(x=20, y=365)
Ltab2=Label(tab1, text='We are located in Arua town opposite Kato hardware.',width=45, height=1,bg='light BLUE', fg='BLACK',font=("Calibri light",14))
Ltab2.place(x=20, y=395)
#ft

#========================================button======================================================================
Ytab1=Label(tab1,text='Terms & Conditions for Booking:',width = '30', height = 1, bg='light BLUE', fg ='red',font=("algerian",15))
Ytab1.place(x=580, y=440)
Ytab2=Label(tab1,text='1.Call the booking office to cancel or postpone\n the ticket 1 hour before departure time',width = '38',bg='light blue' ,height = 2,fg='BLACK',font=("Calibri light",13))
Ytab2.place(x=580, y=470)
Ytab3=Label(tab1,text='2.Missing a bus and ticket cancelation \n charge is UGX10,000/=',width = '35', height = 2,bg='light blue', fg='BLACK',font=("Calibri light",13))
Ytab3.place(x=565, y=515)
Ytab4=Label(tab1,text='3.Goods carried in the bus are at\n owner\'s risk',width = '35', height = 2,bg='light blue', fg='black',font=("Calibri light",13))
Ytab4.place(x=550, y=560)

#========================================button======================================================================
start1=Label(tab2,text="DESTINATION AND TIME",width="23",height=1,bg="light blue",fg="red",font=("sylfaen",20))
start1.place(x=340,y=15)
#Frame4 = Frame(tab2,  width=1020, height=70)
#Frame4.place(x=1, y=605)
#tab2
Ftab2=Label(tab2,text='PASSENGERS ARRIVAL TIME',width = '25', height = 1, bg = 'light blue', fg = 'red', font=('BERLIN SANS FB DEMI',15))
Ftab2.place(x=360, y=100)
Ftab3=Label(tab2,text='Passengers should arrive at the bus station ready to board, 30 minutes before departure time',width=70,height=1,bg='light blue',fg='black',font=('Calibri(Body)',10))
Ftab3.place(x=230, y=150)
Ftab4=Label(tab2, text='BUS DEPARTURE TIME',width='24', height=1, bg='light blue', fg='red', font=('BERLIN SANS FB DEMI',15))
Ftab4.place(x=360, y=200)
#Ftab5=Label(tab2, width='150', height=15,bg='white')
#Ftab5.place(x=5, y=250)
Ftab6=Label(tab2, text='BUS',width='10', height='1', bg='light blue', fg='red', font=('BERLIN SANS FB DEMI ',17))
Ftab6.place(x=140, y=250)
Ftab7=Label(tab2, text='ROUTE',width='10', height='1', bg='light blue', fg='red', font=('BERLIN SANS FB DEMI',17))
Ftab7.place(x=400, y=250)
Ftab8=Label(tab2, text='TIME',width='10', height='1', bg='light blue', fg='red', font=('BERLIN SANS FB DEMI',17))
Ftab8.place(x=640, y=250)
Ftab9=Label(tab2, text='BOARDING PLACE',width='20', height='1', bg='light blue', fg='red', font=('BERLIN SANS FB DEMI',17))
Ftab9.place(x=885, y=250)
#tableinputs
Ftab9=Label(tab2, text='BABY1',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab9.place(x=150, y=300)
Ftab10=Label(tab2, text='BABY2',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab10.place(x=150, y=350)
Ftab11=Label(tab2, text='BABY3',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab11.place(x=150, y=400)
Ftab12=Label(tab2, text='BABY4',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab12.place(x=150, y=450)
Ftab13=Label(tab2, text='ARUA-KLA',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab13.place(x=420, y=300)
Ftab14=Label(tab2, text='ARUA-KLA',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab14.place(x=420, y=350)
Ftab15=Label(tab2, text='ARUA-KLA',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab15.place(x=420, y=400)
Ftab16=Label(tab2, text='ARUA-KLA',width='10', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab16.place(x=420, y=450)
Ftab17=Label(tab2, text='8AM',width='7', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab17.place(x=680, y=300)
Ftab18=Label(tab2, text='10AM',width='7', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab18.place(x=680, y=350)
Ftab19=Label(tab2, text='12PM',width='7', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab19.place(x=680, y=400)
Ftab20=Label(tab2, text='9PM',width='7', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab20.place(x=680, y=450)
#Bording place
Ftab21=Label(tab2, text='OFFICE/EWUATA/AWINDIRI/SUNFORD',width='40', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab21.place(x=835, y=300)
Ftab22=Label(tab2, text='OFFICE/EWUATA/AWINDIRI/SUNFORD',width='40', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab22.place(x=835, y=350)
Ftab23=Label(tab2, text='OFFICE/EWUAT/AWINDIRI/SUNFORD',width='40', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab23.place(x=835, y=400)
Ftab24=Label(tab2, text='OFFICE/EWUATA/AWINDIRI/SUNFORD',width='40', height='1', bg='light blue', fg='black', font=('Calibri light bold',13))
Ftab24.place(x=835, y=450)

#Attractve
Ftab20=Label(tab2, text='BABY COACH BUSES...FOR A STRESS FREE RIDE.',width='50', height='1', bg='light blue', fg='red', font=('CHILLER',25))
Ftab20.place(x=260, y=620)
#========================================tab3======================================================================
start1=Label(tab3,text="BOOK YOUR BUS NOW",width="27",height=1,bg="light blue",fg="red",font=("ALGERIAN",25))
start1.place(x=280,y=20)


FirstName=StringVar()
LastName=StringVar()
Email=StringVar()
PhoneNumber=StringVar()
BusNo=StringVar()
Station=StringVar()
def database():
    name1=FirstName.get()
    name2=LastName.get()
    #name3=OtherName.get()
    email=Email.get()
    number=PhoneNumber.get()
    bus=BusNo.get()
    station=Station.get()

    conn=sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Booking(FirstName TEXT,LastName TEXT,Email TEXT,PhoneNumber TEXT,BusNo TEXT,Station TEXT)')
    cursor.execute('INSERT INTO Booking (FirstName,LastName,Email,PhoneNumber,BusNo,Station) VALUES(?,?,?,?,?,?)',(name1,name2,email,number,bus,station,))
    conn.commit()

    cursor.execute('select * from Booking where PhoneNumber=PhoneNumber')
    print(cursor.fetchall())
    

label=Label(tab3,text='Registration Form',width=20,bg='light blue',fg='red',font=('Calibri light',20))
label.place(x=400,y=70)

label1=Label(tab3,text='FirstName:',width=30,bg='light blue',fg='black',font=('Calibri light',15))
label1.place(x=300,y=150)
entry1=Entry(tab3,textvar=FirstName,width=30)
entry1.place(x=550,y=150)

label3=Label(tab3,text='LastName:',width=20,bg='light blue',fg='black',font=('Calibri light',15))
label3.place(x=350,y=200)
entry3=Entry(tab3,textvar=LastName,width=30)
entry3.place(x=550,y=200)

label5=Label(tab3,text='Email:',width=20,bg='light blue',fg='black',font=('Calibri light',15))
label5.place(x=360,y=250)
entry5=Entry(tab3,textvar=Email,width=30)
entry5.place(x=550,y=250)

mlabel5=Label(tab3,text='PhoneNumber:',width=18,height=1,bg="light blue",fg="black",font=("Calibri light",15))
mlabel5.place(x=360,y=300)
mEntry5=Entry(tab3,textvariable=PhoneNumber,width=30)
mEntry5.place(x=550,y=300)

mlabel6=Label(tab3,text='BusNo:',width=18,height=1,bg="light blue",fg="black",font=("Calibri light",15))
mlabel6.place(x=370,y=340)
list1=['BABY1','BABY2','BABY3','BABY4'];
#c=StringVar()
drop=OptionMenu(tab3,BusNo,*list1)
drop.config(width=15)
BusNo.set('Choose a Bus')
drop.place(x=570,y=340)

mlabel7=Label(tab3,text='Station:',width=15,height=1,bg="light blue",fg="black",font=("Calibri light",15))
mlabel7.place(x=370,y=455)
listh=['Office','Ewuata','Awindiri','SunFord'];
d=StringVar()
drop=OptionMenu(tab3,Station,*listh)
drop.config(width=20)
Station.set('Pickup Station')
drop.place(x=570,y=455)


Button(tab3,text='SUBMIT',width=18,height=1,bg="red",fg="black",command=database).place(x=500,y=580)

   
#========================================tab4======================================================================
start1=Label(tab4,text="CHOOSE YOUR SEAT",width="22",height=1,bg="light blue",fg="red",font=("sylfaen",20))
start1.place(x=400,y=20)
#seat
SeatNo=IntVar()
def database():
    seat=SeatNo.get()
    conn=sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Seat(SeatNo TEXT)')
    cursor.execute('INSERT INTO Seat (SeatNo) VALUES(?)',(seat,))
    conn.commit()
#SEATS
def action():
    btn.configure(text='Booked')
btn=ttk.Button(tab4,text='1',command=action)
btn.place(x=20,y=110)
def action():
    btn1.configure(text='Booked')
btn1=ttk.Button(tab4,text='2',command=action)
btn1.place(x=110,y=110)
def action():
    btn2.configure(text='Booked')
btn2=ttk.Button(tab4,text='25',command=action)
btn2.place(x=300,y=110)
def action():
    btn3.configure(text='Booked')
btn3=ttk.Button(tab4,text='26',command=action)
btn3.place(x=390,y=110)
def action():
    btn4.configure(text='Booked')
btn4=ttk.Button(tab4,text='27',command=action)
btn4.place(x=480,y=110)
def action():
    btn5.configure(text='Booked')
btn5=ttk.Button(tab4,text='3',command=action)
btn5.place(x=20,y=150)
def action():
    btn6.configure(text='Booked')
btn6=ttk.Button(tab4,text='4',command=action)
btn6.place(x=110,y=150)
def action():
    btn7.configure(text='Booked')
btn7=ttk.Button(tab4,text='28',command=action)
btn7.place(x=300,y=150)
def action():
    btn8.configure(text='Booked')
btn8=ttk.Button(tab4,text='29',command=action)
btn8.place(x=390,y=150)
def action():
    btn9.configure(text='Booked')
btn9=ttk.Button(tab4,text='30',command=action)
btn9.place(x=480,y=150)
def action():
    btn10.configure(text='Booked')
btn10=ttk.Button(tab4,text='5',command=action)
btn10.place(x=20,y=190)
def action():
    btn11.configure(text='Booked')
btn11=ttk.Button(tab4,text='6',command=action)
btn11.place(x=110,y=190)
def action():
    btn12.configure(text='Booked')
btn12=ttk.Button(tab4,text='31',command=action)
btn12.place(x=300,y=190)
def action():
    btn13.configure(text='Booked')
btn13=ttk.Button(tab4,text='32',command=action)
btn13.place(x=390,y=190)
def action():
    btn14.configure(text='Booked')
btn14=ttk.Button(tab4,text='33',command=action)
btn14.place(x=480,y=190)
def action():
    btn15.configure(text='Booked')
btn15=ttk.Button(tab4,text='7',command=action)
btn15.place(x=20,y=240)
def action():
    btn16.configure(text='Booked')
btn16=ttk.Button(tab4,text='8',command=action)
btn16.place(x=110,y=240)
def action():
    btn17.configure(text='Booked')
btn17=ttk.Button(tab4,text='34',command=action)
btn17.place(x=300,y=240)
def action():
    btn18.configure(text='Booked')
btn18=ttk.Button(tab4,text='35',command=action)
btn18.place(x=390,y=240)
def action():
    btn19.configure(text='Booked')
btn19=ttk.Button(tab4,text='36',command=action)
btn19.place(x=480,y=240)
def action():
    btn20.configure(text='Booked')
btn20=ttk.Button(tab4,text='9',command=action)
btn20.place(x=20,y=280)
def action():
    btn21.configure(text='Booked')
btn21=ttk.Button(tab4,text='10',command=action)
btn21.place(x=110,y=280)
def action():
    btn22.configure(text='Booked')
btn22=ttk.Button(tab4,text='37',command=action)
btn22.place(x=300,y=280)
def action():
    btn23.configure(text='Booked')
btn23=ttk.Button(tab4,text='38',command=action)
btn23.place(x=390,y=280)
def action():
    btn24.configure(text='Booked')
btn24=ttk.Button(tab4,text='39',command=action)
btn24.place(x=480,y=280)
def action():
    btn25.configure(text='Booked')
btn25=ttk.Button(tab4,text='11',command=action)
btn25.place(x=20,y=320)
def action():
    btn26.configure(text='Booked')
btn26=ttk.Button(tab4,text='12',command=action)
btn26.place(x=110,y=320)
def action():
    btn27.configure(text='Booked')
btn27=ttk.Button(tab4,text='40',command=action)
btn27.place(x=300,y=320)
def action():
    btn28.configure(text='Booked')
btn28=ttk.Button(tab4,text='41',command=action)
btn28.place(x=390,y=320)
def action():
    btn29.configure(text='Booked')
btn29=ttk.Button(tab4,text='42',command=action)
btn29.place(x=480,y=320)
def action():
    btn30.configure(text='Booked')
btn30=ttk.Button(tab4,text='13',command=action)
btn30.place(x=20,y=360)
def action():
    btn31.configure(text='Booked')
btn31=ttk.Button(tab4,text='14',command=action)
btn31.place(x=110,y=360)
def action():
    btn32.configure(text='Booked')
btn32=ttk.Button(tab4,text='43',command=action)
btn32.place(x=300,y=360)
def action():
    btn33.configure(text='Am clicked')
btn33=ttk.Button(tab4,text='44',command=action)
btn33.place(x=390,y=360)
def action():
    btn34.configure(text='Booked')
btn34=ttk.Button(tab4,text='45',command=action)
btn34.place(x=480,y=360)
def action():
    btn35.configure(text='Booked')
btn35=ttk.Button(tab4,text='15',command=action)
btn35.place(x=20,y=400)
def action():
    btn36.configure(text='Booked')
btn36=ttk.Button(tab4,text='16',command=action)
btn36.place(x=110,y=400)
def action():
    btn3k.configure(text='Booked')
btn3k=ttk.Button(tab4,text='46',command=action)
btn3k.place(x=300,y=400)
def action():
    btn37.configure(text='Am clickBookeded')
btn37=ttk.Button(tab4,text='47',command=action)
btn37.place(x=390,y=400)
def action():
    btn38.configure(text='Booked')
btn38=ttk.Button(tab4,text='48',command=action)
btn38.place(x=480,y=400)
def action():
    btn39.configure(text='Booked')
btn39=ttk.Button(tab4,text='15',command=action)
btn39.place(x=20,y=400)
def action():
    btn40.configure(text='Booked')
btn40=ttk.Button(tab4,text='17',command=action)
btn40.place(x=20,y=440)
def action():
    btn41.configure(text='Booked')
btn41=ttk.Button(tab4,text='18',command=action)
btn41.place(x=110,y=440)
def action():
    btn42.configure(text='Booked')
btn42=ttk.Button(tab4,text='49',command=action)
btn42.place(x=300,y=440)
def action():
    btn43.configure(text='Booked')
btn43=ttk.Button(tab4,text='50',command=action)
btn43.place(x=390,y=440)
def action():
    btn44.configure(text='Booked')
btn44=ttk.Button(tab4,text='51',command=action)
btn44.place(x=480,y=440)
def action():
    btn45.configure(text='Booked')
btn45=ttk.Button(tab4,text='19',command=action)
btn45.place(x=20,y=480)
def action():
    btn46.configure(text='Booked')
btn46=ttk.Button(tab4,text='20',command=action)
btn46.place(x=110,y=480)
def action():
    btn47.configure(text='Booked')
btn47=ttk.Button(tab4,text='49',command=action)
btn47.place(x=300,y=480)
def action():
    btn48.configure(text='Booked')
btn48=ttk.Button(tab4,text='50',command=action)
btn48.place(x=390,y=480)
def action():
    btn49.configure(text='Booked')
btn49=ttk.Button(tab4,text='51',command=action)
btn49.place(x=480,y=480)
def action():
    btn50.configure(text='Booked')
btn50=ttk.Button(tab4,text='21',command=action)
btn50.place(x=20,y=520)
def action():
    btn51.configure(text='Booked')
btn51=ttk.Button(tab4,text='22',command=action)
btn51.place(x=110,y=520)
def action():
    btn52.configure(text='Booked')
btn52=ttk.Button(tab4,text='55',command=action)
btn52.place(x=300,y=520)
def action():
    btn53.configure(text='Booked')
btn53=ttk.Button(tab4,text='56',command=action)
btn53.place(x=390,y=520)
def action():
    btn54.configure(text='Booked')
btn54=ttk.Button(tab4,text='57',command=action)
btn54.place(x=480,y=520)
def action():
    btn55.configure(text='Booked')
btn55=ttk.Button(tab4,text='23',command=action)
btn55.place(x=20,y=560)
def action():
    btn56.configure(text='Booked')
btn56=ttk.Button(tab4,text='24',command=action)
btn56.place(x=110,y=560)
def action():
    btn57.configure(text='Booked')
btn57=ttk.Button(tab4,text='58',command=action)
btn57.place(x=300,y=560)
def action():
    btn58.configure(text='Booked')
btn58=ttk.Button(tab4,text='59',command=action)
btn58.place(x=390,y=560)
def action():
    btn59.configure(text='Booked')
btn59=ttk.Button(tab4,text='60',command=action)
btn59.place(x=480,y=560)
def action():
    btn60.configure(text='Booked')
btn60=ttk.Button(tab4,text='61',command=action)
btn60.place(x=20,y=600)
def action():
    btn61.configure(text='Booked')
btn61=ttk.Button(tab4,text='62',command=action)
btn61.place(x=110,y=600)
def action():
    btn62.configure(text='Booked')
btn62=ttk.Button(tab4,text='63',command=action)
btn62.place(x=200,y=600)
def action():
    btn63.configure(text='Booked')
btn63=ttk.Button(tab4,text='64',command=action)
btn63.place(x=300,y=600)
def action():
    btn64.configure(text='Booked')
btn64=ttk.Button(tab4,text='65',command=action)
btn64.place(x=390,y=600)
def action():
    btn65.configure(text='Booked')
btn65=ttk.Button(tab4,text='66',command=action)
btn65.place(x=480,y=600)


mlabel7=Label(tab4,text='NB. Dear customer,you are required to click\n on the seat number you want to take',width=45,height=2,bg="light blue",fg="red",font=("Calibri light",15))
mlabel7.place(x=600,y=155)
image2home1 = PhotoImage(file="C:\\Users\\KEITH NAMU\\Desktop\\kato\\baby1.p.png")
w = image2home.width()
h = image2home.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 =Label(tab4, image=image2home1)
panel1.place(x=600,y=250)
image2home2 = PhotoImage(file="C:\\Users\\KEITH NAMU\\Desktop\\kato\\white.1.png")
w = image2home.width()
h = image2home.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 =Label(tab4, image=image2home2)
panel1.place(x=800,y=250)
image2home3 = PhotoImage(file="C:\\Users\\KEITH NAMU\\Desktop\\kato\\3.p.png")
w = image2home.width()
h = image2home.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 =Label(tab4, image=image2home3)
panel1.place(x=800,y=450)





#button1=Button(tab4,text='OK',width=5,height=1,bg="light blue",fg="black",command=database).place(x=700,y=300)    
#========================================button======================================================================
start1=Label(tab5,text="MAKE YOUR PAYMENT",width="23",height=1,bg="light blue",fg="red",font=("sylfaen",20))
start1.place(x=350,y=20)
#========================================button====================================================================== 
start1=Label(tab6,text="OTHER SERVICES WE OFFER",width="25",height=1,bg="light blue",fg="red",font=("sylfaen",20))
start1.place(x=400,y=20)
Glab1= Label(tab6,text='Our dear customers thank you for always travelling with baby coach\n below is the return for your co-operation',width = '60'\
             , height = 2, bg='light BLUE', fg ='red',font=("Calibri light",15))
Glab1.place(x=280, y=70)
Glab2=Label(tab6,text='1. Our dear customer if you travel with us more than FIVE times,you will be offered 10% DISCOUNT on the\n amount of money to be given for the next journey.',width=85,height=2,bg='light blue',fg='black',font=("Calibri light",15))
Glab2.place(x=50, y=120)
Glab3=Label(tab6,text='2. Our dear cusomer, every  TWO times you travel with us, you DO NOT PAY for the luggage the third time\n you travel with us. ',width=85,height=2,bg='light blue',fg='black',font=("Calibri light",15))
Glab3.place(x=50, y=180)
Glab4=Label(tab6,text='3. Our dear customer if you travel with us more than TEN times,you will be given a chance to choose a permanent\n seat in our bus and it will always be there for you whenever you travel with us',width=92,height=2,bg='light blue',fg='black',font=("Calibri light",15))
Glab4.place(x=50, y=240)
Glab5=Label(tab6,text='4. Our dear customer, the more you travel with us ts the more you increase your chance to WIN a journey\n to watch AFRICAN CUP of nations finals plus many other prizes that are ready for you',width=92,height=2,bg='light blue',fg='black',font=("Calibri light",15))
Glab5.place(x=20, y=300)

Ftab60=Label(tab6, text='WE ARE READY TO SERVE YOU DEAR CUSTOMER',width='50', height='1', bg='light blue', fg='red', font=('CHILLER',25))
Ftab60.place(x=220, y=500)
Glab6=Button(tab6,text='Exit',command=window.destroy,bg='red',fg='black',width=10,font=("sylfaen",10),activebackground='blue')
Glab6.place(x=450,y=570)






window.mainloop()



