class rectangulo:
    
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho
        
        
# Metodo para cambiar la medidas iniciales del rectangulo.
    def cambiar_medidas (self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
            print(f"Nuevas dimensiones configuradas exitosamente")
            
        else:
            print(f"Valores invalidos. Tanto el largo como el ancho deben ser mayores a 0")
            
#Metodo para calcular el área.

    def calc_area(self):
        return self.__largo * self.__ancho
    
# Metodo para calcular el perimetro.

    def calc_perimetro(self):
        return 2 * (self.__largo + self.__ancho)
    
# Metodo para consultar dimensiones actuales del rectangulo.

    def consul_dimensiones(self):
        return f"Largo: {self.__largo}, Ancho: {self.__ancho}"
    
rectangulo1=rectangulo(14, 7)

# TEST #

# Consulta dimensiones actuales
print(f"Consultando dimensiones del rectangulo")
print(f"{rectangulo1.consul_dimensiones()}")

# Calculo del área y el perimetro
Area = rectangulo1.calc_area()
Perimetro = rectangulo1.calc_perimetro()
print(f"El área del rectangulo es: {Area}")
print(f"El perimetro del rectangulo es: {Perimetro}")

# Test con valores invalidos

# Cambiando valores
print(f"Validando con valores invalidos")
rectangulo1.cambiar_medidas(0, -4)

# Validando los valores despues del error.
print(f"Consultando de nuevo los valores")
print(rectangulo1.consul_dimensiones())