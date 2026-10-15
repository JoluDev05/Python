nombre = "karina "
mensaje = "******\nPiso mojado \nno correr\n******" #salto de linea
poema = """Mil pequeños peces blancos
como si hirivera
el color del agua
""" #se puede usar triple comilla para escribir un texto largo

print(nombre * 3) #Repite el texto la cantidad de veces que se le indique
print(mensaje)
print(poema)

print("agua" in poema) #Busca si la palabra esta en el texto y devuelve un booleano
print(len(poema)) #Devuelve la cantidad de caracteres que tiene el texto