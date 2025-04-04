"""
Ejemplo de modulo para almacenar funciones
"""

def hacer_pizza(tamano, *ingredientes):
    """Imprime la lista de ingredientes solicitados."""
    print(f"Preparando una pizza de tamaño {tamano} con los siguientes ingredientes:")
    for i in ingredientes:    
        print(f"- {i}")