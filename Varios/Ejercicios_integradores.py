#DIVISORES PRIMOS DE UN NUMERO
"""
num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))
i=2
j=2

while num1 !=1:
    modulo = num1%i
    if modulo == 0:
        num1 = num1 / i
        print (i,  " y ", num1)
        
        
    else : 
        
        i=i+1
print ("segundo numero")
while num2 !=1:
    modulo2 = num2%j
    if modulo2 == 0:
        num2 = num2 / j
        print (j,  " y ", num2)
    else : 
        j=j+1

"""
"""
#MCD siempre es igual o menor que el mayor de los numeros
def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a
a = int(input("ingrese primer numero: "))
b = int(input("ingrese segundo numero: "))

resultado = maximo_comun_divisor(a, b)
print(
    f"El Máximo común divisor de {a} y {b} es {resultado}.")
"""
"""
# mcm siempre es igual o mayor que el mayor de los numeros
def minimo_comun_multipo (a,b,):
    if a-b>0:
        i=1
        modulo= 1
        while modulo!=0:
            modulo = a*i%b
            
            resultado = i*a
            i= i+1
        return resultado
    else:
        i=1
        modulo= 1
        while modulo!=0:
            modulo = b*i%a
            
            resultado = i*b
            i= i+1
        return resultado

a = int(input("ingrese primer numero: "))
b = int(input("ingrese segundo numero: "))

mcm = minimo_comun_multipo(a, b)
print(
    f"El mcm de {a} y {b} es {mcm}.")

"""

#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''
palabra = str( input('Ingrese la palabra a agregar al diccionario: '))
while palabra !='0':
    if palabra != '0':
        print (palabra)
        palabra = str( input('Ingrese la palabra a agregar al diccionario: '))
    else:
        print (palabra)
       
print("El programa ha finalizado")
'''
