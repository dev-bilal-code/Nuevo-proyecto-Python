# casting (Conversion de tipos de datos)

# print("conversion de tipos de datos")


# convertir un tipo de dato en otro
#print(2 + int("1000"))
#
#print("888" + str(9)) #concatena cadenas de texto (juntando)

#print(777 + int("8"))



#print(type(float("9.99")))  #tipo float
#print(int(9.99 ))   #convierte a entero, elimina los decimales


#print(bool(0))  #False es el num. 0 siempre
#print(bool(8))
#print(bool(-5)) #True cualquier num. distinto de 0 es True


#print(bool("")) #la cadena de texto vacia es siempre y unica False
#print(bool(" ")) 
#print(bool("false")) #cualquier cadena de texto con contenido es True


#print(int("hola mundo")) #error no se puede convertir a entero una cadena de texto que no sea un num.

#print(round(2.5)) #convierte a entero, elimina los decimales

#print(round(3.5)) #convierte a entero al par mas cercano


''' Asignar una variable '''

#my_name = "Bilal"
#print(my_name)

#age = "21"
#print(age)

#tipado dinámico
#name = "xmr"
#print(type(name))

#age = 21
#print(type(age))

#age = 37
#print(type(age))

# tipado fuerte 

''' f-string (formatted string)  '''

my_name = "Bilal"

age = 21

estudios = "2ASIR"

print (f"hola {my_name}, tengo {age + 2} años, actualmente estoy estudiando {estudios}")



is_user_logged_in: bool= True
print(is_user_logged_in)

is_usser_logged_in = 42
print(is_usser_logged_in)