import os

from tkinter import *
from tkinter.constants import *
from method import *
from objects.objects import ListaCircular, ListaDoble, EntryPlaceholder
from objects.library import Library
from objects.objects import *
from thread.thread import *
from tkinter import Image, Tk, Button, Label, Label, ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
import tkinter.font as TFont
from PIL import ImageTk
from PIL import Image
from method.readxml import XMLReader





def search():
    val = filedialog.askopenfilename(title ='Seleccion de archivo xml',initialdir = './', filetypes=(('xml files', '*.xml'),('all files','*.*')))
    XMLReader(val)
    
     

class App(Tk):

# Funciones

    def cerrar_aplicacion(self):
        salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
        if salir == "yes":
         self.ventana.quit()
         self.ventana.destroy()

    def minimizar_ventana(self):
        self.ventana.iconify()
        
        
    
    def __init__(self):
        Tk.__init__(self)
        x_ = self.winfo_screenwidth()//2-1360//2
        y_ = self.winfo_screenheight()//2-700//2
        self.resizable(0,0)
        self.geometry("1360x700+{}+{}".format(x_,y_))
        self.title("NOZC Media Player")
        self.library = None
        self.songslist = ListaDoble()
        self.playList = ListaCircular()
        self.actualPlaylist = None
        self.threadPlay = None
        self.listaPlayList = ListaDoble()
        self.initComponent()

# Constructor
    def initComponent(self):
        self.ventana = Frame(self, background = "#082032")
        self.ventana.place(x = 0, y = 0, width = 1360, height = 700)

        
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Frames ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        # Frame menu
        frame = Frame(self.ventana, width=1310, height=570, bg="#2a5384", highlightthickness=10, highlightbackground="#2a5384", relief="ridge", borderwidth=5)
        frame.place(x=25, y=105)
        frame.config(relief="groove")
        



        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Labels ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Etiquetas para titulos etc
        titulo = Label(self.ventana, text="IPCmusic", bg="#082032", fg="#4BBD43", font=("Gotham-Black", 24)).place(x=560, y=25)
        
        # Label para Imagen Logo
        img = PhotoImage(file="iconos\musica.png")
        logo1 = Label(self.ventana, image=img, bg="#082032").place(x=700, y=10)
        
 
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Buttons ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Boton salir
        img_cerrar = PhotoImage(file="iconos/salir.png")
        btn_cerrar = Button(self.ventana, image=img_cerrar, bg="#292c37", bd=0, command=self.cerrar_aplicacion)
        btn_cerrar.place(x=10, y=10)

        # Botón con imagen para minimizar la ventana
        img_minimizar = PhotoImage(file="iconos/borrar.png")
        btn_minimizar = Button(self.ventana, image=img_minimizar, bg="#292c37", bd=0, command=self.minimizar_ventana)
        btn_minimizar.place(x=60, y=10)


        # Para que sea visible todo lo que realizamos
        self.ventana.mainloop()
    
    


    
            