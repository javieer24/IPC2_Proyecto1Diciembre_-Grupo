# **Manual Técnico**

Requisitos minimos del Sistema Operativo para ejecutar el programa:

- Windows 10 (8u51 y superiores)
- Windows 8.x (escritorio)
- Windows 7 SP1
- Windows Vista SP2
- RAM: 128MB
- Espacio en Disco: 124 MB para python
- Procesador: Minimo Pentium 2 a 266 M




## ⚒ Requerimientos
<ul>
    <li>Python 3.11.5 o Superior</li>
    <li>Graphviz 0.20 o superior</li>
    <li>PySide6 6.5.2 o superior</li>
    <li>Pillow 10.1.0  </li>
    <li>Pygame </li>
</ul>

## 🗂 Recursos
<ul>
  <li><a href="https://www.python.org/downloads/release/python-3115/">Python 3.11.5 o Superior</a></li>
  <li><a href="https://pypi.org/project/PySide6/6.5.2/">PySide6 6.5.2 o superiorr</a></li>
  <li><a href="https://pypi.org/project/graphviz/">Graphviz 0.20 o superior</a></li>
  <li><a href="https://pypi.org/project/Pillow/">Pillow 10.1.0</a></li>
  <li><a href="[hhttps://www.pygame.org/wiki/GettingStarted/](https://www.pygame.org/download.shtml)">Pygame</a></li>
</ul>

## **Descripción General**
El presente proyecto consiste en el desarrollo de un reproductor de música que utiliza un archivo XML para almacenar la información sobre las canciones. El reproductor debe ser capaz de leer el archivo XML, mostrar una lista de las canciones, reproducir las canciones y mostrar la imagen de la canción que se está reproduciendo junto con su archivo mp3.

# Estructura Proyecto 1, carpetas  y archivos

~~~
IPC2_Proyecto1Diciembre_-Grupo8
├── Documentación
│   ├── Manual de Usuario
│   │   ├── README.md
│   └── Manual Tecnico
│   │   ├── README.md
│   └── Documentación
│   └── Proyecto1IPC2 - Diciembre.pdf
├── GUI
│   ├── __init__.py
│   └── app.py
├── iconos
│   ├── 15 imagenes png 
├── IMG
│   ├── archivos jpg para documentación 
├── method
│   ├── __init__.py
│   └── readxml.py
├── MisListas
│   ├── aquí se guardan las listas en xml
├── objects
│   ├── __init__.py
│   └── objects.py
├── Test
│   ├── Musica
│   │   ├──archivos mp3 y jpg
│   ├── biblioteca.xml
│   ├── MiLista.xml
├── thread
│   ├── __init__.py
│   └── thread.py
├── __init__.py
├── app.py
├── library.dot
├── main.py
├── objects.py
├── README.md
~~~

## **Paradigma de Programación**
Todo el desarrollo del programa está basado en el paradigma de programación orientado a objetos, esto es, un modelo o un estilo de programación que proporciona unas guías acerca de cómo trabajar con él y que está basado en el concepto de clases y objetos.

Es por ello que durante toda la realización del programa se implementó el uso de clases, clases abstractas y objetos de las mismas.

**Listas**
Las listas se utilizan para almacenar una colección de datos. En este proyecto, las listas se utilizan para almacenar las canciones, las listas de reproducción y los comandos del usuario.

Se utilizan listas enlazadas para almacenar las canciones, ya que permiten insertar y eliminar elementos de la lista de forma eficiente.

Se utilizan listas circulares para almacenar las listas de reproducción, ya que permiten acceder a cualquier elemento de la lista de forma eficiente.

**Nodos**
Los nodos son las unidades básicas de las listas enlazadas. Cada nodo contiene un elemento de datos y una referencia al siguiente nodo de la lista.

**Pila**
Una pila es una estructura de datos que sigue el principio de la LIFO (Last In, First Out), es decir, el último elemento que se inserta en la pila es el primero que se elimina.

En este proyecto, la pila se utiliza para almacenar los comandos del usuario.

**Cola**
Una cola es una estructura de datos que sigue el principio de la FIFO (First In, First Out), es decir, el primer elemento que se inserta en la cola es el primero que se elimina.

En este proyecto, la cola se utiliza para almacenar las solicitudes de reproducción de canciones.

## **Diccionario de librerías utilizadas**
### Libreria Tkinter:
- Tkinter es una libreria que funciona para la creación y el desarrollo de aplicaciones de escritorio. Esta librería facilita el posicionamiento y desarrollo de una interfaz gráfica de escritorio con python. TK se describe a sí mismo como el único toolkit o kit de herramientas para el desarrollo de una interfaz gráfica de usuario.

### Módulo "os"
- Este módulo provee una manera versátil de usar funcionalidades dependientes del sistema operativo. Si se desea manipular rutas, se realiza gracias al modulo os.path

### xml.etree.ElementTree (ET)

- xml.etree.ElementTree (ET) es un módulo de Python que permite trabajar con archivos XML. ET proporciona una API sencilla y eficiente para leer, escribir y manipular archivos XML.

### PIL (Pillow)

- PIL (Pillow) es una librería de Python que permite trabajar con imágenes. PIL proporciona una API completa para crear, leer, editar y guardar imágenes.

### random

- random es un módulo de Python que proporciona funciones para generar números aleatorios. random se puede utilizar para generar números aleatorios para una variedad de propósitos, como generar números aleatorios para juegos o para crear efectos aleatorios en una GUI.

### filedialog

- filedialog es un módulo de Python que proporciona funciones para abrir y guardar archivos. filedialog se puede utilizar para permitir a los usuarios abrir o guardar archivos desde una GUI.

### threading

