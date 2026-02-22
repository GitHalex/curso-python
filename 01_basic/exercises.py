###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# print(f"Hola mi nombre es {input('¿Cuál es tu nombre? ')} y vivo en {input('¿En qué ciudad vives? ')}.", sep="\n")

### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))  # Debería mostrar <class 'int'>
print(type(b))  # Debería mostrar <class 'float'>
print(type(c))  # Debería mostrar <class 'str'>
print(type(d))  # Debería mostrar <class 'bool'>
print(type(e))  # Debería mostrar <class 'NoneType'>


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
value: int = int("12345")  # Convierte la cadena a entero
print(type(value))
value2: float = float(value)  # Convierte el entero a float
print(type(value2))
entero: int = int(3.99)  # Convierte el float a entero, se trunca la parte decimal
print(entero)


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
nombre: str = "midudev"
edad: int = 39
altura: float = 1.70
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")
pi: float = 3.14159
print(round(pi))  # Redondea el número PI al entero más cercano
division_entera: int = round(pi) // 2  # Realiza la división entera entre el número redondeado y 2
print(division_entera)  # De