import os 
from tkinter import *

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
        self.head = None
        self.cola = None
        
    def append(self, value):
        new = Nodo(value, self.length)
        if self.head == None:
            self.head = new
            self.cola = new
        else:
            actual = self.cola
            new.anterior = actual
            self.cola = new
            actual.siguiente = self.cola
        self.length += 1
    def getById(self, id):
        if self.head == None:
            return "No hay cabeza"
        else:
            if id < 0 or id >= self.length:
                return "Fuera de rango"
            else:
                actual = self.head
                while actual.id != id:
                    actual = actual.siguiente
                    return actual.value
    def contains(self,nombre):
        if self.head == None:
            return None
        else:
            actual = self.head
            while actual != None:
                if actual.value.nombre == nombre:
                    break
                else:
                    actual = actual.siguiente
                if actual != None:
                    return actual.id
                else:
                    return None
            
    def __str__(self):
        if self.head == None:
            return "[]"
        else:
            string = "["
            actual = self.head
            while actual != None:
                if actual.siguiente == None:
                    string += "{}]".format(actual)
                else:
                    string += "{},".format(actual)
                actual = actual.siguiente
            return string
        
class Cancion:
    def __init__(self, nombre, album, artista,ruta, imagen):
        self.nombre = nombre
        self.album = album
        self.artista = artista
        self.ruta = ruta
        self.imagen = imagen
    def __str__(self):
        return "Canción {}".format(self.nombre)

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
        new = Nodo(value, self.length)
        if self.head == None:
            self.head = new
            self.cola = new
            self.head.siguiente = self.cola
            self.cola.siguiente = self.head
        else:
            aux = self.cola
            self.cola = aux.siguiente = new
            self.cola.anterior = aux
            self.head.anterior = self.cola
            self.cola.siguiente = self.head
        self.length += 1
        
    def getById(self, id):
        if id < 0 or id >= self.length or self.head == None:
            return None
        else:
            actual = self.head
            while actual.id != id:
                actual = actual.siguiente
            return actual.value
    def contains(self,object):
        if self.head == None:
            return None
        else:
            actual = self.head
            while actual.siguiente != None:
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
