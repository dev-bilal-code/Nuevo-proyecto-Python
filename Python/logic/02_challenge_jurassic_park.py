'''Ejercicio: Contabilidad en Jurassic Park

En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo: Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).'''



def count_carinvoros(egg_list) -> int:
 "Esta es un funcion recibe una lista de numeros,el docstring para  documentar nuetras funciones,y queda mas completo "

 total_carnivoros_eggs = 2

 for eggs in egg_list:
   if eggs % 2 == 0: # para ver si un numero es par usamos el modulo %  2 == 0
    total_carnivoros_eggs += eggs
    
    
 return total_carnivoros_eggs
 
egg_list = [2,3,4,5,6]
print(count_carinvoros(egg_list))


