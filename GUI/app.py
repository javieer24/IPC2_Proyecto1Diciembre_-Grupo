import os
from objects import *
from tkinter import *
from tkinter.constants import *
from method import *
from objects.objects import *
from objects.objects import ListaDoble, ListaCircular, Pila
from objects import *
from thread.thread import *
from tkinter import Image, Tk, Button, Label, Label, ttk, filedialog, messagebox, simpledialog
import xml.etree.ElementTree as ET
import tkinter.font as TFont
from PIL import ImageTk
from PIL import Image
from method.readxml import XMLReader
import random

class App(Tk):

# Funciones

    def cerrar_aplicacion(self):
        salir = messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
        if salir == "yes":
         self.ventana.quit()
         self.ventana.destroy()

    def minimizar_ventana(self):
        self.ventana.iconify()
        
    def cargarListasDeReproduccion(self, path):
        try:
            tree = ET.parse(path)
            root = tree.getroot()

            for listaXML in root.findall('Lista'):
                nombreLista = listaXML.get('nombre')
                print(f"Cargando lista: {nombreLista}")  # Depuración

                nuevaLista = ListaCircular()
                nuevaLista.nombre = nombreLista

                for cancionXML in listaXML.findall('cancion'):
                    nombre_cancion = cancionXML.get("nombre")
                    artista = cancionXML.find("artista").text
                    album = cancionXML.find("album").text
                    ruta = cancionXML.find("ruta").text
                    imagen = cancionXML.find("imagen").text

                    cancion = Cancion(nombre_cancion, album, artista, ruta, imagen)
                    nuevaLista.append(cancion)
                    print(f"Añadiendo canción: {nombre_cancion}, Artista: {artista}, Album: {album}")  # Depuración 

                self.listaPlayList.append(nuevaLista)
                print(f"Lista añadida: {nuevaLista}")  # Depuración 

        except Exception as e:
            print("Error al cargar las listas de reproducción:", e)

    def seleccionar_y_mostrar_lista(self):
        nombre_archivo = filedialog.askopenfilename(initialdir="MisListas", title="Seleccione un archivo XML", filetypes=[("XML files", "*.xml")])
        if nombre_archivo:
            self.cargarListasDeReproduccion(nombre_archivo)
            self.mostrar_lista(nombre_archivo)

    def actualizar_vista_playlist(self):
        nombre_lista = self.cbbListas.get()
        if nombre_lista:
            self.MisListas(nombre_lista)

    def on_lista_seleccionada(self, event):
        self.actualizar_vista_playlist()
    
    def mostrar_lista(self, archivo_xml):
        try:
            tree = ET.parse(archivo_xml)
            root = tree.getroot()

                        # Iterar sobre las listas de reproducción y canciones
            for lista in root.findall(".//Lista"):
                lista_nombre = lista.get("nombre")

                for cancion_elem in lista.findall(".//cancion"):
                    cancion_nombre = cancion_elem.get("nombre")
                    artista = cancion_elem.find("artista").text
                    album = cancion_elem.find("album").text
                    veces_reproducida = cancion_elem.find("vecesReproducida").text
                    imagen = cancion_elem.find("imagen").text
                    ruta = cancion_elem.find("ruta").text

                    # Agregar la canción a la tabla de canciones ------- Esto no me sirve jeje
                    #row = (cancion_nombre, album, artista)
                    #self.tabla.insert("", END, values=row)

                    # Agregar la canción a la lista de reproducción por defecto
                    row_playlist = (cancion_nombre, album, artista)
                    self.tablePlaylist.insert('', END, values = row_playlist)
        except FileNotFoundError:
            print("Archivo XML no encontrado.")
    
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
        self.tabla.bind('<<TreeviewSelect>>', self.onCancionSeleccionada)
    
    def reproducir_Lista(self):
        print("Intentando reproducir la lista...")
        nombre_lista = self.cbbListas.get()
        print("Nombre de la lista seleccionada:", nombre_lista)

        # Buscar la lista por nombre
        for lista in self.listaPlayList:
            if lista.nombre == nombre_lista:
                # Lista encontrada
                current_lista = lista
                print("Lista actual:", current_lista)

                if current_lista.length > 0:
                    # Seleccionar la primera canción de la lista para empezar la reproducción
                    self.actualPlaylist = current_lista.head
                    self.reproducir(self.actualPlaylist.value)
                    return
                else:
                    print("La lista está vacía.")
                    return
        print("Lista no encontrada.")
  
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
            if self.modo_reproduccion_actual == "Normal":
                self.actualPlaylist = self.next(self.actualPlaylist)
            elif self.modo_reproduccion_actual == "Aleatorio":
                indice_aleatorio = random.randint(0, self.playList.length - 1)
                self.actualPlaylist = self.playList.getById(indice_aleatorio)

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

    # PARA QUE FUNQUE EL BOTON CON DOBLE FUNCION DE PAUSA Y PLAY
    def togglePlayPause(self):
        if self.threadPlay is None:
            return  # No hay música para reproducir o pausar

        if self.threadPlay.estado == "p":  # Si está pausado, reproducir
            self.threadPlay.estado = "r"
        else:  # Si está reproduciendo, pausar
            self.threadPlay.estado = "p"
            
    def agregar_cancion_a_lista(self):
        if self.cancionSeleccionada is None:
            messagebox.showinfo("Error", "No hay canción seleccionada.")
            return

        nombre_lista = self.cbbListas.get()
        if not nombre_lista:
            messagebox.showinfo("Error", "No hay lista seleccionada.")
            return

        archivo_xml = os.path.join("MisListas", nombre_lista + ".xml")
        if not os.path.exists(archivo_xml):
            messagebox.showinfo("Error", "Archivo de lista no encontrado.")
            return

        cancion = self.cancionSeleccionada
        cancion.vecesReproducida += 1  # Aumentar el contador de reproducciones

        tree = ET.parse(archivo_xml)
        root = tree.getroot()
        lista = root.find(f".//Lista[@nombre='{nombre_lista}']")

        # Verificar si la canción ya existe en la lista
        elemento_cancion = lista.find(f".//cancion[@nombre='{cancion.nombre}']")
        if elemento_cancion is not None:
            elemento_cancion.find("vecesReproducida").text = str(cancion.vecesReproducida)
        else:
            # Añadir nueva canción a la lista
            nueva_cancion = ET.SubElement(lista, "cancion", nombre=cancion.nombre)
            ET.SubElement(nueva_cancion, "artista").text = cancion.artista
            ET.SubElement(nueva_cancion, "album").text = cancion.album
            ET.SubElement(nueva_cancion, "vecesReproducida").text = str(cancion.vecesReproducida)
            ET.SubElement(nueva_cancion, "imagen").text = cancion.imagen
            ET.SubElement(nueva_cancion, "ruta").text = cancion.ruta

        tree.write(archivo_xml)
      
    
    def setInfo(self, nombre, album, artista):
        self.labelCancion.config(text = "Canción {}".format(nombre))
        self.labelAlbum.config(text = "Album: {}".format(album))
        self.labelArtista.config(text = "Artista: {}".format(artista))
    
    def reproducir(self, cancion):
        self.setInfo(cancion.nombre, cancion.album, cancion.artista)
        cancion.incrementar_reproducciones()
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
            
    def reportes(self):
        if self.library != None:
            self.library.report()
        else:
            messagebox.showerror(message = "No se ha cargado ninguna biblioteca", title = "Error")
            
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

    def MisListas(self, nombre_lista=None):
        if nombre_lista is None:
            # Puedes elegir mostrar una lista predeterminada o simplemente no hacer nada
            return

        archivo_xml = os.path.join("MisListas", nombre_lista + ".xml")
        if not os.path.exists(archivo_xml):
            print(f"Archivo no encontrado: {archivo_xml}")
            return

        self.tablePlaylist.delete(*self.tablePlaylist.get_children())  # Limpiar la tabla actual

        try:
            # Parsear el archivo XML
            tree = ET.parse(archivo_xml)
            root = tree.getroot()

            # Iterar sobre las listas de reproducción y canciones
            for lista in root.findall(".//Lista"):
                for cancion_elem in lista.findall(".//cancion"):
                    cancion_nombre = cancion_elem.get("nombre")
                    artista = cancion_elem.find("artista").text
                    album = cancion_elem.find("album").text
                    veces_reproducida = cancion_elem.find("vecesReproducida").text
                    imagen = cancion_elem.find("imagen").text
                    ruta = cancion_elem.find("ruta").text

                    # Agregar la canción a la lista de reproducción
                    row_playlist = (cancion_nombre, album, artista)
                    self.tablePlaylist.insert('', END, values=row_playlist)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo_xml}")
    

        
    # ------- Metodos para listas de reproduccion --------

    def crear_listaReproduccion(self):
        nombre_lista = simpledialog.askstring("Crear una lista de Reproducción", "Nombre de la Lista: ")
        if nombre_lista:
            if not self.listaPlayList.contains(nombre_lista):
                nueva_Lista = ListaCircular()
                nueva_Lista.nombre = nombre_lista
                self.listaPlayList.append(nueva_Lista)

                # Crear un nuevo archivo XML con el nombre de la lista
                self.crear_archivo_xml_para_lista(nombre_lista + ".xml", nombre_lista)

                # Almacenar el nombre de la última lista creada
                self.ultimaListaCreada = nombre_lista

                # Actualizar el combobox de listas después de crear la nueva lista
                self.actualizar_lista_combobox()
                self.cbbListas.current(len(self.listaPlayList) - 1)
            else:
                messagebox.showwarning("Error", "Ese nombre ya existe!")


    def crear_archivo_xml_para_lista(self, nombre_archivo, nombre_lista):
        archivo_xml = os.path.join("MisListas", nombre_archivo)
        root = ET.Element("ListasReproduccion")
        ET.SubElement(root, "Lista", nombre=nombre_lista)
        tree = ET.ElementTree(root)
        tree.write(archivo_xml)
    
    def actualizar_lista_combobox(self):
        self.cbbListas["values"] = [archivo.replace(".xml", "") for archivo in os.listdir("MisListas") if archivo.endswith(".xml")]

    def reproducirSeleccionada(self):
        if self.cancionSeleccionada:
            self.reproducir(self.cancionSeleccionada)
        else:
            print("No hay ninguna canción seleccionada")

    def modo_reproduccion(self, modo):
        if modo == "Normal":
            self.modo_reproduccion_actual = "Normal"
        elif modo == "Aleatorio":
            self.modo_reproduccion_actual = "Aleatorio"
    

    def onCancionSeleccionada(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            item = self.tabla.item(seleccion)
            valores_seleccionados = item['values']

            # Buscar la canción correspondiente en self.songslist
            for cancion in self.songslist:
                if cancion.nombre == valores_seleccionados[0] and cancion.album == valores_seleccionados[1] and cancion.artista == valores_seleccionados[2]:
                    self.cancionSeleccionada = cancion
                    break
            else:
                self.cancionSeleccionada = None
                print("Canción no encontrada en la lista.")

    def generar_reporte_html(self):
        # Obtener el nombre de la última lista creada
        nombre_lista = self.ultimaListaCreada if hasattr(self, 'ultimaListaCreada') else 'Sin Nombre'

        # Inicializar la Pila
        pila_canciones = Pila()

        # Agregar canciones a la Pila
        for i in range(self.songslist.length):
            cancion = self.songslist.getById(i)
            pila_canciones.push(cancion)

        # Crear el archivo HTML
        with open("reporte_canciones.html", "w") as file:
            file.write("<html><head><title>Reporte de Canciones</title>")
            file.write("<style>table { width: 100%; border-collapse: collapse; }")
            file.write("th, td { border: 1px solid black; padding: 8px; text-align: left; }")
            file.write("th { background-color: #f2f2f2; }</style></head><body>")
            file.write(f"<h1>Canciones Más Reproducidas - Lista: {nombre_lista}</h1>")
            file.write("<table><tr><th>Canción</th><th>Artista</th><th>Álbum</th><th>Reproducciones</th></tr>")

            # Extraer elementos de la pila y agregarlos al reporte HTML
            while not pila_canciones.is_empty():
                cancion = pila_canciones.pop()
                file.write(f"<tr><td>{cancion.nombre}</td><td>{cancion.artista}</td><td>{cancion.album}</td><td>{cancion.vecesReproducida}</td></tr>")

            file.write("</table></body></html>")
            print("Reporte HTML generado en 'reporte_canciones.html'")

    
    def __init__(self):
        Tk.__init__(self)
        x_ = self.winfo_screenwidth()//2-1360//2
        y_ = self.winfo_screenheight()//2-700//2
        self.resizable(0,0)
        self.geometry("1360x700+{}+{}".format(x_,y_))
        self.title("IPCmusic-----Grupo#8-----")
        self.library = None
        self.songslist = ListaDoble()
        self.playList = ListaCircular()
        self.actualPlaylist = None
        self.threadPlay = None
        self.listaPlayList = ListaDoble()
        self.initComponent()
        self.cancionSeleccionada = None
        self.modo_reproduccion_actual = "Normal"

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
        #Aca agrego las canciones del xml de listas 
        self.MisListas()

        #Arbol
        self.addArbol()
        
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Labels ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Etiquetas para titulos etc
        titulo = Label(self.ventana, text="IPCmusic", bg="#082032", fg="#4BBD43", font=("Gotham-Black", 24)).place(x=560, y=25)
        
        # Label para Imagen Logo
        img = PhotoImage(file="iconos//musica.png")
        logo1 = Label(self.ventana, image=img, bg="#082032").place(x=700, y=10)
        
        Label0 = Label(self.ventana, text="Load XML", bg="#082032", fg="white", font=("Gotham-Black", 6)).place(x=23, y=42)
        
        self.labelCancion = Label(frame, text="Canción:")
        self.labelCancion.config(fg="white", bg="#2a5384", font=("Gotham-Black 14 bold"))
        self.labelCancion.place(x=16,y=431)

        self.labelAlbum = Label(frame, text="Album:")
        self.labelAlbum.config(fg="white", bg="#2a5384", font=("Gotham-Black 14 bold"))
        self.labelAlbum.place(x=16,y=469)

        self.labelArtista = Label(frame, text="Artista:")
        self.labelArtista.config(fg="white", bg="#2a5384", font=("Gotham-Black 14 bold"))
        self.labelArtista.place(x=16,y=505)
 
 
        #-----------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------ Buttons ---------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        # Boton salir
        img_cerrar = PhotoImage(file="iconos//salir.png")
        btn_cerrar = Button(self.ventana, image=img_cerrar, bg="#082032", bd=0, command=self.cerrar_aplicacion)
        btn_cerrar.place(x=10, y=10)

        # Botón con imagen para minimizar la ventana
        img_minimizar = PhotoImage(file="iconos//borrar.png")
        btn_minimizar = Button(self.ventana, image=img_minimizar, bg="#082032", bd=0, command=self.minimizar_ventana)
        btn_minimizar.place(x=60, y=10)


        img_load = PhotoImage(file="iconos//Load.png")
        btn_load = Button(self.ventana, image=img_load, bg="#082032", bd=0, command = self.cargarXML)
        btn_load.place(x=22, y=55)

        #Botón para reportes
        btn_reportes = Button(self.ventana, text = "Graphviz", command = self.reportes)
        btn_reportes.place(x=75, y=70, width = 85, height = 25)

        # REPORTE HTML
        btn_generar_reporte = Button(self.ventana, text = "Generar Reporte HTML", command = self.generar_reporte_html)
        btn_generar_reporte.place(x=170, y=70, width = 155, height = 25)

        btn_crear_lista = Button(frame, text="Crear Lista", command=self.crear_listaReproduccion)
        btn_crear_lista.place(x=840, y=218)
        
        btn_crear_lista = Button(frame, text="Agregar Lista", command=self.agregar_cancion_a_lista)
        btn_crear_lista.place(x=834, y=276)
        
        btn_reproducir = Button(frame, text="Reproducir", command=lambda: self.reproducirSeleccionada())
        btn_reproducir.place(x=1000, y=450)

        btn_modoNormal = Button(frame, text="Normal", command=lambda: self.modo_reproduccion("Normal"))
        btn_modoNormal.place(x=97, y=340)

        btn_modoAleatorio = Button(frame, text="Aleatorio", command=lambda: self.modo_reproduccion("Aleatorio"))
        btn_modoAleatorio.place(x=215, y=340)

        btn_reproducir = Button(frame, text="Reproducir Lista", command=lambda: self.reproducir_Lista())
        btn_reproducir.place(x=1085, y=450)
        
        img_play = PhotoImage(file="iconos//play.png")
        img_play = Button(frame, text="Play", bg="#fff", bd=0, command = self.play)
        img_play.place(x=165, y=340)
        
        # EL BOTON QUE FUNCA CON DOBLE FUNCION PLAY Y PAUSA
        img_play_pause = PhotoImage(file="iconos//play.png")  # NO SE COMO PONER UN ICONO DINAMICO DE PLAY Y PAUSA
        btn_play_pause = Button(frame, image=img_play_pause, bg="#fff", bd=0, command=self.togglePlayPause)
        btn_play_pause.place(x=160, y=370)  
        
        #PARA EL BOTON SIGUIENTE
        img_next = PhotoImage(file="iconos//Next.png")
        btn_next = Button(frame, image=img_next, bg="#fff", bd=0, command=self.aNext)
        btn_next.place(x=215, y=370)

        #PARA EL BOTON ATRAS
        img_previous = PhotoImage(file="iconos//Previous.png")
        btn_previous = Button(frame, image=img_previous, bg="#fff", bd=0, command=self.aBack)
        btn_previous.place(x=115, y=370)
        
        #Añade canciones deseadas a la playlist
        btnAdd = Button(frame, text = "Add To List", bg="#fff", bd=0, command = self.addToList)
        btnAdd.place(x = 840, y = 247)
        
        #Boton para guardar lista y poder usar el combobox de Listas de Reproducción 
        btnSave = Button(frame, text = "Save List", bg="#fff", bd=0, command = self.saveList)
        btnSave.place(x = 846, y = 160)
        
        #Boton para limpiar la lista de reproducción
        btnDelete = Button(frame, text = "Clear List", bg="#fff", bd=0, command= self.addPlayList)
        btnDelete.place(x = 845, y = 189)
        
        #COMBOBOX
        self.cbbArtistas = ttk.Combobox(self.ventana, state = "readonly")
        self.cbbAlbumbes = ttk.Combobox(self.ventana, state = "readonly")
        self.cbbListas = ttk.Combobox(self.ventana, state = "readonly")
        self.cbbArtistas.bind("<<ComboboxSelected>>", self.change_artist)
        self.cbbAlbumbes.bind("<<ComboboxSelected>>", self.change_album)
        self.cbbListas.bind("<<ComboboxSelected>>", self.on_lista_seleccionada)
        self.cbbArtistas.place(x = 855, y = 170, width = 120)
        self.cbbAlbumbes.place(x = 855, y = 210, width = 120)
        self.cbbListas.place(x = 855, y = 250, width = 120)
        
        # Para que sea visible todo lo que realizamos
        self.ventana.mainloop()