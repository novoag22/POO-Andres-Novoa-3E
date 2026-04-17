class Estudiante:
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []
        
        
# Metodo para consultar el nombre del estudiante
    def consul_nombre(self):
        return self.__nombre
    
# Metodo para consultar el edad del estudiante
    def consul_edad(self):
        return self.__edad
    
# Metodo para las notas.
    def ingreso_notas(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
            print(f"La nota {nota} ha sido agregada a {self.__nombre}.")
        else:
            print(f"La nota {nota} es invalida. debe ingresar valores entre 0 y 100")
            
# Metodo para calcular el promedio 
    def calc_prom(self):
        if len(self.__notas) == 0:
            return 0
        
        sum_tot = sum(self.__notas)
        promedio = sum_tot / len(self.__notas)
        return promedio
   
estudiante1 = Estudiante("Lucía Pérez", 20)

    
# TEST #


# Consultar datos básicos
print(f"+++++++++++++++++++++++++++++++++++++++++")
print(f"Consultando nombre y edad del estudiante")
print(f"Estudiante: {estudiante1.consul_nombre()}")
print(f"Edad: {estudiante1.consul_edad()}")
print(f"+++++++++++++++++++++++++++++++++++++++++")

# Agregar notas
print(f"+++++++++++++++++++++++++++++++++++++++++")
print(f"Agregando notas")
estudiante1.ingreso_notas(85)
estudiante1.ingreso_notas(92)
estudiante1.ingreso_notas(110) # Para probar le validación que sea entre 0 y 100
estudiante1.ingreso_notas(78)
print(f"+++++++++++++++++++++++++++++++++++++++++")


# Calcular el promedio final
print(f"+++++++++++++++++++++++++++++++++++++++++")
print(f"Calculando promedio final del estudiante.")
promedio_final = estudiante1.calc_prom()
print(f"El promedio de {estudiante1.consul_nombre()} es: {promedio_final:.2f}")
print(f"+++++++++++++++++++++++++++++++++++++++++")