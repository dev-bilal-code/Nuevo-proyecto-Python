# creacion de las listas




print("\n crear listas:")

lista1 = [1,2,3,4,5]
lista2 = ["aguacate", "banana", "cereza"]
lista3:list[int | str | float | bool] = [1, "dos", 3.0, True, [5,6,7]] 

lista_vacia = []
lista_de_listas = [lista1, lista2], [1, 2], ['calcetin', 4]
matrix = [[1,2,3], [4,5,6], [7,8,"oro"]]


print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)


#acceso a los elementos por indice
print("\n Acceso a elementos por indice:")
print("primer elemento de la lista1:", lista2[0])
print("segundo elemento de la lista2:", lista2[1])
print("ultimo elemento de la lista3:", lista2[-1])  # --> cuando no sabes cuales el ultimo elemento de la lista 
print(lista_de_listas[2][0])
print(matrix[2][2])


#slicing de listas

lista1 = [1,2,3,4,5,6,7,8,9,10 ]

 # print(lista1[desde:hasta])

print(lista1[:4]) # desde el inicio hasta el indice 4 
print(lista1[0:3]) # desde el indice 0 hasta el indice 3
print(lista1[2:]) # desde el indice 2 hasta el final
print(lista1[:]) # toda la lista


# HAY MÁS MAGIA EN LAS LISTAS


print("\nMás magia en las listas:")
 # print(lista1[desde:hasta:salto])

print(lista1[0:10:3]) # desde el indice 0 hasta el indice 9 (sin incluir el 9) saltando de 3 en 3
print(lista1[::-2]) # desde el final hasta el inicio saltando de 2 en 2

print("\n modificar listas:")
# modificar elementos de la lista
print("\n modificar elementos de la lista:")
lista1[0] = 77
print(lista1)


print("\n añadir elementos a la lista:")
# añadir elementos a la lista
lista1 = lista1 + [11,14,16,88] # concatenar listas
print(lista1)

# otra forma más corta y eficiente de concatener listas
lista1 += [77,99,100]
print(lista1)


# Recuperar la longitud de la lista

print(f"longitud de la lista1:", len(lista1))



#EJERCICIOS DE GIT