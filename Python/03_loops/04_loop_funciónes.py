
''' definicion de una funcion te permite agrupar un conjunto de instrucciones bajo un nombre concreto para luego poder reutilizarlas tantas veces como queramos simplemente llamando a la funcion por su nombre. Las funciones en Python se definen con la palabra reservada def seguida del nombre de la funcion y parentesis que pueden incluir parametros o argumentos que la funcion puede recibir para trabajar con ellos. Despues de los parentesis va dos puntos y el bloque de codigo indentado que conforma el cuerpo de la funcion.
'''


# ejemplo de una funcion

def saludar():
 print("hola!")

saludar()
saludar()

# ejemplo de una funcion con parametro
def saludar_a(nombre):
  print(f"hola {nombre}!")

saludar_a("midudev")
saludar_a("xmr")  


#fuciones con mas parametros

def sumar(a,b):
  suma = a + b
  return suma

resul = sumar(2,5)
print(resul)

Documentar las funciones con docstring

def restar(a,b):
  '''Resta dos numeros y devuelve el resulado'''
  return a -b 

# print(restar.__doc__) # acceder a la descripcionde la funcion dentro de Python

help(restar) 

# parametro por defecto
def multiplicar(a, b= 2):
    '''Multiplica dos números y devuelve el resultado'''
    return a * b

print(multiplicar(2,3))

# argumentos por clave
def describir_persona(nombre,edad,sexo):
  print(f"soy {nombre},tengo {edad} años y me iedentifico como {sexo}")
 
# parametros pror posición
describir_persona("Bilal",25,"hombre")

# parametros nombrados el orden no importa

describir_persona(sexo="hombre",nombre='XMR', edad=26)

# argumentos de longitud variable

def sumar_numeros(*args):
  suma= 0
  for numero in args:
    suma += numero
  return suma 

print(sumar_numeros(1, 2, 3, 4))
print(sumar_numeros(2,7))
print(sumar_numeros(2,3,4,5,6,7,8,9))


# argumentos de clave-valor variable
def mostrar_informacion_de(**kwargs):
  for clave,valor in kwargs.items():
      print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="xmr", edad= 23, sexo="varon")
print("\n")
mostrar_informacion_de(nombre="adbduzan", es_sub=True , country="Rusia")
print("\n")
mostrar_informacion_de(nombre="CR7", is_rich=True,es_mod=True, avestruz=30)