Nombre = input("¿Cuál es tu nombre? ")


ventas = int(input("¿Cuánto fue tu venta? "))

comision = round(ventas * 13 / 100, 2)

print(f"El empleado {Nombre} tuvo una venta de {ventas} y su comisión es de {comision} pesos.")