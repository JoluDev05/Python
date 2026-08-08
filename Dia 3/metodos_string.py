texto = "Hola, mi nombre es Jorge"
resultado = texto.upper() #Convierte el texto a mayusculas
print(resultado)
resultado = texto.lower() #Convierte el texto a minusculas
print(resultado)
resultado = texto.capitalize() #Convierte la primera letra a mayuscula y el resto a minuscula
print(resultado)
resultado = texto.split() #Convierte el texto en una lista de palabras x palabras
print(resultado)
resultado = texto.replace("Jorge", "Carlos") #Reemplaza una palabra por otra
print(resultado)

a = "Hola"
b = "Mundo"

c = " ".join([a, b]) #Une las palabras con el texto que se le indique
print(c)