threading es un módulo de Python que proporciona funciones para crear y gestionar procesos en segundo plano. threading se puede utilizar para realizar tareas en segundo plano, como la reproducción de audio o la descarga de archivos.

### ctypes

- ctypes es un módulo de Python que permite acceder a funciones y variables del sistema operativo. ctypes se puede utilizar para realizar tareas que no son posibles o que son difíciles de realizar con las librerías y módulos estándar de Python.

### pygame.mixer

- pygame.mixer es un módulo de Python que permite reproducir audio. pygame.mixer se puede utilizar para reproducir música, efectos de sonido o cualquier otro tipo de audio.

## **Diccionario de Clases**
### **method > readxml.py**
```js

class XMLReader:
    def __init__(self):
        self.ruta = self.loadXML()
        self.contenido = ""
    def loadXML(self):
        try:
            ruta  = filedialog.askopenfilename(title = "Seleccione su XML", filetypes=[("XML File", "*.xml *.XML")])
            return ruta
        except: FileNotFoundError
    def analyze(self):
        if self.ruta == "":
            print("Sin ruta XML")
            return None
        else:
            self.contenido = open(self.ruta, "r").read()
            self.biblioteca = Library()
            library = ET.fromstring(self.contenido)
            for biblioteca in library.iter("biblioteca"):
                for cancion in biblioteca.iter("cancion"):
                    nombre = cancion.attrib["nombre"]
                    album = ""
                    artista = ""
                    imagen = ""
                    ruta = ""
                    for artist, album_, image, path in zip(
                        cancion.iter("artista"), cancion.iter("album"), cancion.iter("imagen"), cancion.iter("ruta")):
                        album += album_.text
                        artista += artist.text
                        imagen += image.text
                        ruta += path.text
                    if nombre == "":
                        nombre += "single"
                    if album == "":
                        album += "single"
                    if artista == "":
                        artista += "single"
                    self.biblioteca.addSong(Cancion(nombre, album, artista, ruta, imagen))
            return self.biblioteca 
```
La clase XMLReader se encarga de leer y analizar un archivo XML que contiene información sobre una biblioteca musical. Extrae los datos de las canciones, álbumes y artistas y los utiliza para poblar una instancia de la clase Library.

**Atributos:**
- ruta: Almacena la ruta del archivo XML seleccionado por el usuario.
- contenido: Contiene el contenido textual del archivo XML cargado.
- biblioteca: Objeto de la clase Library que se llena con los datos del XML.

**Métodos:**
- __init__ : Inicializa la clase y utiliza loadXML para obtener la ruta del archivo XML.
- loadXML : Solicita al usuario que seleccione un archivo XML y devuelve su ruta. Maneja el error FileNotFoundError.
- analyze : Analiza el contenido del archivo XML y devuelve un objeto de la clase Library con los datos cargados. Si no se seleccionó ningún archivo o hubo un error, devuelve None.

**Pasos del análisis:**
1. Verifica si la ruta del archivo es válida.
2. Lee el contenido del archivo.
5. Crea un objeto Library vacío.
4. Analiza el documento XML usando ElementTree:
 - Recorre los elementos "biblioteca".
 - Para cada elemento "cancion":
    - Extrae el nombre, álbum, artista e imagen de la canción.
    - Si alguno de estos valores está vacío, lo reemplaza con "single".
    - Crea un objeto Cancion con la información extraída.
    - Añade la canción a la biblioteca usando addSong.
5. Devuelve el objeto Library con las canciones cargadas.


