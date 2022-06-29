from tkinter import* 
import sqlite3

root = Tk()
root.geometry('410x450')
root.title('Sylite Hotel Database')
root.configure(background='powder blue')

textin=StringVar()
textinn=StringVar()

menu = Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

def helpp():
    help(sqlite3)

subm = Menu(menu)
menu.add_cascade(label='Help',menu=subm)
subm.add_command(label='Sqlite3',command=helpp)

db = sqlite3.connect('sql.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS people(name TEXT, phone TEXT)')
db.commit()

lab=Label(root, text='Name:', font=('none 13 bold'))
lab.place(x=0,y=0)

lab=Label(root, text='Phone:', font=('none 13 bold'))
lab.place(x=0,y=40)

entname = Entry(root,width=20, font=('none 13 bold'),textvar=textin)
entname.place(x=80,y=0)
 
entphone=Entry(root,width=20, font=('none 13 bold'),textvar=textinn)
entphone.place(x=80,y=40)


def insert():

    name1 = textin.get()
    phone1 = textinn.get()
    conn = sqlite3.connect('sql.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO people(name,phone) VALUES(?,?))',(name, phone))
        db.close()

def show():
    connt = sqlite3.connect('sql.db')
    cursor = connt.cursor()
    cursor.execute('SELECT * FROM people')
    for row in cursor.fetchall():
        print(row)


name=StringVar()
phone=StringVar()

but=Button(root,padx=2,pady=2,text='Submit',command=insert,font=('none 13 bold'))
but.place(x=60,y=100)

res=Button(root,padx=2,pady=2,text='show',command=show,font=('none 13 bold'))
res.place(x=160,y=100)

