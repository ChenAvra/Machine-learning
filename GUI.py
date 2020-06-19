import preProcessing
import model
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilename, Label, Button, Entry, IntVar, END, W, E


class OurGUI:

    def __init__(self, master):
        self.master = master
        master.title("countries")
        master.minsize(800, 400)

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
            messagebox.showinfo("error", "You should enter a valid file name before pre processing")
        else:
            self.df = preProcessing.preProcess(self.filename)
            if self.df is not None:
                messagebox.showinfo("message", "Preprocessing completed successfully!")
                print(self.df)
                print(self.e2.get())

    def model(self):
        if int(self.e2.get()) > self.df.shape[0]:
            messagebox.showinfo("Ivalid number of clusters", "please enter a valid number of clusters")
        elif self.e3.get() > 50:
            messagebox.showinfo("Ivalid number of runs", "please enter a valid number of runs")
        else:
            model.runModel(self.df, self.e2, self.e3)
            print()
