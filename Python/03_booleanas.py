# Tabla de la verdad de los operadores 

import os
os.system("clear")

print("\n tablas de la verdad:")
print("\n AND:")
print("A          B        A and B")
print("true       true     ", True and True)
print("true       false    ", True and False)
print("false      true     ", False and True)
print("false      false    ", False and False)



print("\n or:")
print("A         B         A or B")
print("true     true ",      True or True)
print("true     false ",     True or False)
print("false    true ",      False or True)
print("false    false ",     False or False) 


print("\n not:")
print("A         not A")
print("true     ",     not True)
print("false    ",    not False)




''' Ejercicio de comparación/ errores comunes '''
numero = 7 # asignacion

es_el_tres = numero == 3 # comparacion


if es_el_tres:
    print("el numero es tres")
# EJERCICIOS DE GIT


print("\n ternarias:")

# es una forma corta de escribir un if/else
# valor_si_verdadero if condicion else valor_si_falso

edad  = 18 
mensaje = "tienes la edad perfecta para corrar" if edad >= 18 else "Eres menor de edad chiquillo"
print(mensaje) 

