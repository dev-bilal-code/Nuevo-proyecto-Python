
import os
os.system("clear")

lista1 = [ 'a','b','c', 'd', 'e']


lista1.append('f') # añade un elemento al final de la lista
print(lista1)

lista1.insert(2, '@') # añade un elemento en la posicion 2
print(lista1)


lista1.extend (['😃','🫡',]) # añadir varios elementos a la lista
print(lista1)



# ELIMINAR ELEMENTOS DE LA LISTA
print("\nEliminar elementos de la lista:")

lista1.remove('e') # elimina solo el primer elemento con el valor 'e'
print(lista1)


ultimo = lista1.pop(-1) 
print(ultimo) # elimina el ultimo elemento de la lista y lo devuelve
print(lista1)


lista1.pop(2) # elimina el segundo elemento de la lista [índice 1]
print(lista1)


del lista1[-1]
print(lista1)


lista1.clear() # elimina todos los elementos de la lista
print(lista1)

lista1 = [ '🐼', '🐨', '🦥', '🫏']
del lista1[2:3]
print(lista1)


print("\nOrdenador elementos de la lista:")

numbers = [9,99,48,39,2,5,6,22,4,7,25,98]

numbers.sort() # ordena la lista de menor a mayor
print(numbers)

print("\n0Ordenar listas creando una nueva lista:")
sorted_numbers = sorted(numbers) # devuelve una nueva lista ordenada de menor a mayor
print(sorted_numbers)
print(numbers)



print("\nordenar una lista de cadenas de texto:")
frutas = ['naranja', 'manzana', 'kiwi', 'banana', 'cereza', 'aguacate']
sorted_frutas = sorted(frutas) # ordena la lista de cadenas de texto por orden alfabetico
print(sorted_frutas)


print("\nordnadr una lista de cadenas de texto (mezclado mayusculas y minusculas):")

frutas2 = ['naranja', 'Manzana', 'kiwi', 'Banana', 'cereza', 'Aguacate']
frutas2.sort(key=str.lower) 
print(frutas2)

nombre = ['Bilal', 'Ana', 'juan', 'Maria', 'zaira', 'Carlos']
nombre.sort(key=str.lower)
print(nombre)




# mas metodos de listas
print("\nMás métodos de listas:")

animales = ['🐼','🐱','🐨','🦁','🐱','🐯','🐱','🙈']

print("\ncontar elementos en una lista:")

print(len(animales)) # cuenta cuantos elementos hay en la lista

print(animales.count('🐱')) # cuenta cuantas veces aparece el elemento '🐱' en la lista

print(animales.count('🦁')) # cuenta cuantas veces aparece el elemento '🦁' en la lista

print("\nbuscar elementos en una lista:")
print('🐼'in animales) # comprueba si hay un '🦁' en la lista
print('🦅'in animales) # comprueba si hay un '🦅' en la lista



''' EJERCICIOS '''
''' + soluciones '''
