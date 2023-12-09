import tkinter as tk
from tkinter import *



class App():

# Aqui iran las demas ventas 


# Funciones

    def cerrar_aplicacion(self):
        self.ventana.destroy()

    def minimizar_ventana(self):
        self.ventana.iconify()

# Constructor
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("'[PROYECTO 1 IPC2]")
        self.ventana .geometry("1000x700")
        self.ventana.configure(bg="#292c37")
        self.ventana.resizable(0,0)

        canvas = Canvas(self.ventana, width=900, height=550, bg="#2a5384", highlightthickness=10, highlightbackground="#2a5384", relief="ridge", borderwidth=0)
        canvas.place(x=30, y=90)

        # Etiquetas para titulos etc
        titulo = tk.Label(self.ventana, text="IPCmusic", bg="#292c37", fg="#4BBD43", font=("Gotham-Black", 24)).place(x=400, y=20)
        
        # Label para imagen
        img = tk.PhotoImage(file="iconos\musica.png")
        logo1 = tk.Label(self.ventana, image=img, bg="#292c37").place(x=600, y=10)

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