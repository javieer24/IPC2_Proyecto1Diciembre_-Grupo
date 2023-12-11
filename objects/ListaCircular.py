from objects.Nodo import Nodo

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