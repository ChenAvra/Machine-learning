# from image.templatetags import img
from PIL import ImageTk , Image
import PIL.Image

import preProcessing
import model
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename, Label, Button, Entry, IntVar, END, W, E
# from PIL import ImageTk,Image


class OurGUI:
    def __init__(self, master):
        self.master = master
        master.title("countries")
        master.minsize(1200, 600)

        self.filename = None
        self.df = None

        self.e1 = Entry(self.master, width=40)
        self.e1.grid(row=1, column=1)

        master.lableFrame = LabelFrame(master, text="Open a file")
        master.lableFrame.grid(column=0, row=1, padx=20, pady=20)
        master.button = Button(master.lableFrame, text="Browse A File", command=self.fileDialog)
        master.button.grid(column=1, row=1)

        Label(master, text='Number of clusters k').grid(row=2)
        self.e2 = Entry(master, width=40)
        self.e2.grid(row=2, column=1)

        Label(master, text='Number of runs').grid(row=3)
        self.e3 = Entry(master, width=40)
        self.e3.grid(row=3, column=1)
        # lambda: bot_analysis_frame(eventConditionL, eventBreakL)
        master.button = Button(master, text='Pre-process', width=25, command=lambda: self.preProc())
        master.button.grid(column=1, row=4)

        master.button = Button(master, text='Cluster', width=25, command=lambda: self.model())
        master.button.grid(column=3, row=4)

    def fileDialog(self):

        self.filename = filedialog.askopenfilename(initialdir="/", title="Browse a file",
                                                   filetype=(("xlsx", "*jpg"), (" ALL FILES", "*.*")))
        self.e1.insert(0, self.filename)

    def preProc(self):
        if self.filename is None:
            messagebox.showerror("error", "You should enter a valid path file name before pre processing")
        else:
            try:
                self.df = preProcessing.preProcess(self.filename)

                if self.df is not None:
                    messagebox.showinfo("message", "Preprocessing completed successfully!")
                    print(self.df)
            except:
                messagebox.showerror("Error", "error while  the pre processing")



    def model(self):
        try:
            if (int(self.e2.get())) > self.df.shape[0] or (int(self.e2.get()))<3 :
                messagebox.showerror("Ivalid number of clusters", "please enter a valid number of clusters")

            else:
                try:
                    if (int(self.e3.get())) > 50 or (int(self.e3.get())) < 1:
                        messagebox.showerror("Ivalid number of runs", "please enter a valid number of runs")
                    else:
                        try:
                            model.runModel(self.df, int(self.e2.get()), int(self.e3.get()))
                            self.img = ImageTk.PhotoImage(PIL.Image.open("countries.png"))
                            self.panel = Label(self.master, image=self.img)
                            self.panel.grid(row=5, column=1)

                            # canvas = Canvas(self.master, width=300, height=300)
                            # canvas.pack()
                            # img = PhotoImage(file="countries.png")
                            # canvas.create_image(20, 20, anchor=NW, image=img)








                        except:
                            messagebox.showerror("Error", "error while the model")

                except:

                    messagebox.showerror("Ivalid number of runs", "please enter a valid number of runs")




        except:
            messagebox.showerror("Ivalid input of clusters", "please enter a valid number of clusters")



