diccionario = []
cantidad= []

j = int(input('Ingrese cantidad de elementos a agregar al diccionario: '))
k=j
i=0
while j!=0:
   
    palabra = input('Ingrese Palabra al diccionario: ')
    diccionario.insert(i,palabra)
    i=i+1
    j=j-1
    diccionario.sort()
print(diccionario)
i=0
while k!=0:

    cantidad.insert(i, (diccionario.count(diccionario[i])))
    print(("la palabra {word} aparece {count} veces").format(word=diccionario[i], count=cantidad[i]))
    i=i+1
    k=k-1

#tupla

mayor_repetida_tupla=()
palabra,cantidad = mayor_repetida_tupla