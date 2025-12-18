# permte ejecutar un bloque de codigo un numero determinado de veces mientras itera un iterable o una lista

print("\nbucle for")

frutas = [ "cereza", "manzana", "Aguacate", "naranja", "platano"]
for fruta in frutas:
    print(fruta)

 #tierar una lista 
cadena = "Ransomware"
for caracter in cadena:
    print(caracter)

#Recuperar el indice 
frutas = [ "cereza", "manzana", "pera", "naranja", "platano"]
for index ,fruta in enumerate(frutas):
 print(f"El indice es {index} y la fruta es {fruta}")

# bucles anidados
print("\n bucles anidados")

numeros = [1,2]
hackers = ["Neo", "Morpheus", "Trinity"]

for numero in numeros:
    for hacker in hackers:
        print(f"{hacker} tiene el numero {numero}")

# break y continue en bucles for 

print("\n bucle for con break:")

animales = ["avestruz", "aguila", "gallina", "pinguino", "canario"]
for idx ,animal in enumerate(animales):
  print(animal)
  if animal == "pinguino":
      print(f"el pinguino esta muy fuerte hoy en el índice {idx}") 
      break ;

# continue
print("\n continue")

for idx ,animal in enumerate(animales):
  if animal == "aguila":
    continue # salta a la siguiente iteracion del bucle sin mostrar la aguila
  print(animal);


# comprension de listas 
animales = ["avestruz", "aguila", "gallina", "pinguino", "canario"]
animales_mayus =[animal.upper() for animal in animales] # convierte a mayusculas cada animal de la lista animales
print(animales_mayus)

# Muesta los numeros pares
pares = [num for num in [1,2,3,4,5,6,7,8]if num % 2 == 0]
print(pares)