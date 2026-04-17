class Vehiculo:
    
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        
# Metodo para info del vehiculo.

    def mostrar_info(self):
        return (f"Marca: {self.marca}\n"
                f"Año: {self.año}")
        
# Clase hija coche.

class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo
        
# Metodo para mostrar el modelo del coche.

    def mostrar_modelo(self):
        return f"Modelo: {self.modelo}"
    
carrito = Coche("Toyota", 2026, "Land Cruiser Prado (serie 250)")

# TEST #

# Mostrar atributos.
print(f"--------------------------------------")
print(f"Imprimiendo atributos")
print(f"Marca: {carrito.marca}\n"
      f"Año: {carrito.año}\n"
      f"Modelo: {carrito.modelo}")
print(f"--------------------------------------")

# Mostrar los datos usando los metodos

print(f"--------------------------------------")
print(f"Datos del coche. (Con los metodos)")
print(f"{carrito.mostrar_info()}\n"
      f"{carrito.mostrar_modelo()}")
print(f"--------------------------------------")