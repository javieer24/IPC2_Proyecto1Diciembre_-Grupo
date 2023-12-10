import tkinter as tk
import tkinter
from tkinter import *
import os   # Para poder usar el comando os.system("comando") y abrir la terminal
from tkinter import messagebox
import xml.etree.ElementTree as ET
from tkinter import filedialog



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
        self.ventana = tk.Tk()
        self.ventana.title("[PROYECTO 1 IPC2---GRUPO #---SECCION A]")
        self.ventana .geometry("1100x700")
        self.ventana.configure(bg="#292c37")
        self.ventana.resizable(0,0)

        frame = tkinter.Frame(self.ventana, width=1050, height=570, bg="#2a5384", highlightthickness=10, highlightbackground="#2a5384", relief="ridge", borderwidth=5,)
        frame.place(x=25, y=105)
        frame.config(relief="sunken")

        # Etiquetas para titulos etc
        titulo = tkinter.Label(self.ventana, text="IPCmusic", bg="#292c37", fg="#4BBD43", font=("Gotham-Black", 24)).place(x=450, y=25)
        
        # Label para imagen
        img = tk.PhotoImage(file="iconos\musica.png")
        logo1 = tk.Label(self.ventana, image=img, bg="#292c37").place(x=592, y=10)

        # Boton salir
        img_cerrar = tk.PhotoImage(file="iconos/salir.png")
        btn_cerrar = tk.Button(self.ventana, image=img_cerrar, bg="#292c37", bd=0, command=self.cerrar_aplicacion)
        btn_cerrar.place(x=10, y=10)

        # Botón con imagen para minimizar la ventana
        img_minimizar = tk.PhotoImage(file="iconos/borrar.png")
        btn_minimizar = tk.Button(self.ventana, image=img_minimizar, bg="#292c37", bd=0, command=self.minimizar_ventana)
        btn_minimizar.place(x=60, y=10)


        # Para que sea visible todo lo que realizamos
        self.ventana.mainloop()