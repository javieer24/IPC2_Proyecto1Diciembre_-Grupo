import os
from objects import *
from tkinter import *
from tkinter.constants import *
from method import *
from objects.objects import *
from objects.objects import ListaDoble, ListaCircular
from objects import *
from thread.thread import *
from tkinter import Image, Tk, Button, Label, Label, ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
import tkinter.font as TFont
from PIL import ImageTk
from PIL import Image
from method.readxml import XMLReader






    
     

class App(Tk):

# Funciones

    def cerrar_aplicacion(self):
        salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
        if salir == "yes":
         self.ventana.quit()
         self.ventana.destroy()

    def minimizar_ventana(self):
        self.ventana.iconify()

    
    def addArbol(self):
        columns = ("cancion", "album", "artista")
        self.tabla = ttk.Treeview(self.ventana, columns = columns, show = "headings")
        self.tabla.heading('cancion',text = "Canción")
        self.tabla.heading('album', text = "Album")
        self.tabla.heading('artista', text = "Artista")
        self.tabla.column('cancion', width = 150)
        self.tabla.column('album', width = 150)
        self.tabla.column('artista', width = 150)
        scrollbar = ttk.Scrollbar(self.ventana, orient = VERTICAL, command = self.tabla.yview)
        self.tabla.configure(yscrollcommand = scrollbar.set)
        scrollbar.place(x= 810, y = 155, width = 20, height = 300)
        self.tabla.place(x = 375, y = 155, width = 450, height = 300)
    
    def addPlayList(self):
        self.entryPlaylist = EntryPlaceholder("Nombre de Playlist", self.ventana, color = "#333")
        self.entryPlaylist.config(justify = CENTER)
        columns2 = ("lista")
        self.tablePlaylist = ttk.Treeview(self.ventana, columns =  columns2, show = "headings")
        texto = self.entryPlaylist.get()
        self.tablePlaylist.heading("lista", text = texto)
        scrollbar2 = ttk.Scrollbar(self.ventana, orient = VERTICAL, command = self.tablePlaylist.yview)
        self.tablePlaylist.configure(yscrollcommand = scrollbar2.set)
        scrollbar2.place(x = 1280, y = 155, width = 20, height = 400)
        self.entryPlaylist.place(x = 980, y = 125, width = 300, height = 30)
        self.tablePlaylist.place(x = 980, y = 155, width = 300, height = 400)
        self.playList = ListaCircular()
    
    def cargarXML(self):
        lector = XMLReader()
        self.library = lector.analyze()
        self.songslist = self.library.toList()
        self.setArtistas()
    
    def setArtistas(self):
        Artistas = self.library.getArtistas()
        self.cbbArtistas["values"] = Artistas
        self.cbbArtistas.current(0)
        self.change_artist(None)
        
    def change_artist(self, event):
        self.setAlbumes()
        
    def setAlbumes(self):
        artista = self.cbbArtistas.current()
        artista = self.library.listaArtistas.getById(artista)
        self.cbbAlbumbes["values"] = artista.getAlbumes()
        self.cbbAlbumbes.current(0)
        self.setCanciones()
        
    def change_album(self, event):
        self.setCanciones()
        
    def setCanciones(self):
        self.addArbol()
        self.songslist = self.library.listaArtistas.getById(
            self.cbbArtistas.current()).listaAlbumes.getById(
                self.cbbAlbumbes.current()).getCanciones()
        for i in range(self.songslist.length):
            song = self.songslist.getById(i)
            row = ("{}".format(song.nombre),"{}".format(song.album),"{}".format(song.artista))
            self.tabla.insert('', END, values = row, iid = i)
        child_id = self.tabla.get_children()[0]
        self.tabla.focus(child_id)
        self.tabla.selection_set(child_id)     
    
    def addToList(self):
        self.tablePlaylist.heading("lista", text = self.entryPlaylist.get())
        if self.songslist.length > 0:
            song = self.songslist.getById(int(self.tabla.focus()))
            self.playList.append(song)
            row = ("{}".format(song.nombre), "{}".format(song.album), "{}".format(song.artista))
            self.tablePlaylist.insert('', END, values = row, iid = self.playList.length-1)
    
    def play(self):
        if self.playList.length > 0:
            self.actualPlaylist = self.playList.head
            self.setInfo(self.actualPlaylist.value.nombre, self.actualPlaylist.value.album, self.actualPlaylist.value.artista)
            self.setPhoto(self.actualPlaylist)
            self.reproducir(self.actualPlaylist.value)
        elif self.songslist.length > 0 and self.playList.length == 0:
            for i in range(self.songslist.length):
                song = self.songslist.getById(i)
                self.playList.append(song)
                row = ("{}".format(song.nombre), "{}".format(song.album), "{}".format(song.artista))
                self.tablePlaylist.insert('', END, values = row, iid = i)
                self.play()    
    
    def aNext(self):
        if self.playList.length > 0:
            self.actualPlaylist = self.next(self.actualPlaylist)
            self.tablePlaylist.focus(self.actualPlaylist.id)
            self.tablePlaylist.selection_set(self.actualPlaylist.id)
            self.reproducir(self.actualPlaylist.value)
    
    def aBack(self):
        if self.playList.length > 0:
            self.actualPlaylist = self.back(self.actualPlaylist)
            self.tablePlaylist.focus(self.actualPlaylist.id)
            self.tablePlaylist.selection_set(self.actualPlaylist.id)
            self.reproducir(self.actualPlaylist.value)
    
    def next(self, nodo):
        aux = nodo.siguiente
        self.setInfo(aux.value.nombre, aux.value.album, aux.value.artista)
        self.setPhoto(aux)
        return aux
    
    def back(self, nodo):
        aux = nodo.anterior
        self.setInfo(aux.value.nombre, aux.value.album, aux.value.artista)
        self.setPhoto(aux)
        return aux
    
    def setPhoto(self, nodo):
        try:
            self.img1 = Image.open(nodo.value.imagen)
            self.img1 = self.img1.resize((360,350), Image.BILINEAR)
            self.photoImg1 = ImageTk.PhotoImage(self.img1)
            self.lbl = Label(self.foto, image = self.photoImg1)
            self.lbl.place(x = 0,y = 0, width = 360, height = 350)
        except FileNotFoundError:
            print(FileNotFoundError)
    
    def setInfo(self, nombre, album, artista):
        self.labelCancion.config(text = "Canción {}".format(nombre))
        self.labelAlbum.config(text = "Album: {}".format(album))
        self.labelArtista.config(text = "Artista: {}".format(artista))
    
    def reproducir(self, cancion):
        if self.threadPlay != None:
            self.threadPlay.raise_exception()
            self.threadPlay.join()
        self.threadPlay = TPlay(cancion.ruta)
        self.threadPlay.start()
    
    def pause(self):
        if self.threadPlay != None:
            if self.threadPlay.estado != "p":
                self.threadPlay.estado = "p"
            else:
                self.threadPlay.estado = "r"
    
    def stop(self):
        if self.threadPlay != None:
            self.threadPlay.estado = "e"
        
    def saveList(self):
        self.playList.nombre = self.entryPlaylist.get()
        aux = self.playList
        self.playList = None
        contenedor = self.listaPlayList.contains(aux.nombre)
        print("Contenedor: {}".format(contenedor))
        if contenedor == None:
            self.listaPlayList.append(aux)
            valores = []
            for i in range(self.listaPlayList.length):
                valores.append(self.listaPlayList.getById(i).nombre)
                self.cbbListas["values"] = valores
        else:
            messagebox.showwarning(title = "Alerta!!!", message = "Ya existe una lista de reproducción con este nombre")
        self.addPlayList()
    
    def __init__(self):
        Tk.__init__(self)
        x_ = self.winfo_screenwidth()//2-1360//2
        y_ = self.winfo_screenheight()//2-700//2
        self.resizable(0,0)
        self.geometry("1360x700+{}+{}".format(x_,y_))
        self.title("IPCmusic---Proyecto 1----Grupo #")
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
        

        #FOTO
        self.foto = Frame(frame)
        self.foto.place(x = 20, y = 35, width = 300, height = 300)
        #Playlist
        self.addPlayList()
        #Arbol
        self.addArbol()
        
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Labels ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Etiquetas para titulos etc
        titulo = Label(self.ventana, text="IPCmusic", bg="#082032", fg="#4BBD43", font=("Gotham-Black", 24)).place(x=560, y=25)
        
        # Label para Imagen Logo
        img = PhotoImage(file="iconos\musica.png")
        logo1 = Label(self.ventana, image=img, bg="#082032").place(x=700, y=10)
        
        Label0 = Label(self.ventana, text="Load XML", bg="#082032", fg="white", font=("Gotham-Black", 6)).place(x=23, y=42)
        
        labelCancion = Label(frame, text="Canción:")
        labelCancion.config(fg="white", bg="#2a5384", font=("Gotham-Black 14 bold"))
        labelCancion.place(x=16,y=431)
        
        labelAlbum = Label(frame, text="Album:")
        labelAlbum.config(fg="white", bg="#2a5384", font=("Gotham-Black 14 bold"))
        labelAlbum.place(x=16,y=469)
        
        labelArtista = Label(frame, text="Artista:")
        labelArtista.config(fg="white", bg="#2a5384", font=("Gotham-Black 14 bold"))
        labelArtista.place(x=16,y=505)
 
 
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Buttons ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Boton salir
        img_cerrar = PhotoImage(file="iconos/salir.png")
        btn_cerrar = Button(self.ventana, image=img_cerrar, bg="#082032", bd=0, command=self.cerrar_aplicacion)
        btn_cerrar.place(x=10, y=10)

        # Botón con imagen para minimizar la ventana
        img_minimizar = PhotoImage(file="iconos/borrar.png")
        btn_minimizar = Button(self.ventana, image=img_minimizar, bg="#082032", bd=0, command=self.minimizar_ventana)
        btn_minimizar.place(x=60, y=10)


        img_load = PhotoImage(file="iconos/load.png")
        btn_load = Button(self.ventana, image=img_load, bg="#082032", bd=0, command = self.cargarXML)
        btn_load.place(x=22, y=55)
        
        
        
        
        
        
        #COMBOBOX
        self.cbbArtistas = ttk.Combobox(self.ventana, state = "readonly")
        self.cbbAlbumbes = ttk.Combobox(self.ventana, state = "readonly")
        self.cbbListas = ttk.Combobox(self.ventana, state = "readonly")
        self.cbbArtistas.bind("<<ComboboxSelected>>", self.change_artist)
        self.cbbAlbumbes.bind("<<ComboboxSelected>>", self.change_album)
        self.cbbArtistas.place(x = 855, y = 170, width = 120)
        self.cbbAlbumbes.place(x = 855, y = 210, width = 120)
        self.cbbListas.place(x = 855, y = 250, width = 120)
        
        # Para que sea visible todo lo que realizamos
        self.ventana.mainloop()
    
    


    
            