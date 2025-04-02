"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion VI
"""

# Uso de input
message = input("¿Cómo te llamas?: ")
print(message)

# Uso de input numerico 
message = int(input("¿Cuántos años tienes?: "))
print(message)

numero = int(input("Par o Impar: "))

if numero % 2 == 0:
	print("Par")
else:
	print("Impar")

# While
numero = 1
while numero <= 5:
	print(numero)
	numero += 1

# Flags
prompt = 'Di algo: '

activo = True
while activo:
	message = input(prompt)

	if message == 'salir':
		activo = False
	else:
		print(message)

# Brake
prompt = "Hola: "

while True:
	message = input(prompt)

	if message == 'salir':
		break
	else:
		print(message)

# Continue

numero = 0
while numero < 0:
	numero += 1
	if numero % 2 == 0:
		continue

	print(numero)

# Anexo
edad = 0
while edad < 18:
    edad = edad + 1
    print("Felicidades, tienes " + str(edad))

while True:
    entrada = input("> ")
    if entrada == "adios":
        break
    else:
        print(entrada)

salir = False
while not salir:
    entrada = input("> ")
    if entrada == "adios":
        salir = True
    else:
        print(entrada)

edad = 0
while edad < 18:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print("Felicidades, tienes " + str(edad))