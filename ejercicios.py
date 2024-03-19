# dada una lista de numeros, quitar los repetidos

lista = [1, 2, 2, 2, 3, 2, 1]

def orden(lista):
    conjunto = set(lista)
    return conjunto

print(orden(lista))

# dada una lista de numeros, juntar los repetidos y mostrar cuantos hay de cada uno 

# [1, 2, 2, 2, 3, 2, 1]

def ordenar_y_contar(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    
    elementos_unicos = sorted(frecuencia.keys())
    cantidad_por_elemento = [frecuencia[elemento] for elemento in elementos_unicos]
    
    return elementos_unicos, cantidad_por_elemento

print(ordenar_y_contar(lista))