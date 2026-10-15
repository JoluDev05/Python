mi_tuple = (1, 2, 3, 4,(10,20))

print(mi_tuple)  # Imprimir la tupla completa
print(mi_tuple[0])  # Acceder al primer elemento de la tupla
print(mi_tuple[4][0])  # Acceder al segundo elemento de la tupla anidada

mi_tuple = list(mi_tuple)  # Convertir la tupla en una lista
print(type(mi_tuple))  # Imprimir el tipo de la variable mi_tuple
mi_tuple = tuple(mi_tuple)  # Convertir la lista de nuevo en una tupla
print(type(mi_tuple))

t = (1,2,3)

x, y, z = t  # Desempaquetar la tupla en variables individuales
print(x)  # Imprimir el valor de x