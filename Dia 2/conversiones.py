num1 = 20
num2 = 30.5

#Se convierte implicitamente en float al sumarse ambos valores
num3 = num1 + num2

print(type(num1))
print(type(num2))
print(type(num3))

num4 = int(num2) #se convierte a entero, se pierde la parte decimal
print(num4)
print(type(num4))


edad = input("¿Cuántos años tienes? ")
edad = int(edad) #se convierte a entero para poder realizar operaciones matemáticas

nueva_edad = edad + 1

print(nueva_edad)