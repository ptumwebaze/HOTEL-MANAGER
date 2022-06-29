from tkinter import *
import tkinter.messagebox 
import sqlite3

from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import time
import datetime
import random



#from PIL import Image, ImageTk

#for calling different interfaces
def handle(frame):
    frame.tkraise()

window=Tk()
window.geometry('10000x10000')
##frame1 = Frame(window,bg= 'pink',width = 10000,height= 1000)
##frame2 = Frame(window,bg= 'pink',width = 10000,height= 1000)
##frame3 = Frame(window,bg= 'pink',width = 10000,height= 1000)
##frame4 = Frame(window,bg= 'pink',width = 10000,height= 1000)
##frame4_1 = Frame(window,bg= 'pink',width = 10000,height= 1000)
##frame4_2 = Frame(window,bg= 'pink',width = 10000,height= 1000)
##frame5 = Frame(window)
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

tab_control.add(tab1, text='      Home         ')
tab_control.add(tab2, text='      Aboutus    ')
tab_control.add(tab3, text='      Rooms         ')
tab_control.add(tab4, text='      Contacts        ')
tab_control.add(tab5, text='      Book Now                 ')

#===================================================================
#for frame in (frame1,frame2,frame3,frame4,frame4_1,frame4_2,frame5):
    #frame.grid(row =0 ,column=0,sticky = 'news')
start1=Tk()
start1=Label(tab1,text='WELCOME TO SKYLITE HOTEL!!',width="30",height=1,bg="purple",fg="red",font=("lucida calligraphy",30))
start1.place(x=100,y=30)
my_image = PhotoImage(file='C:\\Users\\Admin\\Desktop\\bus.gif')
canvas=Canvas(start1,width=100, height=100 ,bg='#00ff00', higlightthickness=0)
canvas.pack(expand = YES, fill = BOTH)
canvas.create_image(0,0, anchor=NW, image=my_image)
canvas.my_image=my_image

#image3=PhotoImage(file='H:\plants\images of cabbage\lives.PNG')
#panel=Label(frame1,image=image3)
#panel.place(x=315,y=5)
window.title("Hotel management system")
label1=Label(frame1,text="SKYLITE HOTEL  ",bg="white",fg="black",font=("Calbri 34"))
label1.place(x=200,y=30)
label2=Label(frame1,text="Welcome to SKYLITE\n HOTEL\n \nThis is the best place for you and your loved ones, \n come relax and have fun out of home!! ",bg="white",fg="black",font=("Helvetica 15"))#label
label2.place(x=80,y=200)

#image4=PhotoImage(file='H:\plants\images of cabbage\lives.PNG')
#panel=Label(frame2,image=image4)
#panel.place(x=5,y=5)


buton1=Button(frame1,text="NEXT",bg='green',fg='white',width='5',font=("calbri 18 bold"),command = lambda:handle(frame2))
buton1.place(x=1275,y=600)
framem = Frame(frame1,bg='white', width=1500, height=80) 
framem.place(x=1, y=640)
footer1 = Label(framem, text="Contact Us On:",  fg='darkblue',bg="white", font=('times new roman', 14))
footer1.place(x=50, y=5)
footer2 = Label(framem, text="+256 786 605 110", fg='black',bg="white", font=('times new roman', 11))
footer2.place(x=180, y=5)
footer3 = Label(framem, text="+256 753 827 096", fg='black',bg="white", font=('times new roman', 11))
footer3.place(x=180, y=25)

footer4 = Label(framem, text="E-mail:",  fg='darkblue',bg="white", font=('times new roman', 14))
footer4.place(x=380, y=5)

footer5 = Label(framem, text="info@frescosupmrkt.org.ug",  fg='black',bg="white", font=('times new roman', 11))
footer5.place(x=450, y=5)

footer6 =Label(framem,text="nabasaritah02@gmail.com",fg='black',bg="white",font=('times new roman',11))
footer6.place(x=450, y=25)

footer7 = Label(framem, text="Media:",  fg='darkblue',bg="white", font=('times new roman', 14))
footer7.place(x=700, y=5)

