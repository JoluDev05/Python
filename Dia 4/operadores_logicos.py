mi_bool = 4 > 5 and 5 > 2 # Comparar si 4 es mayor que 5 y si 5 es mayor que 2, pero solo una es tru entonces tira falso
print(mi_bool)  # Imprimir el resultado de la comparación (False)


bool2 = (5>4) and (4>2) # se puede usar parentesis para agrupar las comparaciones y que se vea mas claro
print(bool2)  # Imprimir el resultado de la comparación (True)

bool3 = 10 == 9 or 3 == 3 # si una de las comparaciones es verdadera entonces tira verdadero
print(bool3)  # Imprimir el resultado de la comparación (True)

texto = "esta frase es breve"

bool4 = "esta" in texto and "es" in texto # si una de las comparaciones es falsa entonces tira falso
print(bool4)  # Imprimir el resultado de la comparación (True)

bool5 = not ("a" == "a") # el operador not invierte el resultado de la comparacion, si es verdadero entonces tira falso y viceversa
print(bool5)  # Imprimir el resultado de la comparación (False)