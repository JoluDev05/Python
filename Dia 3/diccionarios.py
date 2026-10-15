diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
resultado = diccionario["clave2"]
print(diccionario)
print(resultado)

cliente = {"nombre": "Juan", "apellido": "perez", "edad": 30, "ciudad": "Madrid"}
print(cliente["nombre"])

dic = {"c1": ["a","b","c"],
       "c2": ["d","e","f"],
       }

print(dic["c2"][1].upper()) #extraer el valor "e" y convertirlo a mayúscula

dic["c3"] = ["g","h","i"] #agregar un nuevo elemento al diccionario
print(dic)