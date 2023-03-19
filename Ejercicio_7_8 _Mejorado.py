from abc import ABC, abstractmethod
import random
#Ejercicio 7


class Cuenta(ABC):
    def __init__(self, nombre, apellido, cantidad, saldo, numero_cuenta):
        self._nombre = nombre
        self._apellido = apellido
        self._cantidad = cantidad
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    @property # getter
    def nombre(self):
        #print("getter nombre called")
        return self._nombre
    
    @nombre.setter #setter
    def nombre(self, nuevo_nombre):
        #print("setter nombre called")
        self._nombre = nuevo_nombre
        
    @property
    def apellido(self):
        #print("getter apellido called")
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        #print("setter apellido called")
        self._apellido = nuevo_apellido    

    @property
    def cantidad(self):
        #print("getter cantidad called")
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        #print("setter cantidad called")
        self._cantidad = nueva_cantidad

    @property # getter
    def numero_cuenta(self):
        #print("getter cuenta called")
        return self._numero_cuenta
    
    @numero_cuenta.setter #setter
    def numero_cuenta(self, nueva_cuenta):    
        #print("setter cuenta called")
        self._numero_cuenta = nueva_cuenta

    @abstractmethod
    def nombrar_nombre(self):
        pass

    def nombrar_nombre(self):
        while True:
            self.nombre = str(input("Ingrese Nombre del titular: "))
            if self.nombre.isalpha()!=True:
                print("Debes ingresar un Nombre (sin números)")
                continue
            else:
                break
            
    @abstractmethod
    def nombrar_apellido(self):
        pass

    def nombrar_apellido(self):
        while True:
            self.apellido = str(input("Ingrese Apellido del titular: "))
            if self.apellido.isalpha()!=True:
                print("Debes ingresar un Apellido (sin números)")
                continue
            else:
                break

    @abstractmethod
    def cantidades(self):
        pass

    def cantidades(self):
        while True:
            try:
                self.cantidad  = float(input("Ingrese cantidad de dinero en cuenta: "))
            except ValueError:
                print("Debes ingresar un número (puede tener decimales)")
                continue
            else:
                break
        self.saldo = self.cantidad
        
    @abstractmethod
    def operacion(self):
        pass

    def operacion(self):
        while True:
            print("Seleccione tipo de Operacion:\n","1) Depósitos.\n", "2) Extracciones.\n", "3) Finalizar")
            self.operaciones = int(input("Ingrese número de Operacion: "))
            if self.operaciones ==1:
                while True:
                    try:
                        self.cantidad  = float(input("Ingrese cantidad de dinero a depositar: "))
                        if self.cantidad >0:
                            self.saldo = self.saldo + self.cantidad
                            print("")
                            print("{} {} ha ingresado ${} y su saldo es ${:.2f}".format(self.nombre, self.apellido, self.cantidad, self.saldo))
                            print("")
                            break
                        else:
                            print("Debe ingresar una cantidad mayor a CERO.")
                        continue
                    except ValueError:
                        print("Debes ingresar un número (puede tener decimales)")
                        continue
                
            if self.operaciones==2:
                while True:
                    try:        
                        self.cantidad  = float(input("Ingrese cantidad de dinero a retirar: "))
                        self.saldo = self.saldo - self.cantidad
                        print("")
                        print("{} {} ha retirado ${} y su saldo es ${:.2f}".format(self.nombre, self.apellido, self.cantidad, self.saldo))
                        print("")
                        break
                    except ValueError:
                        print("Debes ingresar un número (puede tener decimales)")
                        continue
                
            if self.operaciones==3:
                print("Muchas gracias por operar con nosotros!")
                break
                
            elif self.operaciones>3:
                print("Ingrese un número de operación válido")
                continue

    pass
 
    @abstractmethod
    def otra_operacion(self):
        pass

    def otra_operacion(self):
        while True:
            print("¿Desea realizar otra Operacion?\n","1) Depósitos.\n", "2) Extracciones.\n", "3) Finalizar")
            self.operaciones = int(input("Ingrese número de Operacion: "))
            if self.operaciones ==1 or self.operaciones==2 or self.operaciones==3:
                break
            else:
                print("Ingrese un número de operación válido")
                continue
                        
    pass
 
    @abstractmethod
    def mostrar(self):
        pass

    def mostrar(self):
        print("Nombre del titular: {} {} cantidad en cuenta: {} N°Cuenta: {}".format(self.nombre, self.apellido, self.saldo, self.numero_cuenta))
  