### **GUI > app.py**
```js

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
                    print(f"Añadiendo canción: {nombre_cancion}")  # Depuración

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
        btn_reportes = Button(self.ventana, text = "Reportes", command = self.reportes)
        btn_reportes.place(x=70, y=70, width = 85, height = 25)


        btn_crear_lista = Button(frame, text="Crear Lista", command=self.crear_listaReproduccion)
        btn_crear_lista.place(x=840, y=218)
        
        btn_crear_lista = Button(frame, text="Agregar Lsita", command=self.agregar_cancion_a_lista)
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


        btnnext = Button(frame, text = "Next", bg="#fff", bd=0, command = self.aNext)
        btnnext.place(x = 215, y = 415)

        btnback = Button(frame, text = "Back", bg="#fff", bd=0, command = self.aBack)
        btnback.place(x = 115, y = 415)
        
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
```
**Class app**
Esta clase es la encargada de crear la ventana principal de la aplicación, en ella se encuentran todos los componentes que se utilizan en la interfaz gráfica, como lo son los botones, labels, combobox, etc. Además, se encarga de llamar a los métodos que se encargan de realizar las funciones de cada botón, como lo son la reproducción de canciones, la creación de listas de reproducción, etc.
- Esta clase hereda de Tk y representa la ventana principal de la aplicación.
- Define varias funciones para administrar la interfaz de usuario, la reproducción de música y la gestión de listas de reproducción.
**Funciones**
- cerrar_aplicación: Cierra la ventana de la aplicación.
- minimizar_ventana: Minimiza la ventana de la aplicación.
- cargarListasDeReproduccion: Carga las listas de reproducción desde archivos XML.
- seleccionar_y_mostrar_lista: Abre un cuadro de diálogo de archivos para seleccionar un archivo XML de lista de reproducción y luego muestra su contenido.
- actualizar_vista_playlist: Actualiza la vista de la lista de reproducción en función de la lista de reproducción seleccionada.
- on_lista_seleccionada: Se llama cuando se selecciona una lista de reproducción en la lista.
- mostrar_lista: Muestra el contenido de un archivo XML de lista de reproducción.
- addArbol: Crea un widget treeview para mostrar canciones.
- reproducir_Lista: Intenta reproducir la lista de reproducción seleccionada.
- addPlayList: Crea una nueva lista de reproducción y la muestra en la interfaz.
- cargarXML: Carga la biblioteca de música desde archivos XML.
- setArtistas: Llena el combobox de artistas con artistas de la biblioteca.
- change_artist: Se llama cuando cambia la selección del combobox de artistas.
- setAlbumes: Llena el combobox de álbumes con álbumes para el artista seleccionado.
- change_album: Se llama cuando cambia la selección del combobox de álbumes.
- setCanciones: Llena la lista de canciones con canciones para el álbum seleccionado.
- addToList: Agrega la canción seleccionada a la lista de reproducción actual.
- play: Inicia la reproducción de la lista de reproducción actual o la canción seleccionada.
- aNext: Reproduce la siguiente canción en la lista de reproducción o una canción aleatoria en modo aleatorio.
- aBack: Reproduce la canción anterior en la lista de reproducción.
- next: Devuelve el siguiente nodo en la lista de reproducción.
- back: Devuelve el nodo anterior en la lista de reproducción.
- setPhoto: Establece la imagen de la obra de arte del álbum en función de la canción actual.
- togglePlayPause: Pausa o reanuda la reproducción.
- agregar_cancion_a_lista: Agrega la canción seleccionada a una lista de reproducción elegida y actualiza su archivo XML.
- setInfo: Actualiza las etiquetas de información de la canción (título, álbum, artista).
- reproducir: Inicia la reproducción de una canción específica e incrementa su recuento de reproducción.
- pause: Pausa la reproducción.
- stop: Detiene la reproducción.
- reportes: Genera informes basados ​​en la biblioteca de música.
- saveList: Guarda la lista de reproducción actual a la lista de listas de reproducción.
- MisListas: Carga y muestra una lista de reproducción específica.
- crear_listaReproduccion: Crea una nueva lista de reproducción con un nombre y archivo XML elegidos.
- crear_archivo_xml_para_lista: Crea un nuevo archivo XML para una lista de reproducción.
- actualizar_lista_combobox: Actualiza el combobox de listas de reproducción con las listas de reproducción disponibles.
- reproducirSeleccionada: Reproduce la canción seleccionada actualmente en la lista de canciones.
- modo_reproduccion: Establece el modo de reproducción (normal o aleatorio).
- onCancionSeleccionada: Se llama cuando se selecciona una canción en la lista de canciones.
- init: Inicializa la ventana de la aplicación y configura las variables internas.
- initComponent: Inicializa los componentes de la interfaz de usuario.

