mi_lista = [1,2,3]
mi_otra_lista = [4,5,6]
mi_grande_lista = mi_lista + mi_otra_lista #Concatena las listas

mi_grande_lista.append(7) #Agrega un elemento al final de la lista
print(mi_grande_lista)

mi_grande_lista.pop() #Elimina el ultimo elemento de la lista, si no se le indica un indice
print(mi_grande_lista)

lista_letras = ["G", "A", "B", "C"]
lista_letras.sort() #Ordena la lista de menor a mayor
print(lista_letras)

lista_letras.reverse() #Invierte el orden de la lista
print(lista_letras)