import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Page1, Page2,Page3):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame(Page1)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def qf(quickPrint):
    print(quickPrint)

        
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="welcome", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda:controller.show_frame(Page2))
        button2.pack()

        button3 = tk.Button(self, text="Visit Page 3",
                            command=lambda:controller.show_frame(Page3))
        button3.pack()

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="karibu mini 2 a", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda:controller.show_frame(Page1) )
        button.pack()
        
        button3 = tk.Button(self, text="Visit Page 3",
                            command=lambda:controller.show_frame(Page3))
        button3.pack()


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Uko kwenye Tatu sasa", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda:controller.show_frame(Page1) )
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda:controller.show_frame(Page2))
        button2.pack()



app = SeaofBTCapp()
app.mainloop()
