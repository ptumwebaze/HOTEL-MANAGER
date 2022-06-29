from tkinter import*
import sqlite3

root=Tk()
root.geometry('650x550')
root.title('Skylite Hotel database')
root.configure(background='powder blue')

textin = StringVar()
textiin=StringVar()
textinn =StringVar()
texttin =StringVar()
textttin =StringVar()
textttinn =StringVar()
textinin =StringVar()
textini =StringVar()
textinii =StringVar()
textinni =StringVar()
textiinn =StringVar()
textiiin =StringVar()
texttiin =StringVar()
textttiin =StringVar()
textttinnn =StringVar()
texttttinnn = StringVar()


menu=Menu(root)
root.config(menu=menu)

menu=Menu(root)
root.config(menu=menu)

lab = Label(root,text='Ref:',bg= 'powder blue',font=('none 13 bold'))
lab.place(x=0,y=0)
entRef = Entry(root,width=20, font=('none 13 bold'),textvar=textin)
entRef.place(x=140,y=0)

lab=Label(root, text='Firstname:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=30)
entFirstname = Entry(root,width=20, font=('none 13 bold'),textvar=textiin)
entFirstname.place(x=140,y=30)

lab=Label(root, text='Surname:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=60)
entSurname = Entry(root,width=20,font=('none 13 bold'),textvar=textinn)
entSurname.place(x=140,y=60)

lab=Label(root, text='Address:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=90)
entAddress = Entry(root,width=20, font=('none 13 bold'),textvar=texttin)
entAddress.place(x=140,y=90)

lab=Label(root, text='Mobile:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=120)
entMobile = Entry(root,width=20, font=('none 13 bold'),textvar=textttin)
entMobile.place(x=140,y=120)

lab=Label(root, text='Email:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=150)
entEmail = Entry(root,width=20, font=('none 13 bold'),textvar=textttinn)
entEmail.place(x=140,y=150)

lab=Label(root, text='Nationality:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=180)
entNationality= Entry(root,width=20, font=('none 13 bold'),textvar=textinin)
entNationality.place(x=140,y=180)

lab=Label(root, text='DOB:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=210)
entDOB = Entry(root,width=20, font=('none 13 bold'),textvar=textini)
entDOB.place(x=140,y=210)

lab=Label(root, text='IDType:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=240)
entIDType = Entry(root,width=20, font=('none 13 bold'),textvar=textinii)
entIDType.place(x=140,y=240)

lab=Label(root, text='Gender:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=270)
entGender = Entry(root,width=20, font=('none 13 bold'),textvar=textinni)
entGender.place(x=140,y=270)

lab=Label(root, text='CheckInDate:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=300)
entCheckInDate= Entry(root,width=20, font=('none 13 bold'),textvar=textiinn)
entCheckInDate.place(x=140,y=300)

lab=Label(root, text='CheckOutDate:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=330)
entCheckOutDate= Entry(root,width=20, font=('none 13 bold'),textvar=textiiin)
entCheckOutDate.place(x=140,y=330)

lab=Label(root, text='Meal:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=360)
entMeal= Entry(root,width=20, font=('none 13 bold'),textvar=texttiin)
entMeal.place(x=140,y=360)

lab=Label(root, text='RoomCategory:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=390)
entRoomCategory= Entry(root,width=20, font=('none 13 bold'),textvar=textttiin)
entRoomCategory.place(x=140,y=390)

lab=Label(root, text='RoomNo:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=420)
entRoomNo= Entry(root,width=20, font=('none 13 bold'),textvar=textttinnn)
entRoomNo.place(x=140,y=420)

lab=Label(root, text='ModeOfPayment:',bg= 'powder blue', font=('none 13 bold'))
lab.place(x=0,y=450)
entRoomNo= Entry(root,width=20, font=('none 13 bold'),textvar=texttttinnn)
entRoomNo.place(x=140,y=450)


db = sqlite3.connect('mql.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS customers(Ref,Firstname,Surname,Address,Mobile, Email,Nationality,DOB,Gender,IDType,CheckInDate,CheckOutDate,Meal,RoomCategory,RoomNo, ModeOfPayment)')
db.commit()

def insert():
    Ref = textin.get()
    Firstname = textiin.get()
    Surname = textinn.get()
    Address = texttin.get()
    Mobile = textttin.get()
    Email = textttinn.get()
    Nationality = textinin.get()
    DOB = textini.get()
    IDType = textinii.get()
    Gender = textinni.get()
    CheckInDate = textiinn.get()
    CheckOutDate = textiiin.get()
    Meal = texttiin.get()
    RoomCategory = textttiin.get()
    RoomNo = textttinnn.get()
    ModeOfPayment= texttttinnn.get()
    conn = sqlite3.connect('mql.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customers(Ref,Firstname,Surname,Address,Mobile, Email,Nationality,DOB,Gender,IDType,CheckInDate,CheckOutDate,Meal,RoomCategory,RoomNo,ModeOfPayment) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Ref,Firstname,Surname,Address,Mobile, Email,Nationality,DOB,Gender,IDType,CheckInDate,CheckOutDate,Meal,RoomCategory,RoomNo,ModeOfPayment))
        db.close()
    

def show():
    connt = sqlite3.connect('mql.db')
    cursor = connt.cursor()
    cursor.execute('SELECT * FROM customers')
    for row in cursor.fetchall():
        print(row)
                    
res=Button(root,padx=2,pady=2,text='show',command=show,font=('none 13 bold'))
res.place(x=160,y=480)

but=Button(root,padx=2,pady=2,text='Submit',command=insert,font=('none 13 bold'))
but.place(x=260,y=480)


                      







                      
 
