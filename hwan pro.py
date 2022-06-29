from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import time
from datetime import datetime
import sqlite3


class Hotel:
    def __init__(self,root):

    
        self.root = root
        self.root.title("Skylite Hotel Management System")
        self.root.geometry("1350x750")
        self.root.config(background="white")
       

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame,bd=14, width=1350, height=550, padx=20, relief=RIDGE,bg="cadet blue")
        TopFrame.pack(side=TOP)
        
        LeftFrame = Frame(TopFrame,bd=10, width=450, height=550, padx=2, relief=RIDGE,bg="powder blue")
        LeftFrame.pack(side=LEFT)

                              
        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal= StringVar()
        RoomCategory = StringVar()
        RoomNo = StringVar()
        ModeOfPayment = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        SubTax = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()
 #============================Widget==============================================
        
        self.lblCustomer_Ref =Label(LeftFrame,font=('arial',12,'bold'),text="Customer Ref:",padx=2,bg="powder blue")
        self.lblCustomer_Ref.grid(row=0,column=0,sticky =W)
        self.txtCustomer_Ref = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CustomerRef,width=20)
        self.txtCustomer_Ref.grid(row=0,column=1,pady=3, padx=20)

        self.lblFirstname =Label(LeftFrame,font=('arial',12,'bold'),text="Firstname:",padx=2,bg="powder blue")
        self.lblFirstname.grid(row=1,column=0,sticky =W)
        self.txtFirstname = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Firstname,width=20)
        self.txtFirstname.grid(row=1,column=1,pady=3, padx=20)

        self.lblSurname =Label(LeftFrame,font=('arial',12,'bold'),text="Surname:",padx=2,bg="powder blue")
        self.lblSurname.grid(row=2,column=0,sticky =W)
        self.txtSurname = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Surname,width=20)
        self.txtSurname.grid(row=2,column=1,pady=3, padx=20)

        self.lblAddress =Label(LeftFrame,font=('arial',12,'bold'),text="Address:",padx=2,bg="powder blue")
        self.lblAddress.grid(row=3,column=0,sticky =W)
        self.txtAddress = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Address,width=20)
        self.txtAddress.grid(row=3,column=1,pady=3, padx=20)

        self.lblMobile =Label(LeftFrame,font=('arial',12,'bold'),text="Mobile:",padx=2,bg="powder blue")
        self.lblMobile.grid(row=4,column=0,sticky =W)
        self.txtMobile = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Mobile,width=20)
        self.txtMobile.grid(row=4,column=1,pady=3, padx=20)

        self.lblEmail =Label(LeftFrame,font=('arial',12,'bold'),text="Email:",padx=2,bg="powder blue")
        self.lblEmail.grid(row=5,column=0,sticky =W)
        self.txtEmail = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Email,width=20)
        self.txtEmail.grid(row=5,column=1,pady=3, padx=20)

        self.lblNationality =Label(LeftFrame,font=('arial',12,'bold'),text="Nationality:",padx=2,bg="powder blue")
        self.lblNationality.grid(row=6,column=0,sticky =W)
        self.cboNationality = ttk.Combobox(LeftFrame, textvariable =Nationality, state='readonly', font=('arial', 12, 'bold'),width=18)
        self.cboNationality['value'] = ('', 'Ugandan', 'Kenyan', 'Rwandan', 'American', 'Tanzanian')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=6, column=1, pady=3, padx=20)
        
        self.lblDOB =Label(LeftFrame,font=('arial',12,'bold'),text="DOB:",padx=2,bg="powder blue")
        self.lblDOB.grid(row=7,column=0,sticky =W)
        self.txtDOB = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =DOB,width=20)
        self.txtDOB.grid(row=7,column=1,pady=3, padx=20)

        self.lblIDType=Label(LeftFrame,font=('arial',12,'bold'),text="IDType:",padx=2,bg="powder blue")
        self.lblIDType.grid(row=8,column=0,sticky =W)
        self.cboRoomIDType = ttk.Combobox(LeftFrame, textvariable =IDType, state='readonly', font=('arial', 12, 'bold'),width=18)
        self.cboRoomIDType['value'] = ('', 'Pilot Licence', 'Driving Licence', 'Student ID', 'Passport')
        self.cboRoomIDType.current(0)
        self.cboRoomIDType.grid(row=8, column=1, pady=3, padx=20)

        self.lblGender =Label(LeftFrame,font=('arial',12,'bold'),text="Gender:",padx=2,bg="powder blue")
        self.lblGender.grid(row=9,column=0,sticky =W)
        self.cboGender = ttk.Combobox(LeftFrame, textvariable =Gender, state='readonly', font=('arial', 12, 'bold'),width=18)
        self.cboGender['value'] = ('', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=9, column=1, pady=3, padx=20)
        
        self.lblCheckInDate =Label(LeftFrame,font=('arial',12,'bold'),text="CheckInDate:",padx=2,bg="powder blue")
        self.lblCheckInDate.grid(row=10,column=0,sticky =W)
        self.txtCheckInDate = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CheckInDate,width=20)
        self.txtCheckInDate.grid(row=10,column=1,pady=3, padx=20)
  
        self.lblCheckOutDate =Label(LeftFrame,font=('arial',12,'bold'),text="CheckOutDate:",padx=2,bg="powder blue")
        self.lblCheckOutDate.grid(row=11,column=0,sticky =W)
        self.txtCheckOutDate = Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CheckOutDate,width=20)
        self.txtCheckOutDate.grid(row=11,column=1,pady=3, padx=20)

        
        self.lblMeal =Label(LeftFrame,font=('arial',12,'bold'),text="Meal:",padx=2,bg="powder blue")
        self.lblMeal.grid(row=12,column=0,sticky =W)
        self.cboMeal = ttk.Combobox(LeftFrame, textvariable =Meal, state='readonly', font=('arial', 12, 'bold'),width=18)
        self.cboMeal['value'] = ('', 'Breakfast', 'Lunch', 'Dinner', 'Snacks')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=12, column=1, pady=3, padx=20)
        
        self.lblRoomCategory =Label(LeftFrame,font=('arial',12,'bold'),text="RoomCategory:",padx=2,bg="powder blue")
        self.lblRoomCategory.grid(row=13,column=0,sticky =W)
        self.cboRoomCategory = ttk.Combobox(LeftFrame, textvariable =RoomCategory, state='readonly', font=('arial', 12, 'bold'),width=18)
        self.cboRoomCategory['value'] = ('', 'Single', 'Double', 'Single and Selfcontined', 'Double and SelfContained')
        self.cboRoomCategory.current(0)
        self.cboRoomCategory.grid(row=13, column=1, pady=3, padx=20)

        self.lblRoomNo =Label(LeftFrame,font=('arial',12,'bold'),text="RoomNo:",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=14,column=0,sticky =W)
        self.cboRoomNo = ttk.Combobox(LeftFrame, textvariable =RoomNo, state='readonly', font=('arial', 12, 'bold'),width=18)
        self.cboRoomNo['value'] = ('', '001', '002', '003', '004', '005')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=14, column=1, pady=3, padx=20)

        self.lblModeOfPayment =Label(LeftFrame,font=('arial',12,'bold'),text="ModeOfPayment:",padx=2,bg="powder blue")
        self.lblModeOfPayment.grid(row=15,column=0,sticky =W)
        self.cboModeOfPayment = ttk.Combobox(LeftFrame,textvariable =ModeOfPayment, state='readonly',font=('arial',12,'bold'),width=20)
        self.cboModeOfPayment['value'] = ('', 'Cash', 'Cheque')
        self.cboModeOfPayment.current(0)
        self.cboModeOfPayment.grid(row=15,column=1,pady=3, padx=20)

                
if __name__=='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()

        