### **method > objects.py**
```js
class Nodo:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.siguiente = None
        self.anterior = None
    def __str__(self) -> str:
        return str(self.value)
class ListaDoble:
    def __init__(self):
        self.length = 0
        self.cabeza = None
        self.cola = None

    def append(self, value):
        nuevo = Nodo(value, self.length)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            actual = self.cola
            nuevo.anterior = actual
            actual.siguiente = nuevo
            self.cola = nuevo
        self.length += 1

    def getById(self, id):
        if self.cabeza is None:
            return "No hay cabeza"
        else:
            if id < 0 or id >= self.length:
                return "Fuera de rango"
            else:
                actual = self.cabeza
                while actual.id != id:
                    actual = actual.siguiente
                return actual.value

    def contains(self, nombre):
        actual = self.cabeza
        while actual is not None:
            if actual.value.nombre == nombre:
                return actual.id
            actual = actual.siguiente
        return None

    def __str__(self):
        if self.cabeza is None:
            return "[]"
        else:
            string = "["
            actual = self.cabeza
            while actual is not None:
                string += "{},".format(actual) if actual.siguiente else "{}]".format(actual)
                actual = actual.siguiente
            return string

    def get_nombres(self):
        nombres = []
        actual = self.cabeza
        while actual is not None:
            nombres.append(actual.value.nombre)  # Asumiendo que cada nodo tiene un atributo 'nombre'
            actual = actual.siguiente
        return nombres
    
    def __init__(self):
            self.length = 0
            self.cabeza = None
            self.cola = None    
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.value
            actual = actual.siguiente
class Cancion:
    def __init__(self, nombre, album, artista, ruta, imagen):
        self.nombre = nombre
        self.album = album
        self.artista = artista
        self.ruta = ruta
        self.imagen = imagen
        self.vecesReproducida = 0  # Añade el contador de reproducciones

    def incrementar_reproducciones(self):
        self.vecesReproducida += 1

    def __str__(self):
        return f"Canción: {self.nombre}, Reproducciones: {self.vecesReproducida}"

class Album:
    def __init__(self, nombre, imagen):
        self.nombre = nombre
        self.imagen = imagen
        self.listaCanciones = ListaDoble()
    def getCanciones(self):
        return self.listaCanciones
    def __str__(self):
        string = "\n\t\t\tAlbum: {} - Canciones:\n".format(self.nombre)
        for i in range(self.listaCanciones.length):
                string += "\n\t\t\t\t{}".format(self.listaCanciones.getById(i))       
        return string

class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaAlbumes = ListaDoble()
    def getAlbumes(self):
        lista = []
        for i in range(self.listaAlbumes.length):
            album = self.listaAlbumes.getById(i)
            lista.append(album.nombre)
        return lista
    def __str__(self):
        string = "\n\t\tArtista: {} - Albumes:".format(self.nombre)
        for i in range(self.listaAlbumes.length):
            string += "\n{}".format(self.listaAlbumes.getById(i))
        return string


class Library:
    def __init__(self):
        self.listaArtistas = ListaDoble()
    def addSong(self, song):
        new = song
        nombre = new.nombre
        album = new.album
        artista = new.artista
        imagen = new.imagen
        contains = self.listaArtistas.contains(artista)
        if contains != None:
            artist = self.listaArtistas.getById(contains)
            contains = artist.listaAlbumes.contains(album)
            if contains != None:
                album_ = artist.listaAlbumes.getById(contains)
                contains = album_.listaCanciones.contains(nombre)
                if contains != None:
                    print("Cancion en biblioteca.. Posición: {}".format(contains))
                else:
                    album_.listaCanciones.append(new)
            else:
                nuevoAlbum = Album(album, imagen)
                nuevoAlbum.listaCanciones.append(new)
                artist.listaAlbumes.append(nuevoAlbum)
        else:
            nuevoArtista = Artista(artista)
            nuevoAlbum = Album(album, imagen)
            nuevoAlbum.listaCanciones.append(new)
            nuevoArtista.listaAlbumes.append(nuevoAlbum)
            self.listaArtistas.append(nuevoArtista)
    def toList(self):#Este método retorna una lista que es necesaria
        lista = ListaDoble()
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            for j in range(artista.listaAlbumes.length):
                album = artista.listaAlbumes.getById(j)
                for k in range(album.listaCanciones.length):
                    cancion = album.listaCanciones.getById(k)
                    lista.append(cancion)
        return lista
    
    def report(self):
        string = """digraph G {
layout = dot;
labelloc = "t";
edge [weigth = 1000];
rankdir = LR;\n"""
        string += "\tsubgraph artistas {\n\trankdir = LR;\n"
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            string += '\t\t"{}"[fillcolor = beige style = "filled"];\n'.format(artista.nombre)
            string += '\t\t\tsubgraph "album{}"{}\n\t\t\trankdir = TB;\t\t\trank=same;\n'.format(artista.nombre,"{")
            for j in range(artista.listaAlbumes.length):
                album = artista.listaAlbumes.getById(j)
                if j == 0:
                    string += '\t\t\t\t"{}"->"{}"\n'.format(artista.nombre,album.nombre)
                string += '\t\t\t\t"{}"[fillcolor = aquamarine style = "filled"];\n'.format(album.nombre)
                string += '\t\t\t\t\tsubgraph "album{}"{}\n\t\t\t\t\trankdir = LR;\n'.format(album.nombre,"{")
                for k in range(album.listaCanciones.length):
                    cancion = album.listaCanciones.getById(k)
                    if k == 0:
                        string += '\t\t\t\t\t\t"{}"->"{}"\n'.format(album.nombre, cancion.nombre)
                    string += '\t\t\t\t\t\t\t"{}"[fillcolor = deepskyblue style = "filled"];\n'.format(cancion.nombre)
                string += '\t\t\t\t\t}\n'

            string += '\t\t\t}\n'
        string += "\t}\n"
        # Hacia delante
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            for j in range(artista.listaAlbumes.length):
                album = artista.listaAlbumes.getById(j)
                for k in range(album.listaCanciones.length):
                    cancion = album.listaCanciones.getById(k)

                    # Conexiones hacia adelante
                    if i + 1 < self.listaArtistas.length:
                        siguiente_artista = self.listaArtistas.getById(i + 1)
                        string += '"{}"->"{}";\n'.format(artista.nombre, siguiente_artista.nombre)

                    if j + 1 < artista.listaAlbumes.length:
                        siguiente_album = artista.listaAlbumes.getById(j + 1)
                        string += '"{}"->"{}";\n'.format(album.nombre, siguiente_album.nombre)

                    if k + 1 < album.listaCanciones.length:
                        siguiente_cancion = album.listaCanciones.getById(k + 1)
                        string += '"{}"->"{}";\n'.format(cancion.nombre, siguiente_cancion.nombre)

        # Hacia atras
        for i in range(self.listaArtistas.length - 1, 0, -1):
            artista = self.listaArtistas.getById(i)
            for j in range(artista.listaAlbumes.length - 1, 0, -1):
                album = artista.listaAlbumes.getById(j)
                for k in range(album.listaCanciones.length - 1, 0, -1):
                    cancion = album.listaCanciones.getById(k)

                    # Conexiones hacia atras
                    if i - 1 >= 0:
                        anterior_artista = self.listaArtistas.getById(i - 1)
                        string += '"{}"->"{}";\n'.format(artista.nombre, anterior_artista.nombre)

                    if j - 1 >= 0:
                        anterior_album = artista.listaAlbumes.getById(j - 1)
                        string += '"{}"->"{}";\n'.format(album.nombre, anterior_album.nombre)

                    if k - 1 >= 0:
                        anterior_cancion = album.listaCanciones.getById(k - 1)
                        string += '"{}"->"{}";\n'.format(cancion.nombre, anterior_cancion.nombre)
        string += "\n}"
        file = open("library.dot", "w")
        file.write(string)
        file.close()
        os.system('dot -Tpng library.dot -o library.png')
        
    def getArtistas(self):
        lista = []
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            lista.append(artista.nombre)
        return lista    
    def __str__(self):
        string = "Biblioteca\n\tArtistas:\n"
        for i in range(self.listaArtistas.length):
            string += "\n\t{}".format(self.listaArtistas.getById(i))
        return string
    
class EntryPlaceholder(Entry):
    def __init__(self, placeholder, master = None, color = 'grey'):    
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()
            
class ListaCircular:
    def __init__(self):
        self.length = 0
        self.head = None
        self.cola = None
        self.nombre = ""
    def append(self, value):
        nuevo = Nodo(value, self.length)
        if self.head == None:
            self.head = self.cola = nuevo
            self.head.anterior = self.cola
            self.cola.siguiente = self.head
        else:
            aux = self.cola
            self.cola = aux.siguiente = nuevo
            self.cola.anterior = aux
            self.head.anterior = self.cola
            self.cola.siguiente = self.head
        self.length += 1
    def getById(self, id):
        if id < 0 or id >= self.length or self.head == None:
            return None
        else:
            actual = self.head
            while True:
                if actual.id == id:
                    break
                actual = actual.siguiente
            return actual.value
    def contains(self, nombre):
            if self.head == None:
                return None
            actual = self.head
            inicio = True
            while inicio or actual != self.head:
                inicio = False
                if actual.value.nombre == nombre:
                    return actual.id
                actual = actual.siguiente
            return None
    
    def __str__(self):
        string = "["
        if self.head != None:
            actual = self.head
            while True:
                if actual.siguiente == self.head:
                    string += "{}]".format(actual)
                else:
                    string += "{},".format(actual)
                actual = actual.siguiente
                if actual == self.head:
                    break

        else:
            string += "]"
        return string
```
**Clases:**