footer8 = Label(framem, text="Facebook rhyter keysher",  fg='black',bg="white", font=('times new roman', 11))
footer8.place(x=780, y=5)
footer9 = Label(framem, text="YouTube",  fg='black',bg="white", font=('times new roman', 11))
footer9.place(x=780, y=25)
footer10 = Label(framem, text="Twitter  @rhyterkeysher",  fg='black',bg="white", font=('times new roman', 11))
footer10.place(x=880, y=5)
footer11 = Label(framem, text="Instagram @rhyterkeysher",  fg='black',bg="white", font=('times new roman', 11))
footer11.place(x=880, y=25)

footer = Label(framem, text="copy;2019 copyright. All rights Reserved",  fg='red',bg="white",
                    font=('times new roman', 10))
footer.place(x=350, y=50)
        
#buton2=Button(frame1,text="NEXT",bg='green',fg='white',width='5',font=("calbri 18 bold"),command = lambda:handle(frame2))
#buton2.place(x=200,y=600)



window.title('SKYLITE HOTEL')
#title1=Label(frame2,text="SKYLITE HOTELT ",bg="white",fg="black",font=("Calbri 34"))
#title1.place(x=200,y=30)
#label2=Label(frame2,text="LET'S MAKE LIFE BETTER ",bg="white",fg="black",font=("Calbri 20"),width=25)
#label2.place(x=380,y=100)


#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD= StringVar()
USERNAME2 = StringVar()
PASSWORD2 = StringVar()


#==============================LABELS=========================================
lbl_title = Label(frame2, text = "LOGIN TO HAVE ACCESS", bg="white", font=('times new roman', 20))
lbl_title.place(x=500,y=20)

lbl1_title=Label(frame2, text = "ADMINISTRATOR", bg="white", font=('times new roman', 15))
lbl1_title.place(x=200,y=70)

lbl2_title=Label(frame2, text = "TELLER", bg="white", font=('times new roman', 15))
lbl2_title.place(x=800,y=70)


lbl_username = Label(frame2, text = "Username:", bg="white", font=('times new roman', 15))
lbl_username.place(x=200,y=150)

lbl_username2 = Label(frame2, text = "Username:", bg="white", font=('times new roman', 15))
lbl_username2.place(x=800,y=150)

lbl_password = Label(frame2, text = "Password:", bg="white", font=('times new roman', 15))
lbl_password.place(x=200,y=200)

lbl_password2 = Label(frame2, text = "Password:", bg="white", font=('times new roman', 15))
lbl_password2.place(x=800,y=200)

 
#==============================ENTRY WIDGETS==================================
username = ttk.Entry(frame2, textvariable=USERNAME,width=25 ,font=('times new roman', 15))
username.place(x=300,y=150)

username2 = ttk.Entry(frame2, textvariable=USERNAME2,width=25 ,font=('times new roman', 15))
username2.place(x=900,y=150)

password = ttk.Entry(frame2, textvariable=PASSWORD,width=25, show="*", font=('times new roman', 15))
password.place(x=300,y=200)

password2 = ttk.Entry(frame2, textvariable=PASSWORD2,width=25, show="*", font=('times new roman', 15))
password2.place(x=900,y=200)
 


def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()



def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("ERROR", "Mendatory Field is empty")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (username.get(), password.get()))
    if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME1.set("")
            PASSWORD1.set("")
    else:
            messagebox.showinfo("ERROR", "Invalid Username or Password")
            USERNAME1.set("")
            PASSWORD1.set("")
            
    cursor.close()
    conn.close()



btn_login = ttk.Button(frame2, text="Login", width=20, command=Login)
btn_login.place(x=425, y=300)

button2=Button(frame2,text='BACK',font=('calbri 17 bold'),bg='red',fg='white',width='10',command=lambda:handle(frame1))
button2.place(x=15,y=650)

def HomeWindow():
    global Home
    window.withdraw()
    Home=Tk()
    Home.geometry('10000x10000')

    Home.title("FRESCO SUPERMARKET MANAGEMENT SYSTEM)")
    Home.config(bg="turquoise")

    button2=Button(Home,text='HOME',font=('calbri 17 bold'),bg='GREY',fg='white',width=20,command=lambda:handle(frame3))
    button2.place(x=90,y=150)
    button3=Button(Home,text=' CREATE ACCOUNT',font=('calbri 17 bold'),bg='GREY',fg='white',width=20)
    button3.place(x=400,y=150)
    button4=Button(Home,text=' ITEMS',font=('calbri 17 bold'),bg='GREY',fg='white',width=20)
    button4.place(x=800,y=150)
    button5=Button(Home,text='  PURCHASES',font=('calbri 17 bold'),bg='GREY',fg='white',width=20)
    button5.place(x=90,y=300)
    button6=Button(Home,text='  VIEW RECORDS',font=('calbri 17 bold'),bg='GREY',fg='white',width=20)
    button6.place(x=400,y=300)
    button7=Button(Home,text='  PERSONAL',font=('calbri 17 bold'),bg='GREY',fg='white',width=20)
    button7.place(x=800,y=300)

