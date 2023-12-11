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