- Nodo: Representa un nodo en una lista doblemente enlazada. Contiene un valor, un ID único, y referencias al nodo anterior y siguiente.
- ListaDoble: Implementa una lista doblemente enlazada. Almacena el número de elementos, la cabeza y la cola de la lista. Proporciona métodos para añadir, obtener por ID, buscar por nombre, iterar y convertir a string.
- Cancion: Representa una canción. Contiene nombre, álbum, artista, ruta de archivo e imagen. Permite incrementar el contador de reproducciones y convertir a string.
- Album: Representa un álbum. Contiene nombre, imagen y una lista doble de canciones. Ofrece métodos para obtener las canciones, convertir a string e imprimir los detalles.
- Artista: Representa un artista. Contiene nombre y una lista doble de álbumes. Proporciona métodos para obtener los álbumes, convertir a string e imprimir los detalles.
- Library: Representa una biblioteca musical. Contiene una lista doble de artistas. Se encarga de añadir canciones, generar una lista plana de todas las canciones, generar un diagrama de relaciones en formato .dot y obtener la lista de artistas.
- EntryPlaceholder: Es una extensión de la clase Entry de tkinter que añade un placeholder personalizable que desaparece al enfocar el campo de texto.
- ListaCircular: Implementa una lista circular enlazada. Contiene el número de elementos, el nodo cabeza y cola, y un nombre opcional. Proporciona métodos para añadir, obtener por ID, buscar por nombre y convertir a string.

**Funciones:**
- os.system('dot -Tpng library.dot -o library.png'): Esta función utiliza la herramienta 'dot' para generar un archivo PNG a partir del archivo de texto generado por el método report de la clase Library.

### **TPlay**
```js
class TPlay(threading.Thread):
    def __init__(self, ruta):
        threading.Thread.__init__(self)
        self.ruta = ruta
        self.estado = ""
    def run(self):
        mixer.init() 
        mixer.music.load(self.ruta) 
        mixer.music.set_volume(0.7) 
        mixer.music.play() 
        while True: 
            if self.estado == 'p': 
                mixer.music.pause()      
            elif self.estado == 'r': 
                mixer.music.unpause() 
            elif self.estado == 'e': 
                mixer.music.stop() 
                break
    def get_id(self):
        if hasattr(self, "_thread_id"):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
```

La clase TPlay permite crear un hilo independiente para reproducir un archivo de audio. El hilo se encarga de cargar el archivo, controlar la reproducción (play, pause, stop) y detenerse cuando se le indique. La función raise_exception se utiliza como último recurso para detener el hilo en caso de que no responda a los cambios de estado.

**Clase TPlay:**

- Subclase de threading.Thread que representa un hilo para reproducir música.
- Atributos:
  - ruta: Ruta del archivo de audio a reproducir.
  - estado: Cadena que indica el estado actual de la reproducción ('', 'p', 'r', 'e').
- Métodos:
  - __init__: Inicializa el hilo con la ruta del archivo.
  - run: Método principal del hilo que se ejecuta al iniciar:
- Inicializa el mixer de Pygame.
- Carga el archivo de audio.
- Establece el volumen a 0.7.
- Comienza la reproducción.
- Entra en un ciclo infinito que verifica el estado:
   - 'p': Pausa la reproducción.
   - 'r': Reanuda la reproducción.
   - 'e': Detiene la reproducción y sale del ciclo.
- get_id: Obtiene el ID del hilo.
- raise_exception: Intenta detener el hilo de manera forzada usando funciones del sistema operativo.

