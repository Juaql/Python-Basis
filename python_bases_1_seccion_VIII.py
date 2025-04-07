"""
Este archivo reproduce los codigos mostrados como ejemplo en el
PDF Python I: Bases I - Seccion VII
"""

# Clae base
class Perro:
    """Modelo de perro."""

    def __init__(self, name, age):
        """Comenzar con los atributos."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulación del perro sentado."""
        print(f"{self.name} esta sentado.")

    def roll_over(self):
        """Simulación del perro rodar."""
        print(f"{self.name} rodó!")


mi_perro = Perro("Toby", 4)

print(f"Mi perro se llama {mi_perro.name}.")
print(f"Mi perro tiene {mi_perro.age} años.")

mi_perro.sit()
mi_perro.roll_over()

class Auto:
    """Un intento simple de representar un auto."""

    def __init__(self, marca, modelo, año):
        """Inicializa los atributos para describir un auto."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0

    def obtener_nombre_descriptivo(self):
        """Devuelve un nombre descriptivo con buen formato."""
        nombre_largo = f"{self.año} {self.marca} {self.modelo}"
        return nombre_largo.title()

    def leer_kilometraje(self):
        """Muestra los kilómetros que tiene el auto."""
        print(f"Este auto cuenta con {self.kilometraje} kilómetros")

    def actualizar_kilometraje(self, kilometros):
        """Actualiza los kilómetros que tiene el auto."""
        self.kilometraje = kilometros

    def incrementar_kilometraje(self, km_extra):
        """Suma una cantidad dada al valor actual del odómetro."""
        self.kilometraje += km_extra

    def llenar_tanque(self):
        """Simula llenar el tanque de combustible."""
        print("Este auto necesita llenar el tanque de combustible.")


# Crear una instancia y mostrar el nombre descriptivo
mi_auto_nuevo = Auto('audi', 'a4', 2024)
print(mi_auto_nuevo.obtener_nombre_descriptivo())

class AutoElectrico(Auto):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)  # Hereda atributos de Auto
        self.bateria = 75  # Atributo específico

    def descripcion_bateria(self):
        print(f"Este auto tiene una batería de {self.bateria} kWh.")

# Ejemplo
mi_tesla = AutoElectrico('Tesla', 'Model 3', 2024)
mi_tesla.obtener_nombre_descriptivo()
mi_tesla.descripcion_bateria()

class Bateria:
    def __init__(self, capacidad=75):
        self.capacidad = capacidad

    def describir_bateria(self):
        print(f"Esta batería tiene una capacidad de {self.capacidad}-kWh.")

class AutoElectrico:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.bateria = Bateria()  # Composición: incluye una instancia de Bateria

    def describir_auto(self):
        print(f"{self.marca} {self.modelo} ({self.año})")
        self.bateria.describir_bateria()