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
