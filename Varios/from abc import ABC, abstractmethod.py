from abc import ABC, abstractmethod

class Cuenta(ABC):
    def __init__(self, nombre, apellido, cantidad, saldo):
        self._nombre = nombre
        self.apellido = apellido
        self.cantidad = cantidad
        self.saldo = saldo
        
    
       

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

        while True:
            self._nombre = str(input("Ingrese Nombre del titular: "))
            if self._nombre.isalpha()!=True:
                print("Debes ingresar un Nombre (sin números)")
                continue
            else:
                break
            


        @abstractmethod
        def mostrar(self):
            pass

        def mostrar(self):
            if self.operaciones == 3:
                print("Nombre del titular: {} {} cantidad en cuenta: {}".format(self.nombre, self.apellido, self.saldo))
            else:
                pass
            pass