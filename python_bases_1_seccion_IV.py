"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion III
"""

# Comprobar igualdad
auto = "bmw"
auto == "bmw"
auto == "Bmw"

if auto != "bmw":
	print("No es una bemba")
else:
	print("Si es una bemba")


# Comrpobar condiciones multiples
edad = 18 # Escribir años no está mal pero no es lo habitual por la ñ
edad == 18

if edad < 18:
	print("No tomes alcohol.")
else:
	print("Toma poquito.")

edad_0 = 18
edad_1 = 22

# Uso de and
edad_0 >= 18 and edad_1 >= 22

# Uso de or
edad_0 >= 18 or edad_1 >= 40

# Comrponbar si un valor esta en una lista
aderezos = ["mayonesa","mostaza","ketchup"] 
			
"mayonesa" in aderezos
"bmw" not in aderezos


# Condicion if - elif - esle
edad = 19

if edad  < 18:
	print("No tomes alcohol.")
elif edad == 18:
	print("Desde ahora podes tomar.")
else:
	print("Toma poquito.")

# Anexo
x = 40

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
