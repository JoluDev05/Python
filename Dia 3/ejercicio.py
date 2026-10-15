texto = input("Ingrese un texto: ")
letras = []
texto = texto.lower()  # Convertir el texto a minúsculas para evitar problemas de mayúsculas y minúsculas

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("Cantidad de letras")

cantidad_letras1=texto.count(letras[0])
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f"Hemos encontrado {cantidad_letras1} veces la letra '{letras[0]}' en el texto ingresado.")
print(f"Hemos encontrado {cantidad_letras2} veces la letra '{letras[1]}' en el texto ingresado.")
print(f"Hemos encontrado {cantidad_letras3} veces la letra '{letras[2]}' en el texto ingresado.")

print("\n")
print("Cantidad de palabras")

palabras = texto.split()  # Dividir el texto en palabras utilizando el espacio como separador
print(f"El texto ingresado tiene {len(palabras)} palabras.")                        

print("\n")
print("Letra inicial y letra finañ")

letra_inicial = texto[0]  # Obtener la primera letra del texto
letra_final = texto[-1]  # Obtener la última letra del texto

print(f"La letra inicial del texto ingresado es: '{letra_inicial}'")
print(f"La letra final del texto ingresado es: '{letra_final}'")