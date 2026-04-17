class Libro:

    def __init__(self, titulo, autor, num_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = num_paginas
        self.__pag_actual = 1
        
# Metodo para pasar las paginas con la validación que no se pase del total de páginas.

    def pasar_pag (self, cant_pag):
        nueva_pag = self.__pag_actual + cant_pag
        
        if nueva_pag <= self.__num_paginas:
            self.__pag_actual = nueva_pag
            print(f"Has avanzado {cant_pag} páginas. Te encuentras en la página # {self.__pag_actual}")
        else:
            print(f"No puedes pasar a la página {nueva_pag} porque el libro solo tiene {self.__num_paginas} páginas.")
            
# Metodo para retroceder páginas con la validación que no se pase de la pagina 1.

    def regresar_pag (self, cant_pag):
        nueva_pag = self.__pag_actual - cant_pag
        
        if nueva_pag >= 1:
            self.__pag_actual = nueva_pag
            print(f"Has regresado {cant_pag} páginas. Te encuentras en la página # {self.__pag_actual}")
        else:
            print(f"No puedes retroceder a la página {nueva_pag}. No se puede estar mas allá de la página 1")
            
# Metodo para consultar la página actual.

    def consul_pag_actual(self):
        return self.__pag_actual
    
# Metodo para consultar la información completa del libro.

    def consul_info_libro(self):
        return (f"Titulo: {self.__titulo}\n"
                f"Autor: {self.__autor}\n"
                f"Numero de páginas: {self.__num_paginas}\n"
                f"Página actual: {self.__pag_actual}")
        
        
libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 285)

# TEST #


# Consultar info inicial
print(f"--------------------------------------")
print(f"--- Información del Libro ---")
print(libro1.consul_info_libro())
print(f"--------------------------------------")

# Avanzar algunas páginas
print(f"--------------------------------------")
print(f"--Leyendo...--")
libro1.pasar_pag(50)
print(f"--------------------------------------")

# Intentando avanzar mas allá del número de páginas
print(f"--------------------------------------")
print(f"--Intentando saltar al final...--")
libro1.pasar_pag(286) 
print(f"--------------------------------------")

# Retroceder
print(f"--------------------------------------")
print(f"--Volviendo atrás...--")
libro1.regresar_pag(20)
print(f"--------------------------------------")

# Intentando retroceder menos paginas que la 1
print(f"--------------------------------------")
print(f"Volviendo antes de la pagina 1--")
libro1.regresar_pag(32)
print(f"--------------------------------------")

# 6. Consultar página actual
print(f"--------------------------------------")
print(f"--¿En qué página voy?: {libro1.consul_pag_actual()}")
print(f"--------------------------------------")