# dada una lista de numeros, quitar los repetidos

lista = [1, 2, 2, 2, 3, 2, 1]

def orden(lista):
    conjunto = set(lista)
    return conjunto

print(orden(lista))

# dada una lista de numeros, juntar los repetidos y mostrar cuantos hay de cada uno 

# [1, 2, 2, 2, 3, 2, 1]

contador = {}

for i in lista:
    if i in contador:
        contador[i] +=1
    else:
        contador[1] =1

for i, repeticiones in contador.items():
    print(i, ":", repeticiones)