def button2():

        button2 = Button(window,width=1300,height=550, bg="lightgreen")
        button2.place(x=170, y=80)


        Fullname=StringVar()
        Email=StringVar()
        PhoneNo=StringVar()
        RegNo=StringVar()
        Job_Title=StringVar()
        gender=StringVar()
        var = IntVar()
       



        def database():
           name1=Fullname.get()
           email=Email.get()
           phoneNo=PhoneNo.get()
           RegNo=RegNo.get()
           job_Title=Job_Title.get()
           gender=var.get()
           conn = sqlite3.connect('Form.db')
           with conn:
              cursor=conn.cursor()
           cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,PhoneNo TEXT,RegNo TEXT,Job_Title TEXT,Gender TEXT)')
           cursor.execute('INSERT INTO Student (FullName,Email,PhoneNo,Job_Title,Gender) VALUES(?,?,?,?,?,?)',(name1,email,phoneNo,RegNo,job_Title,gender))
           conn.commit()
           
           
                     
        label_0 = Label(button2, text="Registration form",bg="lightgreen",width=20,font=("bold", 20))
        label_0.place(x=90,y=20)
        
        label_reg = Label(button2, text="RegNo",bg="lightgreen",font=("bold", 10))
        label_reg.place(x=180,y=120)
        entry_reg= ttk.Entry(button2,textvar=RegNo,width=40)
        entry_reg.place(x=270,y=120)


        label_1 = Label(button2, text="FullName",bg="lightgreen",font=("bold", 10))
        label_1.place(x=180,y=160)
        entry_1 = ttk.Entry(button2,textvar=Fullname,width=40)
        entry_1.place(x=270,y=160)

        label_2 = Label(button2, text="Email",bg="lightgreen",font=("bold", 10))
        label_2.place(x=180,y=200)
        entry_2 = ttk.Entry(button2,textvar=Email,width=40)
        entry_2.place(x=270,y=200)

        label_p = Label(button2, text="PhoneNo:",bg="lightgreen",font=("bold", 10))
        label_p.place(x=180,y=240)
        entry_p = ttk.Entry(button2,textvar=PhoneNo,width=40)
        entry_p.place(x=270,y=240)

        label_j = Label(button2, text="Job Title",bg="lightgreen",font=("bold", 10))
        label_j.place(x=180,y=280)
        entry_j = ttk.Entry(button2,textvar=Job_Title,width=40)
        entry_j.place(x=270,y=280)

        label_d = Label(button2, text="Date of Birth",bg="lightgreen",font=("bold", 10))
        label_d.place(x=180,y=320)
        entry_d = ttk.Entry(button2,textvar=Job_Title,width=40)
        entry_d.place(x=270,y=320)
        

        label_3 = Label(button2, text="Gender",bg="lightgreen",font=("bold", 10))
        label_3.place(x=180,y=360)

        Radiobutton(button2, bg="lightgreen",text="Male",padx = 5, variable=var, value=1).place(x=270,y=360)
        Radiobutton(button2, bg="lightgreen",text="Female",padx = 20, variable=var, value=2).place(x=340,y=360)

        label_4 = Label(button2,bg="lightgreen", text="country",font=("bold", 10))
        label_4.place(x=180,y=400)

        list1 = ['Canada','India','UK','Nepal','Iceland','South Africa','Uganda','Kenya'];

        droplist=OptionMenu(button2,c, *list1)
        droplist.config(width=15)
        c.set('select your country') 
        droplist.place(x=270,y=400)

        label_4 = Label(self.button2, bg="lightgreen",text="Programming",font=("bold", 10))
        label_4.place(x=180,y=440)
        var2= IntVar()
        Checkbutton(button2, bg="lightgreen",text="java", variable=var1).place(x=270,y=440)

        Checkbutton(button2, bg="lightgreen",text="python", variable=var2).place(x=340,y=440)

        Button(button2, text='Submit',width=30,bg='brown',fg='white',command=database).place(x=280,y=480)


    
