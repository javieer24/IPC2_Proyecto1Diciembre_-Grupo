import tkinter as tk
import tkinter
from tkinter import *
import os   # Para poder usar el comando os.system("comando") y abrir la terminal
from tkinter import messagebox
import xml.etree.ElementTree as ET
from tkinter import filedialog


def search():
    val = filedialog.askopenfilename(title ='Seleccion de archivo xml',initialdir = './', filetypes=(('xml files', '*.xml'),('all files','*.*')))
    loadXML(val)


def loadXML():
    contenido = open(ruta).read()
    biblioteca = ET.fromstring(contenido)
    for biblio in biblioteca.iter("biblioteca"):
        for can in biblio.iter("cancion"):
            nombre = can.attrib['nombre']
            album = ""
            artista = ""
            imagen = ""
            ruta = ""
            for ar in can.iter("artista"):
                artista += ar.text  
            for al in can.iter("album"):
                album += al.text  
            for im in can.iter("imagen"):
                imagen += im.text 
            for ru in can.iter("ruta"):
                ruta += ru.text   
    
    
     

class App():

# Aqui iran las demas ventas 




# Funciones

    def cerrar_aplicacion(self):
        salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
        if salir == "yes":
         self.ventana.quit()
         self.ventana.destroy()

    def minimizar_ventana(self):
        self.ventana.iconify()

# Constructor
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("'[PROYECTO 1 IPC2]")
        self.ventana .geometry("1100x700")
        self.ventana.configure(bg="#292c37")
        self.ventana.resizable(0,0)
        
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Frames ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        # Frame menu
        frame = tkinter.Frame(self.ventana, width=1050, height=570, bg="#2a5384", highlightthickness=10, highlightbackground="#2a5384", relief="ridge", borderwidth=5)
        frame.place(x=25, y=105)
        frame.config(relief="groove")
        
        #Framme showinfo
        frameInfo = tkinter.Frame(frame, width=580,height=300, bg="#294362", highlightthickness=10,highlightbackground="#2a5384", relief="ridge", borderwidth=5)
        frameInfo.place(x=410, y=150)
        frame.config(relief="sunken")
        
        # Frame search
        frameSearch = tkinter.Frame(self.ventana, width=300,height=60, bg="#294362", highlightthickness=10,highlightbackground="#2a5384", relief="ridge", borderwidth=5)
        frameSearch.place(x=775, y=10)
        frame.config(relief="sunken")

        # Frame img
        frameImg = tkinter.Frame(frame, width=400,height=500, bg="#294362", highlightthickness=10,highlightbackground="#2a5384", relief="ridge", borderwidth=5)
        frameImg.place(x=15, y=30)
        frame.config(relief="sunken")


        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Labels ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Etiquetas para titulos etc
        titulo = tkinter.Label(self.ventana, text="IPCmusic", bg="#292c37", fg="#4BBD43", font=("Gotham-Black", 24)).place(x=450, y=25)
        
        # Label para Imagen Logo
        img = tkinter.PhotoImage(file="iconos\musica.png")
        logo1 = tkinter.Label(self.ventana, image=img, bg="#292c37").place(x=592, y=10)
        
        Label1 = tkinter.Label(frameInfo, text="Canción:")
        Label1.config(fg="white", bg="#294362", font=("Gotham-Black 18 bold"))
        Label1.place(x=20,y=50)

        CANCION = "VALOR"

        Label1A = tkinter.Label(frameInfo, text=CANCION)
        Label1A.config(fg="white", bg="#294362", font=("Gotham-Black 14"))
        Label1A.place(x=155,y=50)

        Label2 = tkinter.Label(frameInfo, text="Artista:")
        Label2.config(fg="white", bg="#294362", font=("Gotham-Black 18 bold"))
        Label2.place(x=20,y=110)

        ARTISTA = "VALOR2"

        Label2A = tkinter.Label(frameInfo, text=ARTISTA)
        Label2A.config(fg="white", bg="#294362", font=("Gotham-Black 14"))
        Label2A.place(x=155,y=115)

        Label3 = tkinter.Label(frameInfo, text="Álbum:")
        Label3.config(fg="white", bg="#294362", font=("Gotham-Black 18 bold"))
        Label3.place(x=20,y=175)

        ALBUM = "VALOR3"

        Label3A = tkinter.Label(frameInfo, text=ALBUM)
        Label3A.config(fg="white", bg="#294362", font=("Gotham-Black 14"))
        Label3A.place(x=155,y=180)
        

        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Buttons ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        def hello():
            print("Hello")

        # Boton salir
        img_cerrar = tkinter.PhotoImage(file="iconos/salir.png")
        btn_cerrar = tkinter.Button(self.ventana, image=img_cerrar, bg="#292c37", bd=0, command=self.cerrar_aplicacion)
        btn_cerrar.place(x=10, y=10)

        # Botón con imagen para minimizar la ventana
        img_minimizar = tkinter.PhotoImage(file="iconos/borrar.png")
        btn_minimizar = tkinter.Button(self.ventana, image=img_minimizar, bg="#292c37", bd=0, command=self.minimizar_ventana)
        btn_minimizar.place(x=60, y=10)

        # Boton cargar
        img_load = tkinter.PhotoImage(file="iconos/Load.png")
        buttonload = tkinter.Button(self.ventana,image=img_load,  bg="#292c37", bd=0, command=search)
        buttonload.place(x=22, y=55)

        # Boton detener
        
        # Boton play

        # Boton siguiente
        
        # Boton anterior
        
        # Boton aleatorio
        
        # Boton pausa
        
        # Boton repetir

        # Boton buscar
        search2 = tkinter.StringVar()
        txtA = tkinter.Entry(frameSearch , textvariable=search2)
        txtA.place(x=3,y=2)
        txtA.config(width=43)

        def pn(valor):
            print(valor)

        img13 = tkinter.PhotoImage(file="iconos/search.png")
        img_Label9 = tkinter.Label(image=img13)
        button12 = tkinter.Button(self.ventana, image=img13, command = pn(search2.get()), borderwidth=0, bg="white")
        button12.place(x=740, y=23)
        button12.config(width=30, height=30)

        # Para que sea visible todo lo que realizamos
        self.ventana.mainloop()
    
    
