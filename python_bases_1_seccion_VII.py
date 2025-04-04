"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion VII
"""

# Funcion basica
def di_hola():
	"""
	Simplemente dice Hola.
	"""
	print("Hola.")

di_hola()

# pasar un argumento
def di_hola(usuario):
	"""
	Simplemente dice Hola.
	"""
	print(f"Hola {usuario.title()}.")

di_hola("Toretto")

# argumentos posicionales
def descipcion_de_plantas(tipo, altura):
	"""Información de las plantas"""
	print("Características:")
	print(f"{tipo.title()}")
	print(f"{altura} cm")

descipcion_de_plantas("Albahaca",13)


descipcion_de_plantas(tipo="Albahaca", altura=13)

# valor por defecto
def descipcion_de_plantas(altura,tipo="Albahaca"):
	"""Información de las plantas"""
	print("Características:")
	print(f"{tipo.title()}")
	print(f"{altura} cm")

descipcion_de_plantas(altura=14)
descipcion_de_plantas(14)

# Returns
def nombre_del_musico(nombre, apellido):
	"""Devuelve el nombre completo del artista """
	nombre_completo = f"{nombre} {apellido}"
	return nombre_completo.title()

musico = nombre_del_musico("David","Gilmour")
print(musico)

# Agumento opcional
def nombre_del_artista(nombre, segundo_nombre, apellido):
	"""Devuelve el nombre completo del artista """
	if segundo_nombre:
		nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
	else:
		nombre_completo = f"{nombre} {apellido}"
	return nombre_completo.title()

artista = nombre_del_artista("jamie","lee","curtis")
print(artista)

# pasar una lista
def saludar_usuarios(nombres):
    """Imprime un saludo simple para cada usuario en la lista."""
    for nombre in nombres:
        mensaje = f"¡Hola, {nombre.title()}!"
        print(mensaje)

usuarios = ['hannah', 'ty', 'margot']
saludar_usuarios(usuarios)

#  argumentos arbitrarios
def hacer_pizza(*ingredientes):
    """Imprime la lista de ingredientes solicitados."""
    for i in ingredientes:    
        print(f" -{i}")

hacer_pizza('pepperoni')
hacer_pizza('champiñones', 'pimientos verdes', 'queso extra')

# argumentos posicionales y arbitrarios
def hacer_pizza(tamano, *ingredientes):
    """Imprime la lista de ingredientes solicitados."""
    print(f"Preparando una pizza de tamaño {tamano} con los siguientes ingredientes:")
    for i in ingredientes:    
        print(f" -{i}")

hacer_pizza("grande",'pepperoni')
hacer_pizza("mediana",'champiñones', 'pimientos verdes', 'queso extra')


# Importar modulos
from python_modulo_I import hacer_pizza
from python_modulo_I import hacer_pizza as hp


# Anexo
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(1000)