### app.py
```js
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
            
    def reportes(self):
        if self.library != None:
            self.library.report()
        else:
            messagebox.showerror(message = "No se ha cargado ninguna biblioteca", title = "Error")
        
    # ------- Metodos para listas de reproduccion --------

    def crear_listaReproduccion(self):
        nombre_lista = simpledialog.askstring("Crear una lista de Reproducción", "Nombre de la Lista: " )
        if nombre_lista:
            if not self.listaPlayList.buscar(nombre_lista):
                nueva_Lista = ListaCircular()
                nueva_Lista.nombre = nombre_lista
                self.listaPlayList.append(nueva_Lista)
                self.cbbListas["values"] = self.listaPlayList.get_nombres()
                self.cbbListas.current(len(self.listaPlayList) -1)
                print("Contenido actual de self.listaPlayList:", self.listaPlayList)

            else:
                messagebox.showwarning("Error, ese nombre ya existe!")
    

    def modo_reproduccion(self, modo):
        if modo == "Normal":
            self.modo_reproduccion_actual = "Normal"
        elif modo == "Aleatorio":
            self.modo_reproduccion_actual = "Aleatorio"

    
    def reproducir_Lista(self):
        if self.cbbListas.get():
            nombre_lista = self.cbbListas.get()
            id_lista = self.listaPlayList.contains(nombre_lista)

            if id_lista is not None:
                current_lista = self.listaPlayList.getById(id_lista)
                if current_lista:
                    if self.modo_reproduccion_actual == "Normal":
                        self.actualPlaylist = current_lista.head
                    elif self.modo_reproduccion_actual == "Aleatorio":
                        indice_aleatorio = random.randint(0, current_lista.length - 1)
                        self.actualPlaylist = current_lista.getById(indice_aleatorio)

                    self.reproducir(self.actualPlaylist.value)
                else:
                    print("La lista está vacía.")
            else:
                print("Lista no encontrada.")

    
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

# Constructor
    def initComponent(self):
        self.ventana = Frame(self, background = "#082032")
        self.ventana.place(x = 0, y = 0, width = 1360, height = 700)

        #------------------------------------------------------ Frames ---------------------------------------------------------
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
        
       #------------------------------------------------------ Labels ---------------------------------------------------------
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
 
  #------------------------------------------------------ Buttons ---------------------------------------------------------
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

        #Botón para reportes
        btn_reportes = Button(self.ventana, text = "Reportes", command = self.reportes)
        btn_reportes.place(x=40, y=55, width = 85, height = 25)


        btn_crear_lista = Button(frame, text="Crear Lista", command=self.crear_listaReproduccion)
        btn_crear_lista.place(x=990, y=450)

        btn_modoNormal = Button(frame, text="Normal", command=lambda: self.modo_reproduccion("Normal"))
        btn_modoNormal.place(x=400, y=350)

        btn_modoAleatorio = Button(frame, text="Aleatorio", command=lambda: self.modo_reproduccion("Aleatorio"))
        btn_modoAleatorio.place(x=475, y=350)

        btn_reproducir = Button(frame, text="Reproducir Lista", command=lambda: self.reproducir_Lista())
        btn_reproducir.place(x=1090, y=450)
        
        img_play = PhotoImage(file="iconos/play.png")
        img_play = Button(frame, text="play", bg="#fff", bd=0, command = self.play)
        img_play.place(x=475, y=400)
        
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
```
***Clases***
- App: Clase principal de la aplicación. Contiene la interfaz gráfica y las funciones principales.
- Cancion: Clase que representa una canción.
- Artista: Clase que representa un artista.
- Album: Clase que representa un álbum.
- ListaReproduccion: Clase que representa una lista de reproducción.
- TPlay: Clase que representa un hilo para la reproducción de música.

***Funciones:***

- cerrar_aplicacion(): Cierra la aplicación.
- minimizar_ventana(): Minimiza la ventana de la aplicación.
- cargarXML(): Carga un archivo XML que contiene la biblioteca musical.
- setArtistas(): Actualiza la lista de artistas en el combobox.
- change_artist(): Se llama cuando se selecciona un artista en el combobox.
- setAlbumes(): Actualiza la lista de álbumes en el combobox.
- change_album(): Se llama cuando se selecciona un álbum en el combobox.
- setCanciones(): Actualiza la lista de canciones en el TreeView.
- addArbol(): Añade el TreeView a la interfaz gráfica.
- addPlayList(): Añade el combobox de listas de reproducción a la interfaz gráfica.
- addToList(): Añade una canción a la lista de reproducción actual.
- play(): Inicia la reproducción de la canción o lista de reproducción actual.
- pause(): Pausa la reproducción de la canción o lista de reproducción actual.
- stop(): Detiene la reproducción de la canción o lista de reproducción actual.
- aNext(): Pasa a la siguiente canción en la lista de reproducción actual.
- aBack(): Pasa a la canción anterior en la lista de reproducción actual.
- crear_listaReproduccion(): Crea una nueva lista de reproducción.
- modo_reproduccion(): Cambia el modo de reproducción a normal o aleatorio.
- reproducir_Lista(): Inicia la reproducción de la lista de reproducción seleccionada.

***Métodos:***

- __init__(self): Constructor de la clase ```app```.
- mainloop(): Método principal de la aplicación.
- setInfo(): Establece la información de la canción actual.
- setPhoto(): Establece la imagen de la portada del álbum actual.
- reproducir(): Reproduce una canción.
            
### Objects.py

