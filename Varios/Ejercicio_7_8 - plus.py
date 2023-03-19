from abc import ABC, abstractmethod
'''
class Persona(ABC):
    def __init__(self, nombre, apellido, edad, dni):
        while True:
            self.nombre = str(input("Ingrese Nombre: "))
            if self.nombre.isalpha()!=True:
                print("Debes ingresar un Nombre (sin números)")
                continue
            else:
                break
            
        while True:
            self.apellido = str(input("Ingrese Apellido: "))
            if self.apellido.isalpha()!=True:
                print("Debes ingresar un Apellido (sin números)")
                continue
            else:
                break

        while True:
            try:
                self.edad  = int(input("Escribe tu edad: "))
            except ValueError:
                print("Debes ingresar un número entero")
                continue
            else:
                break
        while True:
            try:
                self.dni =  int(input("Escribe tu DNI: "))
            except ValueError:
                print("Debes ingresar un número entero")
                continue
            else:
                break
    @abstractmethod
    def mostrar(self):
        pass

    def mostrar(self):
        print("Nombre: {} Apellido: {} Edad: {} DNI: {}".format(self.nombre, self.apellido, self.edad, self.dni))
        pass
    
    @abstractmethod
    def mayor_de_edad(self):
        pass

    def mayor_de_edad(self):
        if self.edad>=18:
            print("{} {} es mayor de edad.".format(self.nombre, self.apellido))
        else:
            print("{} {} NO es mayor de edad.".format(self.nombre, self.apellido))
        pass

nueva_persona = Persona("", "", "", "")
nueva_persona.mostrar()
nueva_persona.mayor_de_edad()
otra_persona = Persona("", "","" , "")
otra_persona.mostrar()
otra_persona.mayor_de_edad()
'''
#Ejercicio 7


class Cuenta(ABC):
    def __init__(self, nombre, apellido, cantidad, saldo):
        self._nombre = nombre
        self._apellido = apellido
        self._cantidad = cantidad
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

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido
        while True:
            self._apellido = str(input("Ingrese Apellido del titular: "))
            if self._apellido.isalpha()!=True:
                print("Debes ingresar un Apellido (sin números)")
                continue
            else:
                break
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad
        while True:
            try:
                self._cantidad  = float(input("Ingrese cantidad de dinero: "))
                self.saldo = self._cantidad
            except ValueError:
                print("Debes ingresar un número (puede tener decimales)")
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

    @abstractmethod
    def ingresar(self):
        pass
    def ingresar(self):
        if self.operaciones==1:
            while True:
                self.cantidad  = float(input("Ingrese cantidad de dinero a depositar: "))
                if self.cantidad >0:
                    self.saldo = self.saldo + self.cantidad
                    break
                else:
                    print("Debe ingresar una cantidad mayor a CERO.")
                    continue
            print("{} {} ha ingresado ${} y su saldo es ${}".format(self.nombre, self.apellido, self.cantidad, self.saldo))
        else:
            pass

    @abstractmethod
    def retirar(self):
        pass
    def retirar(self):
        if self.operaciones==2:
            self.cantidad  = float(input("Ingrese cantidad de dinero a retirar: "))
            self.saldo = self.saldo - self.cantidad
            print("{} {} ha retirado ${} y su saldo es ${:.2f}".format(self.nombre, self.apellido, self.cantidad, self.saldo))
        else:
            pass

    @abstractmethod
    def operacion(self):
        pass

    def operacion(self):
        while True:
            print("Seleccione tipo de Operacion:\n","1) Depósitos.\n", "2) Extracciones.\n", "3) Finalizar")
            self.operaciones = int(input("Ingrese número de Operacion: "))
            if self.operaciones ==1 or self.operaciones==2 or self.operaciones==3:
                break
            else:
                print("Ingrese un número de operación válido")
                continue
                        
    pass

    @abstractmethod
    def finalizar(self):
        pass

    def finalizar(self):
        self.operaciones == 3
    



nueva_cuenta = Cuenta("","", 0.00, 0.00)
nueva_cuenta.operacion()
nueva_cuenta.ingresar()
nueva_cuenta.retirar()
nueva_cuenta.mostrar()

# Ejercicio 8:
class Cuenta_Joven(Cuenta):
    def __init__(self, nombre, apellido, cantidad, saldo, bonificacion, titular_valido, edad):
        super().__init__(nombre, apellido, cantidad, saldo)
        self.bonificacion = bonificacion
        while True:
            try:
                self.edad  = int(input("Escribe tu edad: "))
            except ValueError:
                print("Debes ingresar un número entero")
                continue
            else:
                break
    
    
    @abstractmethod
    def es_titular_valido(self):
        pass
    def es_titular_valido(self):
        while True:
            if self.edad>=18 and self.edad<=25:
                self.titular_valido = True
                print("TITULAR VALIDO CJ")
                print(self.titular_valido)
                break
            else:
                self.titular_valido = False
                print("Titular No apto CJ")
                print(self.titular_valido)
                break
        pass

    @abstractmethod
    def mostrar_joven(self):
        pass
    
    def mostrar_joven(self):
        while True:
            if self.titular_valido == True:
                self.bonificacion = float(input("Ingrese porcentaje de bonificación: "))
                print ("Cuenta Joven con una bonificacion de {}%\n" "Titular: {} {}".format(self.bonificacion, self.nombre, self.apellido))
                break
            else:
                break
        pass

"""
nueva_cuenta_joven = Cuenta_Joven ("","", 0, 0, 0,"",0)
nueva_cuenta_joven.es_titular_valido()
nueva_cuenta_joven.mostrar_joven()
"""