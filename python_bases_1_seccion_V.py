"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion V
"""

# Crear y acceder a los datos de un diccionario
plantas =  {"nombre":"albahaca","altura":"12 cm"}

print(plantas["nombre"])
print(plantas["altura"])

# Añadir un dato
plantas["dias"] = 7
print(plantas)

# Modificar un dato
plantas["nombre"] = "romero"
print(plantas)

# Eliminar un dato
del plantas["dias"]

# Metodo get()
altura = plantas.get("altura", "No se tiene información de la altura.")
                     
student = {
    "nombre": "Alice",
    "edad": 22,
    "carrera": "Computer Science"
}

# Usando un bucle for para recorrer el diccionario
for k, v in student.items():
    print(f"{k}: {v}")


for k in student.keys():
	print(f"{k}")

# Anidar (Nested)
accion_0 = {"ticker":"AAPL","close":100}
accion_1 = {"ticker":"MMM","close":90}
accion_2 = {"ticker":"TTT","close":80}

acciones = [accion_0, accion_1, accion_2]
print(acciones)

users = { 
	'aeinstein': { 
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton', 
		},

	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	}, 
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location'] 

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
