"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion I
"""

# Hello World con varaibles

message = "Hello world!"
print(message)

message = "Hello Python!"
print(message)

# Strings con "" y ''

texto_1 = "Esto es un string"
texto_2 = 'Esto también'

print(texto_1)

nombre_1 = "joaquin lopez"

# Metodos title, upper y lower

print(nombre_1.title())
print(nombre_1.upper())
print(nombre_1.lower())

# Uso de tabuladores (\t) y saltos (\n)

print ("\tPython")
print("Lenguajes:\n1 -Python\n2 - Francia\n3- C++")

# Combinacion de ambos

print("Lenguajes:\n1 -Python\n\t2 - Francia\n3- C++\n\n")

# Metodo rstrip

espacio_derecho = "python "
print(espacio_derecho.rstrip())

espacios = " python "
print(espacios.lstrip())
print(espacios.lstrip())

# Quitar prefijos

google_url = "https://google.com"
print(google_url.removeprefix("https://"))


# NUMEROS
# Operaciones con integers

suma = 2 + 2
resta = 2- 2
multiplicacion = 2 *2
division = 2/2
potencia = 2 ** 3

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(potencia)

# Orden de prioridades

orden_1 = 2 + 3 * 4
orden_2 = (2 + 3) * 4

print(orden_1)
print(orden_2)

# Floats

a = 0.2 + 0.2
b = 0.2 - 0.2
c = 2 * 0.1
d = 0.2 + 0.1

print(a)
print(b)
print(c)
print(d)

# Integers a floats

numero_1 = 4 / 2
print(numero_1)

numero_2 = 1 + 2.0
print(numero_2)

# Uso de guines bajos

numero_largo = 10_000_000_000_000_000
print(numero_largo)

# Asignacion de variables multiples

x, y, z = -1, 0, 1
print(y)

# Ejemplo de comentario

# Tu nombre almacenado en una variable mas arriba
print(nombre_1.title())