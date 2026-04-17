class biblioteca:
    def __init__(self, titulo, autor, num_pag):
        self.titulo = titulo
        self.autor = autor
        self.num_pag = num_pag
        

    def info_libro(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"# Páginas: {self.num_pag}")
        
    def actualiza_pag(self, nuevas_pag):
        self.num_pag = nuevas_pag
        print("El número de páginas se ha actualizado")
        

libro1 = biblioteca("Habitos Atomicos", "James Clear", "456 pg")
libro2 = biblioteca("Harry Potter y la piedra filosofal", "J. K. Rowling", "264 pg")


# ____________TEST_______________

# Muestra las info del libro 1
print("Libro 1:")
libro1.info_libro()
print(f"")

# Actualizar las páginas
libro1.actualiza_pag(479)
print(f"")

# Mostrar información actualizada
print("Libro 1 actualizado:")
libro1.info_libro()
print(f"")

#________________________________________________________

# Muestra las info del libro 2
print("Libro 2:")
libro2.info_libro()
print(f"")

# Actualizar las páginas
libro2.actualiza_pag(301)
print(f"")

# Mostrar información actualizada
print("Libro 2 actualizado: ")
libro2.info_libro()