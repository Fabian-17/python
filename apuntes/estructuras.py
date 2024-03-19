if True != True: 
    print("True no es igual a True")
elif True == False:
    print("True es igual a False")
else:
    print("True es igual a True")

# While
    
while False:
    print("Esto se ejecutara por siempre")

# For
    
mi_lista = [1,2,3,4,5,6,7,8,9,10]

for i in mi_lista:
    print(i)


for x in range(0, 10, 2):
    print(x)

for y in range(10, 0, -1):
    print(y)

for i, x in enumerate(mi_lista):
    print(i, x)

for i in range(0, len(mi_lista)):
    print(i, mi_lista[i])

for i in "ddfgdf":
    print(i)