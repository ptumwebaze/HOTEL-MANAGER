import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox


class OOP:
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("silver and gold")
        self.GUI()

    def click_me(self):
        self.action.configure(text = "item has been added-- "+ self.matrial.get()+self.weight.get())

    def quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def msgbox(self):
        answer=mBox.askyesno('','are you satisfied ?  ')
        if answer==True:
            print("+1 satisfied ")
        else:
            print("+1 unsatisfied ")

    def spin(self):
        value= self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT,value+'\n')

    def GUI(self):
        tabcontrol=ttk.Notebook(self.win)

        tab1=ttk.Frame(tabcontrol)
        tabcontrol.add(tab1,text = 'Entry')

        tab2=ttk.Frame(tabcontrol)
        tabcontrol.add(tab2,text = "Storage")

        tab3=ttk.Frame(tabcontrol)
        tabcontrol.add(tab3,text = "customers")

        tab3=tk.Frame(tab3,bg = 'blue')
        tab3.pack()

        tabcontrol.pack(expand = 1,fill = "both")

        safezone=ttk.LabelFrame(tab1,text = 'my comfort zone')
        safezone.grid(column = 0,row = 0)

        mBox.showinfo('',"Running  ")

        ## my safe zone

        storage=ttk.LabelFrame(tab2,text = 'your storage is here')
        storage.grid(column = 0,row = 0)

        for orangecolor in range(2):
            canvas=tk.Canvas(tab3,width = 150,height = 80,highlightthickness = 0,bg = 'orange')
            canvas.grid(row = orangecolor,column = orangecolor)

        menuBar=Menu(self.win)
        self.win.config(menu = menuBar)

        fileMenu=Menu(menuBar,tearoff = 0)
        HelpMenu=Menu(menuBar,tearoff = 0)
        menuBar.add_cascade(label = "File",menu = fileMenu)
        menuBar.add_cascade(label = "Help",menu = HelpMenu)
        HelpMenu.add_command(label = "About",command = self.msgbox)

        fileMenu.add_command(label = "New")
        fileMenu.add_command(label = "Exit",command = quit)
        fileMenu.add_checkbutton(label = "Night Mode")

        labelsFrame=ttk.LabelFrame(storage,text = "made by essam")
        labelsFrame.grid(column = 0,row = 9,padx = 10,pady = 0)


        ttk.Label(safezone,text = "Choose a metal: ").grid(column = 0,row = 0)
        ttk.Label(safezone,text = "type the weight: ").grid(column = 1,row = 0,sticky = 'W')

        weight=tk.StringVar()
        wightEntered=ttk.Entry(safezone,width = 12,textvariable = weight)
        wightEntered.grid(column = 1,row = 1)
        wightEntered.focus()

        matrial=tk.StringVar()
        matrialEntered=ttk.Combobox(safezone,width = 12,textvariable = matrial,state = 'readonly')
        matrialEntered.grid(column = 0,row = 1)
        matrialEntered [ 'values' ]=("Gold","silver")
        matrialEntered.current(0)

        action=ttk.Button(safezone,text = "add ",command = self.click_me)
        action.grid(column = 4,row = 1)

        radVar=tk.IntVar()
        radVar.set(99)
        colors=[ "blue","gold","red" ]

        spin=Spinbox(safezone,values = (1,2,4,42,100),width = 5,borderwidth = 20,
            relief = tk.SUNKEN,command = self.spin)
        spin.grid(column = 2,row = 1)

        scrolW=30
        scrolH=3
        scr=scrolledtext.ScrolledText(safezone,width = scrolW,height = scrolH,wrap = tk.WORD)
        scr.grid(column = 0,columnspan = 5,row = 7)



    #******




oop =OOP()
oop.win.mainloop()
