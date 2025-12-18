# los bucles while

import os
os.system("clear")

print("\n bucle while:")
      
contador = 0

while contador <=5:
    print(contador)
    contador += 1 

while True:
    print("Vamos a ganar mucho dinero!!!")

while False:
    print("Esto es otro mensaje infinito")



print ("\nbucle while con break:")

while True:
    print(contador)
    contador += 1 # incrementa el contador en 1
    if contador == 10: 
        break # rompe el bucle



print("\n bucle while con continue:")
      
contador = 0
while contador < 15:
    contador += 1

    if contador % 2 == 0: 
        continue # salta a la siguiente iteracion del bucle(arriba)
    print(contador) # imprime solo los numeros impares



# bucle while con else
print("\n bucle while con else:")

contador = 0
while contador < 7:
    print(contador)
    contador +=1
else:
    print(f"El bucle llego a su fin, el contador es:", contador)


numero = -1
while numero <= 0:
   try:
    numero = int(input("Introduce un numero en condiciones: "))
    if numero < 0:
        print("Esto no puede ser! , intentalo de nuevo majo/a")
   except: 
    print("No!, eso no es un numero que está en condiciones")
print(f"Gracias porfin!, has introducido el numero {numero}, que es un numero en condiciones 👍")
    