"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion II
"""

# Crear una lista

autos = ["nissan","chevrolet","ford"]
print(autos)

# Seleccionar elemetno de una lista

print(autos[0])

# Metodos de strings sobre elemento de una lista

print(autos[0].title())
print(autos[-1].upper())

# Ejemplo

message = f"Mi primer auto fue un {autos[1].title()}."
print(message)

# Modificar una lista

autos_modificados = autos
autos_modificados[0] = "renault"
print(autos)

# Agregar dato una lista

agregar_auto = autos
agregar_auto.append("ferrari")
print(autos)

# Crear una lista vacia

lista_de_autos_vacia = []

lista_de_autos_vacia.append("ford")
lista_de_autos_vacia .append("ferrari")

print(lista_de_autos_vacia )

# Agregar elemento en una determinada posicion en una lista

autos.insert(0, "toyota")
print(autos)

# Eliminar elemento de una lista

del autos[0]
del autos[-1]
print(autos)


popped_autos = autos.pop()
print(popped_autos)


mi_primer_auto = autos.pop(1)
print(f"Mi primer auto fue un {mi_primer_auto.title()}.")


removed_autos = autos.remove("renault")
print(removed_autos)

# Ordenar elementos de una lista

autos = ["ford","chevrolet","renault"]
autos.sort()
print(autos)

autos.sort(reverse=True)
print(autos)

print(sorted(autos))
print(autos)

autos.reverse()
print(autos)

# Longitud de la lista

print(len(autos))

# Anexo

squares = [1, 4, 9, 16, 25]

# Contcatenado

concatenado = squares + [36, 49, 64, 81, 100]
print(concatenado)

# Requisito de datos de una lista en base a sliceing

squares = squares[2:5]
print(squares)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)
print(x[0])
print(x[0][1])
