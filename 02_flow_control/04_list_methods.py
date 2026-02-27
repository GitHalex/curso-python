###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

from os import system
if system("clear") != 0: system("cls")

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia un índice
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
print("####################")
lista_numeros = [1, 2, 3, 4, 5]
# Añade el número 6 al final usando append().
lista_numeros.append(6)
# Inserta el número 10 en la posición 2 usando insert().
lista_numeros.insert(2, 10)
# Modifica el primer elemento de la lista para que sea 0.
lista_numeros[0] = 0
# Imprime la lista resultante.
print(lista_numeros)


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
lista_a.extend(lista_b)
print("Lista A después de extender con lista B:", lista_a)
# Elimina la primera aparición del número 1 en lista_a usando remove().
lista_a.remove(1)
print("Lista A después de eliminar la primera aparición de 1:", lista_a)
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
elemento_eliminado = lista_a.pop(3)
print("Elemento eliminado:", elemento_eliminado)
print("Lista A después de eliminar el elemento en índice 3:", lista_a)
# Limpia completamente lista_b usando clear().
lista_b.clear()
print("Lista B después de limpiarla:", lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
numeros_diez = list(range(1, 11))
print("Lista de números del 1 al 10:", numeros_diez)
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
del numeros_diez[2:5]
print("Lista después de eliminar los elementos del índice 2 al 4:", numeros_diez)
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
numeros = [5, 2, 8, 1, 9, 4, 2]
# Ordena la lista de forma ascendente usando sort().
numeros.sort()
print("Lista ordenada:", numeros)
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
print("Número de veces que aparece el 2:", numeros.count(2))
# Comprueba si el número 7 está en la lista usando in.
print("¿Está el número 7 en la lista?", 7 in numeros)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
original = [1, 2, 3]
# Crea una copia de la lista original llamada copia_1 usando slicing.
copia_1 = original[:]
# Crea otra copia llamada copia_2 usando copy().
copia_2 = original.copy()
# Crea una referencia a la lista original llamada referencia.
referencia = original
# Modifica el primer elemento de la lista referencia a 10.
referencia[0] = 10
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("Original:", original)
print("Copia 1:", copia_1)
print("Copia 2:", copia_2)
print("Referencia:", referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
cadenas = ["Manzana", "pera", "BANANA", "naranja"]
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
cadenas.sort(key=str.lower)
print("Cadenas ordenadas sin diferenciar mayúsculas y minúsculas:", cadenas)