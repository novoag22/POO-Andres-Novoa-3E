class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
# Metodo para mostrar los datos de la persona.
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\n"
              f"Edad: {self.edad}")
        
# Creo la clase hija estudiante.

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
# Metodo para mostrar el grado del estudiante.

    def mostrar_grado(self):
        print(f"Grado del estudiante: {self.grado}")
        
estudiante1 = Estudiante("Andrea Romero", 14, "10°")

# Test #

# Mostrando atributos.
print(f"--------------------------------------")
print(f"Imprimiendo atributos")
print(f"Nombre: {estudiante1.nombre}\n"
      f"Edad: {estudiante1.edad}\n"
      f"Grado: {estudiante1.grado}")
print(f"--------------------------------------")

# Mostrando datos del estudiante con los metodos. Nombre, edad y grado
print(f"--------------------------------------")
print(f"Datos del estudiante. (Con los metodos)")
estudiante1.mostrar_datos()
estudiante1.mostrar_grado()
print(f"--------------------------------------")