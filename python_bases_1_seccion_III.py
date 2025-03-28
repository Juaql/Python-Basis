"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion III
"""

# Lista de numeros
numeros = [3,2,1]

# Loop for
for n in numeros:
	print(n)

for num in range(1,6):
	print(num)
	
# Crear una lista con range()
numeros= list(range(1,6))
print(numeros)

# Saltarse numeros con range()
numeros_impares= list(range(1,15,2))
print(numeros_impares)

# Aplicar funcion matemarica de cuadrados
cuadrados = []

for numero in range(1,15,2):
	cuadrado = numero ** 2
	cuadrados.append(cuadrado)

print(cuadrados)

# Otras funciones
numeros = [1,5,2,8,9]
min(numeros)
max(numeros)
sum(numeros)

# Otra manera de obtener los cuadrados
# De esta forma se escriben menos lineas de codigo

cuadrados = [numero**2 for numero in range(1,15,2)]
print(cuadrados)

# Slicing
numeros = [1,2,3,4,5]
print(numeros[0:3])

print(numeros[1:3])

print(numeros[:3])

print(numeros[-3:])

otros_numeros = numeros[:]

# Tuplas
dimensiones = (100,50)
print(dimensiones[0])
print(dimensiones[1])

# Cambiar una tupla
dimensiones = (100,50)
print(dimensiones)

dimensiones = (200,50)
print(dimensiones)

# Otros metodos para iteraciones
# for
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# range
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# items
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# reversed
for i in reversed(range(1, 7, 2)):
    print(i)

# sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# sorted set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)