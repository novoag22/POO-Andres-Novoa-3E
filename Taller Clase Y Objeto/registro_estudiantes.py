class estudiantes:
    def __init__(self, nombre, id, programa, nota_final):
        self.nombre = nombre
        self.id = id
        self.programa = programa
        self.nota_final = float (nota_final)
 
 #Metodo para mostrar la información del estudiante.
    def info_estudiante(self):
        print(f"Nombre del estudiante: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Programa: {self.programa}")
        print(f"Nota final: {self.nota_final}")
        
 #Metodo para calificar al estudiante.               
    def calificador(self):
        if self.nota_final >= 3.0:
            print(f"El estudiante ha aprobado el semestre")
        
        else:
            print(f"El estudiante no ha aprobado el semestre")
            

estudiante1 = estudiantes ("Pepito Perez", "1357924680", "Ingeniería de sistemas", 4.5)
estudiante2 = estudiantes ("Juanito Gonzalez", "1234567890", "Administración de empresas", 3.0)
estudiante3 = estudiantes ("Pedrito Ramirez", "2468013579", "Ingeniería industrial", 2.5 )

# TEST #

# Información estudiante y evaluación final.
print(f"Información del Estudiante 1")
estudiante1.info_estudiante()
print(f"")

print(f"Resultado academico final:")
estudiante1.calificador()
print(f"----------------------------------")

# Información estudiante y evaluación final.
print(f"Información del Estudiante 2")
estudiante2.info_estudiante()
print(f"")

print(f"Resultado academico final:")
estudiante2.calificador()
print(f"----------------------------------")

# Información estudiante y evaluación final.
print(f"Información del Estudiante 3")
estudiante3.info_estudiante()
print(f"")

print(f"Resultado academico final:")
estudiante3.calificador()
print(f"----------------------------------")