#wwindow.mainloop()

    
        btn_back = Button(Home, text='LOGOUT',bg="blue",fg="white",width=15, command=Back)
        btn_back.place(x=20, y=2)


def Homey():

    frame3 = Tk()
    frame3.title("FRESCO SUPERMARKET MANAGEMENT SYSTEM)")

def Back():
    Home.destroy()
    window.deiconify()




#window.title("FRESCO SUPERMARKET MANAGEMENT SYSTEM")
#label1=Label(frame3,text="FRESCO SUPERMARKET ",bg="white",fg="black",font=("Calbri 34"))
#label1.place(x=200,y=30)
#label=Label(frame3,text="PLEASE LOGIN TO GET ACCESS ",bg="white",fg="black",font=("Calbri 12"))
#label.place(x=350,y=150)
#buton=Button(frame3,text="username",bg='GREY',fg='white',font=("calbri 12"),command=lambda:handle(frame4))
#buton.place(x=120,y=350)

#image=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\B1.PNG')
#panel=Label(frame3,image=image)
#panel.place(x=50,y=400)

#buton=Button(frame3,text="password",bg='GREY',fg='white',font=("calbri 12"),command=lambda:handle(frame4_1))
#buton .place(x=450,y=350)

#image1=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\T1.PNG')
#panel=Label(frame3,image=image1)
#panel.place(x=400,y=400)

#buton=Button(frame3,text="BACK",bg='red',fg='white',width='5',font=("calbri 12"),command=lambda:handle(frame2))
#buton.place(x=15,y=650)
####FRAME 4
#window.title("FRESCO SUPERMARKET MANAGEMENT SYSTEM")
#label1=Label(frame4,text="AGRO-CHEMICAL SOLUTIONS ",bg="black",fg="white",font=("Calbri 34"))
#label1.place(x=200,y=30)
#### TOMATO BLIGHT
#label2=Label(frame4, text='TOMATO BLIGHT SIGNS AND SYMPTOMS',bg="white",fg="black",font='Calbri 15')
#label2.place(x=300, y=100)
#label4=Label(frame4,text="Rotten tomato",bg="white",fg="black",font=("calbri 15"))
#label4.place(x=80,y=170)
#image4=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\B8.PNG')
#panel=Label(frame4,image=image4)
#panel.place(x=10,y=220)

#label5=Label(frame4,text="Wilting Leaves",bg="white",fg="black",font=("calbri 15"))
#label5.place(x=450,y=170)                  
#image5=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\B2.PNG')
#panel=Label(frame4,image=image5)
#panel.place(x=370,y=220)

#label6=Label(frame4,text="Rotting stem",bg="white",fg="black",font=("calbri 15"))
#label6.place(x=750,y=170)
#image6=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\B1.PNG')
#panel=Label(frame4,image=image6)
#panel.place(x=700,y=220)                  
                  
#button=Button(frame4,text="Treatment",bg='red',fg='white',width='10',font=("calbri 12"),command=lambda:handle(frame5))
#button.place(x=890,y=700)
#button1=Button(frame4,text="BACK",bg='red',fg='white',width='5',font=("calbri 12"),command=lambda:handle(frame3))
#button1.place(x=50,y=500)

#### DUMPING OFF Frame 4_1
#label1=Label(frame4_1,text="AGRO-CHEMICAL SOLUTIONS ",bg="white",fg="black",font=("Calbri 34"))
#label1.place(x=200,y=30)
#label2=Label(frame4_1, text='DUMPING OFF SIGNS AND SYMPTOMS',bg="white",fg="black",font='Calbri 18')
#label2.place(x=300, y=100)
#label4=Label(frame4_1,text="Rotten Roots",bg="white",fg="black",font=("calbri 15"))
#label4.place(x=80,y=170)
#image7=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\D1.PNG')
#panel=Label(frame4_1,image=image7)
#panel.place(x=10,y=220)

#label5=Label(frame4_1,text="wilting plant",bg="black",fg="white",font=("calbri 15"))
#label5.place(x=400,y=170)
#image8=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\D2.PNG')
#panel=Label(frame4_1,image=image8)
#panel.place(x=332,y=220)

