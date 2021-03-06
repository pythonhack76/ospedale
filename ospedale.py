from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector 

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Sistema di Gestione Hospital")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root, bd=20, relief=RIDGE, text="GESTIONE MANAGER OSPEDALE", fg="red", bg="white", font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP, fill=X)


        # =============================DataFrame==========================================
        Dataframe=Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0,y=130, width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Informazioni Paziente")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12,"bold"),text="Prescrizioni")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # ============================= Buttons frame =====================================

        Buttonframe=Frame(self.root,bd=20, relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        # =============================Details Frame========================================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # =============================DataFrameLeft========================================

        lblNameTablet=Label(DataframeLeft,text="Names of tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)





        

    

root=Tk()
ob=Hospital(root)
root.mainloop()