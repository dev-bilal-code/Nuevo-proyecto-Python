

# import re

# pattern = "Hola"

# text = "Hola, ¿cómo estás? Hola de nuevo."

# result = re.search(pattern, text)


# if result:
#     print("¡Coincidencia encontrada!")
# else:
#     print("No se encontró ninguna coincidencia.")


# # devuelve la coincidencia encontrada con el patrón
# print(result.group())  


# # devuelve la posicion inicial de la coincidencia
# print(result.start())  

# # devuelve la posicion final de la coincidencia
# print(result.end())





# ''' EJERCICSO DE EXPRESIONES REGULARES '''

# text = "Todo el mundo dice que la IA nso va a quitar el trabajo,pero solo hacer falta ver como puede cagar con los Regexes para ir con cuidado" 

# pattern= "IA"

# result = re.search(pattern, text)

# if result:
#     print(f"he encontrado la palabra {pattern} en el texto , en la posicion{result.start()} y esta en el indice {result.end()}")
# else:
#     print("No se encontró el patron en el texto.")



# encontrar todas las coincidencias en un texto

import re


text = "python es genaial, me encanta pyxhon porque pyphon es facil de aprender"

pattern = "py.hon" # el punto . representa cualquier caracter

matches = re.findall(pattern, text)

# print(matches)  # ['pyjhon', 'pyxhon', 'pyphon']



# print(len(matches))  # len devuelve el numero de coincidencias encontradas



''' iter() devuelve un iterados con todas las coincidencias encontradas en el texto '''
text = "python es genial. me encanta pyxhon. porque pyphon es facil de aprender"

pattern = "py.hon" # el punto . representa cualquier caracter

matches = re.finditer(pattern, text)  # Cambiado de re.findall a re.finditer para obtener objetos Match

for bilal in matches:
    print(bilal.group(), bilal.start(), bilal.end())





''' modificadores: los modificadores cambian el comportamiento de la busqueda '''


# ''' EJERCICSO DE EXPRESIONES REGULARES '''

text = "Todo el mundo dice que la Ia nos va a quitar el trabajo,pero la ia es buena depende como se use la IA " 

pattern= "IA"

result = re.findall(pattern, text,re.IGNORECASE)  # re.IGNORECASE para ignorar mayusculas y minusculas


if result:print(result) 


# EJERCICIO 03
# Encuentra todas las ocurrencas de la palabra "python " en el siguiente texto,sin distinguir enre mayusculas y minusculas.


text = "Este es el curso de python de midudev.Python es un lenguaje de programacion muy popular.PYTHON es facil de aprender." 

pattern = "python"


found =re.findall(pattern,text,re.IGNORECASE)

if found: print(found) 

# reemplezar el txto
# sub() sustituye todas las ocurrencias de un patron por un texto dado

text = "Hola, mundo! Hola a todos, hola de nuevo"

pttern = "Hola" 

remplacement = "A salam aleikum"

new_text = re.sub(pttern,remplacement,text)
print(new_text)