#label6=Label(frame4_1,text="Rotting stem",bg="white",fg="black",font=("calbri 15"))
#label6.place(x=750,y=170)
#image9=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\D3.PNG')
#panel=Label(frame4_1,image=image9)
#panel.place(x=700,y=220)

#button=Button(frame4_1,text="Treatment",bg='red',fg='white',width='10',font=("calbri 12"))
#button.place(x=890,y=700)
#buton=Button(frame4_1,text="BACK",bg='red',fg='white',width='5',font=("calbri 12"),command=lambda:handle(frame3))
#buton.place(x=15,y=650)

####Frame 4_2
#label=Label(frame4_2,text="AGRO-CHEMICAL SOLUTIONS ",bg="white",fg="black",font=("Calbri 34"))
#label.place(x=200,y=30)

#label=Label(frame4_2, text='BACTERIAL WILT SIGNS AND SYMPTOMS',bg="white",fg="black",font='Calbri 18')
#label.place(x=300, y=100)
#label=Label(frame4_2,text="Wilting Leaves",bg="white",fg="black",font=("calbri 15"))
#label.place(x=80,y=170)
#image_1=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\D1.PNG')
#panel=Label(frame4_1,image=image_1)
#panel.place(x=10,y=220)

#label=Label(frame4_2,text="Hallow and rotten stems",bg="white",fg="black",font=("calbri 15"))
#label.place(x=400,y=170)
#image_2=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\D2.PNG')
#panel=Label(frame4_1,image=image_2)
#panel.place(x=332,y=220)

#label=Label(frame4_2,text="scrotched leaves",bg="white",fg="black",font=("calbri 15"))
#label.place(x=750,y=170)
#image9=PhotoImage(file='C:\\Users\\user\\Desktop\\project\\images\\D3.PNG')
#panel=Label(frame4_1,image=image9)
#panel.place(x=700,y=220)

#button=Button(frame4_2,text="Treatment",bg="white",fg="black",font=("calbri 12"))
#button.place(x=890,y=650)
#buton=Button(frame4_1,text="BACK",bg="white",fg="black",font=("calbri 12"),command=lambda:handle(frame3))
#buton.place(x=15,y=650)
#buton1=Button(window,text="MUSINGUZI VINCENT DAVID",bg="black",fg="white",font=("Times 10 bold"))
#buton1.place(x=0,y=10)

#Drug application(frame5)
#import sqlite3 as lite
#conn = lite.connect('Agro-chemicals')
#cur = conn.cursor()
#rows=cur.execute('SELECT* FROM Drugs where DiseaseID = "D01"')



#g.geometry('950x800+0+0')
#g.title('Kiguli Emmanuel')
#header = Label(frame5, text="AGRO-CHEMICAL SOLUTION", font=('calbri',30,'bold'), fg='black#L1 = Label(frame5, text = 'DRUG APPLICATION', font=('calbri', 20,'bold')).place(x=250,y=50)
#button1 = Button(frame5, text='BACK',font =('calbri',15),fg= 'black',bg = 'green',command=lambda:handle(frame4))
#button1.place(x=10,y= 500)



#headings......................
#Label(frame5,text = 'Drug Name',font = ('arial',15),fg = 'black',bg = 'white',width = 20).place(x= 10,y= 100)
#Label(frame5,text = 'Area of application',font = ('arial',15),fg = 'black',bg = 'white',width =20).place(x= 250,y = 100)
#Label(frame5,text = 'Mixture',font = ('arial',15),fg = 'black',bg = 'white',width = 40).place(x= 490,y = 100)
#print(mixture)
#print(rows,app,mixture)


#for row in rows:
    
    #text=Text(frame5)
    #text.insert( INSERT,row[1])
    #text.config(foreground="black",background="white",height = 7,width= 30)
    #text.place (x= 10,y = 150)

    #text1=Text(frame5)
    #text1.insert( INSERT,row[2])
    #text1.config(foreground="black",background="white",height = 7,width= 30)
    #text1.place (x= 250,y = 150)
    
    
    #text2=Text(frame5)
    #text2.insert( INSERT,row[3])
    #text2.config(foreground="black",background="white",height = 7,width =56)
    #text2.place (x= 490,y = 150)
    #print (row)
handle(frame1)

mainloop()