```js
class Nodo:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.siguiente = None
        self.anterior = None
    def __str__(self) -> str:
        return str(self.value)
class ListaDoble:
    def __init__(self):
        self.length = 0
        self.cabeza = None
        self.cola = None
    
    def buscar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.value.nombre == nombre:
                return True
            actual = actual.siguiente
        return False

    def append(self, value):
        nuevo = Nodo(value, self.length)
        if self.cabeza == None:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            actual = self.cola
            nuevo.anterior = actual
            self.cola = nuevo
            actual.siguiente = self.cola
        self.length += 1
    def getById(self, id):
        if self.cabeza == None:
            return "No hay cabeza"
        else:
            if id < 0 or id >= self.length:
                return "Fuera de rango"
            else:
                actual = self.cabeza
                while actual.id != id:
                    actual = actual.siguiente
                return actual.value
    def contains(self, nombre):
            if self.head == None:
                return None
            actual = self.head
            inicio = True
            while inicio or actual != self.head:
                inicio = False
                if actual.value.nombre == nombre:
                    return actual.id
                actual = actual.siguiente
            return None
        
    def __str__(self):
        if self.cabeza == None:
            return "[]"
        else:
            string = "["
            actual = self.cabeza
            while actual != None:
                if actual.siguiente == None:
                    string += "{}]".format(actual)
                else:
                    string += "{},".format(actual)
                actual = actual.siguiente
            return string
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.value
            actual = actual.siguiente
class Cancion:
    def __init__(self, nombre, album, artista, ruta, imagen):
        self.nombre = nombre
        self.album = album
        self.artista = artista
        self.ruta = ruta
        self.imagen = imagen
        self.vecesReproducida = 0  # Añade el contador de reproducciones

    def incrementar_reproducciones(self):
        self.vecesReproducida += 1

    def __str__(self):
        return f"Canción: {self.nombre}, Reproducciones: {self.vecesReproducida}"

class Album:
    def __init__(self, nombre, imagen):
        self.nombre = nombre
        self.imagen = imagen
        self.listaCanciones = ListaDoble()
    def getCanciones(self):
        return self.listaCanciones
    def __str__(self):
        string = "\n\t\t\tAlbum: {} - Canciones:\n".format(self.nombre)
        for i in range(self.listaCanciones.length):
                string += "\n\t\t\t\t{}".format(self.listaCanciones.getById(i))       
        return string

class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaAlbumes = ListaDoble()
    def getAlbumes(self):
        lista = []
        for i in range(self.listaAlbumes.length):
            album = self.listaAlbumes.getById(i)
            lista.append(album.nombre)
        return lista
    def __str__(self):
        string = "\n\t\tArtista: {} - Albumes:".format(self.nombre)
        for i in range(self.listaAlbumes.length):
            string += "\n{}".format(self.listaAlbumes.getById(i))
        return string


class Library:
    def __init__(self):
        self.listaArtistas = ListaDoble()
    def addSong(self, song):
        new = song
        nombre = new.nombre
        album = new.album
        artista = new.artista
        imagen = new.imagen
        contains = self.listaArtistas.contains(artista)
        if contains != None:
            artist = self.listaArtistas.getById(contains)
            contains = artist.listaAlbumes.contains(album)
            if contains != None:
                album_ = artist.listaAlbumes.getById(contains)
                contains = album_.listaCanciones.contains(nombre)
                if contains != None:
                    print("Cancion en biblioteca.. Posición: {}".format(contains))
                else:
                    album_.listaCanciones.append(new)
            else:
                nuevoAlbum = Album(album, imagen)
                nuevoAlbum.listaCanciones.append(new)
                artist.listaAlbumes.append(nuevoAlbum)
        else:
            nuevoArtista = Artista(artista)
            nuevoAlbum = Album(album, imagen)
            nuevoAlbum.listaCanciones.append(new)
            nuevoArtista.listaAlbumes.append(nuevoAlbum)
            self.listaArtistas.append(nuevoArtista)
    def toList(self):#Este método retorna una lista que es necesaria
        lista = ListaDoble()
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            for j in range(artista.listaAlbumes.length):
                album = artista.listaAlbumes.getById(j)
                for k in range(album.listaCanciones.length):
                    cancion = album.listaCanciones.getById(k)
                    lista.append(cancion)
        return lista
    
    def report(self):
        string = """digraph G {
layout = dot;
labelloc = "t";
edge [weigth = 1000];
rankdir = LR;\n"""
        string += "\tsubgraph artistas {\n\trankdir = LR;\n"
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            string += '\t\t"{}"[fillcolor = beige style = "filled"];\n'.format(artista.nombre)
            string += '\t\t\tsubgraph "album{}"{}\n\t\t\trankdir = TB;\t\t\trank=same;\n'.format(artista.nombre,"{")
            for j in range(artista.listaAlbumes.length):
                album = artista.listaAlbumes.getById(j)
                if j == 0:
                    string += '\t\t\t\t"{}"->"{}"\n'.format(artista.nombre,album.nombre)
                string += '\t\t\t\t"{}"[fillcolor = aquamarine style = "filled"];\n'.format(album.nombre)
                string += '\t\t\t\t\tsubgraph "album{}"{}\n\t\t\t\t\trankdir = LR;\n'.format(album.nombre,"{")
                for k in range(album.listaCanciones.length):
                    cancion = album.listaCanciones.getById(k)
                    if k == 0:
                        string += '\t\t\t\t\t\t"{}"->"{}"\n'.format(album.nombre, cancion.nombre)
                    string += '\t\t\t\t\t\t\t"{}"[fillcolor = deepskyblue style = "filled"];\n'.format(cancion.nombre)
                string += '\t\t\t\t\t}\n'

            string += '\t\t\t}\n'
        string += "\t}\n"
        #Hacia delante
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            if i+1 == self.listaArtistas.length:
                string += '"{}"->"NoneR{}"[style = dashed];\n'.format(artista.nombre, i+1)
            else:
                siguiente = self.listaArtistas.getById(i+1)
                string += '"{}"->"{}";\n'.format(artista.nombre, siguiente.nombre)
            for j in range(artista.listaAlbumes.length):
                album = artista.listaAlbumes.getById(j)
                if j+1 == artista.listaAlbumes.length:
                    string += '"{}"->"NoneR{}{}"[style = dashed];\n'.format(album.nombre,i,j)
                else:
                    siguiente = artista.listaAlbumes.getById(j+1)
                    string += '"{}"->"{}";\n'.format(album.nombre, siguiente.nombre)
                for k in range(album.listaCanciones.length):
                    cancion = album.listaCanciones.getById(k)
                    if k+1 == album.listaCanciones.length:
                        string += '"{}"->"NoneR{}{}{}"[style = dashed];\n'.format(cancion.nombre,i,j,k)
                    else:
                        siguiente = album.listaCanciones.getById(k+1)
                        string += '"{}"->"{}";\n'.format(cancion.nombre, siguiente.nombre)
        #Hacia atras
        for i in range(self.listaArtistas.length-1,-1,-1):
            artista = self.listaArtistas.getById(i)
            if i-1 == -1:
                string += '"{}"->"NoneL{}"[style = dashed];\n'.format(artista.nombre,i)
            else:
                anterior = self.listaArtistas.getById(i-1)
                string += '"{}"->"{}";\n'.format(artista.nombre, anterior.nombre)
            for j in range(artista.listaAlbumes.length-1,-1,-1):
                album = artista.listaAlbumes.getById(j)
                if j-1 == -1:
                    string += '"{}"->"NoneL{}{}"[style = dashed];\n'.format(album.nombre,j,i)
                else:
                    anterior = artista.listaAlbumes.getById(j-1)
                    string += '"{}"->"{};"\n'.format(album.nombre, anterior.nombre)
                for k in range(album.listaCanciones.length-1,-1,-1):
                    cancion = album.listaCanciones.getById(k)
                    if k-1 == -1:
                        string += '"{}"->"NoneL{}{}{}"[style = dashed];\n'.format(cancion.nombre,k,j,i)
                    else:
                        anterior = album.listaCanciones.getById(k-1)
                        string += '"{}"->"{}";\n'.format(cancion.nombre, anterior.nombre)
        string += "\n}"
        file = open("library.dot", "w")
        file.write(string)
        file.close()
        os.system('dot -Tpng library.dot -o library.png')
        
    def getArtistas(self):
        lista = []
        for i in range(self.listaArtistas.length):
            artista = self.listaArtistas.getById(i)
            lista.append(artista.nombre)
        return lista    
    def __str__(self):
        string = "Biblioteca\n\tArtistas:\n"
        for i in range(self.listaArtistas.length):
            string += "\n\t{}".format(self.listaArtistas.getById(i))
        return string
    
class EntryPlaceholder(Entry):
    def __init__(self, placeholder, master = None, color = 'grey'):    
        super().__init__(master)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()
            
class ListaCircular:
    def __init__(self):
        self.length = 0
        self.head = None
        self.cola = None
        self.nombre = ""
    def append(self, value):
        nuevo = Nodo(value, self.length)
        if self.head == None:
            self.head = self.cola = nuevo
            self.head.anterior = self.cola
            self.cola.siguiente = self.head
        else:
            aux = self.cola
            self.cola = aux.siguiente = nuevo
            self.cola.anterior = aux
            self.head.anterior = self.cola
            self.cola.siguiente = self.head
        self.length += 1
    def getById(self, id):
        if id < 0 or id >= self.length or self.head == None:
            return None
        else:
            actual = self.head
            while True:
                if actual.id == id:
                    break
                actual = actual.siguiente
            return actual.value
    def contains(self, object):
        if self.head == None:
            return None
        else:
            actual = self.head
            while actual.siguiente != self.head:
                if actual == object:
                    break
                else:
                    actual = actual.siguiente
            if actual != None:
                return actual.siguiente
            else:
                return None
    def __str__(self):
        string = "["
        if self.head != None:
            actual = self.head
            while True:
                if actual.siguiente == self.head:
                    string += "{}]".format(actual)
                else:
                    string += "{},".format(actual)
                actual = actual.siguiente
                if actual == self.head:
                    break

        else:
            string += "]"
        return string
```
**Clases:**

