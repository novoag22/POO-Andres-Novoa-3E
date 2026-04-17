class Animal:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        
# Creo el metodo para mostrar el nombre y la especie.

    def mostrar_datos(self):
        return (f"Nombre: {self.nombre}\n"
                f"Especie: {self.especie}")
        
# Creo la clase hija

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.raza =  raza
        
# Metodo para mostrar la raza del perro.

    def mostrar_raza(self):
        return f"Raza: {self.raza}"
    

perrito = Perro("Pluto", "Canis lupus familiaris", "Pastor Aleman")

# TEST #

# Mostrar atributos.
print(f"--------------------------------------")
print(f"Imprimiendo atributos")
print(f"Nombre: {perrito.nombre}\n"
      f"Especie: {perrito.especie}\n"
      f"Raza: {perrito.raza}")
print(f"--------------------------------------")

# Mostrar los datos usando los metodos

print(f"--------------------------------------")
print(f"Datos animal. (Con los metodos)")
print(f"{perrito.mostrar_datos()}\n"
      f"{perrito.mostrar_raza()}")
print(f"--------------------------------------")