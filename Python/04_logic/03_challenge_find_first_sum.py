''' Búsqueda de Índices (Suma Objetivo)

Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

Ejemplo de entrada:

    nums = [4, 5, 6, 2]

    goal = 8

Ejemplo de salida:

    find_first_sum(nums, goal) # [2, 3]'''


def find_first_sum(nums, goal):
 for i in range(len(nums)):
  for x in range( i + 1, len(nums)):
   if nums[i] + nums[x] == goal:
    return [i, x]
  
  return None # No se encontro ninguna combinación

nums = [2, 4, 5, 6] # iteracion
goal = 6
result = find_first_sum(nums, goal)
print (result)




