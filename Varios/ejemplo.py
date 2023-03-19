num1 = int(input("Ingrese Número A: "))
j = 0
i = 1
for i in range (num1):
    i = i + 1
    if num1 % i == 0:
        j = j + 1
        print (i)
        
if j < 10:
    print(num1, "es numero primo.") 
else:
    print(num1, "NO es numero primo.") 