- Nodo: Representa un nodo en una lista doblemente enlazada. Tiene los atributos ```value``` (el valor del nodo), ```id``` (identificador único del nodo), ```siguiente``` (puntero al siguiente nodo) y ```anterior``` (puntero al nodo anterior).
- ListaDoble: Implementa una lista doblemente enlazada. Tiene los atributos ```length``` (cantidad de nodos en la lista), ```cabeza``` (primer nodo de la lista) y ```cola``` (último nodo de la lista).
- Cancion: Representa una canción. Tiene los atributos ```nombre``` (nombre de la canción), ```album``` (álbum al que pertenece), ```artista``` (nombre del artista), ```ruta``` (ruta del archivo de la canción) e ```imagen``` (ruta de la imagen de la portada del álbum).
- Album: Representa un álbum. Tiene los atributos ```nombre``` (nombre del álbum) e ```imagen``` (ruta de la imagen de la portada del álbum). Posee también una ```listaCanciones``` (una instancia de ListaDoble que contiene las canciones del álbum).
- Artista: Representa un artista. Tiene el atributo ```nombre``` (nombre del artista) y una ```listaAlbumes``` (una instancia de ``` ListaDoble``` que contiene los álbumes del artista).
- Library: Representa la biblioteca musical completa. Tiene el atributo listaArtistas (una instancia de ```ListaDoble ``` que contiene los artistas de la biblioteca).

**Funciones:**

- buscar(nombre): Busca un artista en la biblioteca por su nombre. Devuelve ```True``` si lo encuentra, ```False``` en caso contrario. (dentro de ListaDoble)
- append(value): Añade un nuevo nodo al final de la lista doblemente enlazada. (dentro de ListaDoble)
- getById(id): Obtiene un nodo de la lista doblemente enlazada por su id. Devuelve el nodo si lo encuentra, ```None``` en caso contrario. (dentro de ListaDoble)
- contains(nombre): Verifica si un nodo con un determinado valor se encuentra en la lista doblemente enlazada. Devuelve el id del nodo si lo encuentra, None en caso contrario. (dentro de ListaDoble)
- incrementar_reproducciones(): Incrementa en 1 el contador de reproducciones de una canción. (dentro de Cancion)
- getCanciones(): Devuelve la lista de canciones del álbum. (dentro de Album)
- addSong(song): Añade una nueva canción a la biblioteca musical. (dentro de Library)
- toList(): Convierte la biblioteca musical en una lista plana de canciones. (dentro de Library)
- report(): Genera un archivo PNG con un diagrama de relaciones en formato DOT que representa la biblioteca musical. (dentro de Library)
- getArtistas(): Devuelve una lista con los nombres de los artistas de la biblioteca. (dentro de Library)

**Métodos:**

- init(self): Constructor de la clase. (en todas las clases)
- str(self): Devuelve una representación textual de la clase. (en todas las clases)

**Otras:**

-EntryPlaceholder: Clase personalizada de ```Entry``` de tkinter que muestra un texto de marcador de posición cuando el campo está vacío.
-ListaCircular: Implementa una lista circular con nodos.

