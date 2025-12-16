''' 01 - entrada de datos por consola '''


# la funcion input permite al usuario ingresar datos por consola
# nuy simple de usar
# input (mensaje a mostrar al usuario)
#con saltos de linea \n
# int (): convierte a entero
# split (): divide una cadena de texto en varias partes


nombre = input("hola!, ¿como te llamas?\n")
print(f"hola {nombre}, Encantado de conocerte!, Quieres aprender Python conmigo?!")

respuesta = input("Responde si o no:\n")
print(f"has respondido que {respuesta}! entonces vamos a empezar!")

age = input ("¿Cuantos años tienes?\n")
age = int(age)
print (f"Tienes {age} años, que bien!")


country,city = input ("¿En que pais y cuidad vives?\n").split()

print(f"vives en {country} en la cuidad de {city} me encanta la ciudad!")



#02 - sentencias condicionales

''' permiten ejecutar bloques de código dependiendo de si una condición es verdadera o falsa o si cumple cierta condición '''

import os
os.system("clear")


print("\n sentencias simples if \n")

edad = 18
if edad >= 18:
    print ("Eres mayor de edad")
    print ("ya Puedes votar por tu candidato favorito")

edad = 17
if edad <= 18:
    print ("Eres menor de edad")
    print ("Todavia no Puedes votar quien sabe cuando lo haras")



#sentencia if/else

edad = 15
if edad >= 18:
    print ("Eres mayor de edad")
    print ("ya Puedes votar por tu candidato favorito")
else:
    print (f"Eres menor de edad")
    print (f"Todavia no Puedes votar, quien sabe cuando lo haras, que pena tienes {edad} años")

#sentencia if/elif/else

nota = 9

if nota >= 9:
    print ("Excelente!")
elif nota >=7:
    print("notable!")
elif nota >=5:
    print("Aprobado!")
else:
    print("Reprobado, estudia mas la proxima vez")


#OPERADORES LOGICOS
edad = 17
tienes_carnet = True

if edad >= 18 and tienes_carnet:
    print (f"Deberias poder conducir🏎️")
else:
    print(f"no deberias poder conducir🚔🚫🙅‍♂️")


edad = 14
if edad >= 18 or tienes_carnet:
    print (f"Deberias poder conducir🏎️")
else:
    print(f"no deberias poder ni de plantartelo🚔🚫🙅‍♂️")


se_acaba_el_curso = False

if se_acaba_el_curso:
    print("Aprovecha el verano para descansar y recargar pilas")
else:
    print("Aun te queda ciber por estudiar,y la empresa")    
if not se_acaba_el_curso:
    print("Aun te queda bash por estudiar, a seguir estudiando")

edad = 20
tienes_dinero = True


if edad < 18: 
    if tienes_dinero:
        print("Puedes trabajar")
    else:
     print("Gracias a pedro sanchez!")
else:
    print("Eres un estudiante homogeneo")