nueva_cuenta = Cuenta("","", 0, 0, 0)
nueva_cuenta.nombrar_nombre()
nueva_cuenta.nombrar_apellido()
nueva_cuenta.cantidades()
nueva_cuenta.numero_cuenta = random.randint(1, 100)
nueva_cuenta.operacion()
nueva_cuenta.mostrar()

# Ejercicio 8:
class Cuenta_Joven(Cuenta):
    def __init__(self, nombre, apellido, cantidad, saldo, numero_cuenta, bonificacion, edad):
        super().__init__(nombre, apellido, cantidad, saldo, numero_cuenta)
        self._bonificacion = bonificacion
        self._edad = edad

    @property # getter
    def bonificacion(self):
        #print("getter bonificacion called")
        return self._bonificacion
    
    @bonificacion.setter #setter
    def bonificacion(self, bonificacion_asignada):
        #print("setter bonificacion called")
        self._bonificacion = bonificacion_asignada
        
    @property
    def edad(self):
        #print("getter edad called")
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        #print("setter edad called")
        self._edad = nueva_edad 

    @property # getter
    def nombre(self):
        print("getter nombre called")
        return self._nombre


    @abstractmethod
    def ingrese_edad(self):
        pass

    def ingrese_edad(self):    
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
                print("TITULAR VALIDO CJ {}".format(self.titular_valido))
                #print(self.titular_valido)
                break
            else:
                self.titular_valido = False
                print("Titular No apto CJ {}" .format(self.titular_valido))
                #print(self.titular_valido)
                break
        pass

    @abstractmethod
    def mostrar_joven(self):
        pass
    
    def mostrar_joven(self):
        while True:
            if self.titular_valido == True:
                self.bonificacion = float(input("Ingrese porcentaje de bonificación: "))
                print ("Cuenta Joven con una bonificacion de {}%\n" "Titular: {} {}\n" "Numero de cuenta: {}".format(self.bonificacion, nueva_cuenta.nombre, nueva_cuenta.apellido, nueva_cuenta.numero_cuenta))
                #print ("Cuenta Joven con una bonificacion de {}%\n".format(self.bonificacion))
                break
            else:
                print("nada que mostrar")
                break
        pass
    
    @abstractmethod
    def retirar_Cj(self):
        pass
    def retirar_Cj(self):
        if self.titular_valido == True:
                print("")
                print("Está Habilitado para retirar dinero.")
                print("")
                self.cantidad  = float(input("Ingrese cantidad de dinero a retirar: "))
                nueva_cuenta.saldo = nueva_cuenta.saldo - self.cantidad
                print("{} {} ha retirado ${} y su saldo es ${:.2f}".format(nueva_cuenta.nombre, nueva_cuenta.apellido, self.cantidad, nueva_cuenta.saldo))
                print("\nEl programa ha finalizado!")
        else:
            print("")
            print("NO está Habilitado para retirar dinero.")
            print("\nEl programa ha finalizado!")

            pass


nueva_cuenta_joven = Cuenta_Joven("","",0,0,0,0,0)
# nueva_cuenta_joven.nombrar()
nueva_cuenta_joven.ingrese_edad()
nueva_cuenta_joven.es_titular_valido()
nueva_cuenta_joven.mostrar_joven()
nueva_cuenta_joven.retirar_Cj()