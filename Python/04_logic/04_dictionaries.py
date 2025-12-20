import os 
os.system("clear")


persona = {
    "nombre": "Bilal",
    "edad":24,
    "cuidad":"Tanger",
    "profesion": {
        "nombre": "Ciberseguridad",
        "otro_detalle": "Hala Madrid",
        "me_gusta_python": True,
    }

}

# para acceder a los valores de un diccionario usamos los valores
print(persona["nombre"])
print(persona["edad"])
print(persona["cuidad"])
print(persona["profesion"]["nombre"])
print(persona["profesion"]["otro_detalle"])
print(persona["profesion"]["me_gusta_python"])


# para cambiar un valor en un diccionario

persona ["edad"] = 25
print(persona["edad"])



# para eliminar completamente un valor en un dicicionario usamos del
del persona["profesion"]["me_gusta_python"] # lo elimina completamente

#print(persona)


# solo para eliminar un valor usamos pop
profesion_detalle = persona["profesion"].pop("otro_detalle") # lo elimina   y lo guarda en una variable
print(profesion_detalle)

#print(persona)


# sobreescribir un valor en un diccionario
a = {"nombre": "Bilal", "age" : 24, "futbolista": True}
b = {"nombre": "Cristiano", "age" : 40, "equipo": "Al Nassr"}

a.update(b) # sobreescribe los valores de a con los valores de b
print(a)


# para comprobar si existe una clave en un diccionario usamos in
print("nombre" in a)

print("futbolista" in a)

print("pizza" in b)

print("name" in persona) # false porque la clave es nombre no name



# para obtener todas las claves de un diccionario usamos keys()
print("\nclaves del diccionario persona:")
print(persona.keys())


# para obetener todos los valore de un diccionario usamos values()
print("\nValores del diccionario persona:")
print(persona.values())


# para obtener todos los elementos (clave, valor) usams items()
print("\nElementos del diccionario persona:")
print(persona.items())




for key,values in persona.items():
    print(f"{key} : {values}") 




'''  EJERCICIOS DE DICCIONARIOS  '''