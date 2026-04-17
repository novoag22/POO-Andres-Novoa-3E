class Empleado:
    __contar_empleados = 0
    
    def __init__(self, nombre_empl, salario_empl):
        self.__nombre_empl = nombre_empl
        self.__salario_empl = salario_empl
        
        Empleado.__contar_empleados += 1
        
# Metodo de clase para el total de empleados

    @classmethod
    def cant_empleados(cls):
        return cls.__contar_empleados
    
    
# Metodo para consultar nombre del empleado

    def consul_nombre(self):
        return self.__nombre_empl
    
# Metodo para consultar salario del empleado

    def consul_salario(self):
        return self.__salario_empl
    
    
empleado1 = Empleado("Pedrito Perez", 2000000)
empleado2 = Empleado("Pepito Rodriguez", 2300000)
empleado3 = Empleado("Juanito Hernandez", 2500000)

# TEST # 

# Verificar Contador#
print(f"--------------------------------------")
print(f"Lista de empleados")
print(f"Empleado: {empleado1.consul_nombre()}ha sido creado\n"
    f"Empleado: {empleado2.consul_nombre()} ha sido creado\n"
    f"Empleado: {empleado3.consul_nombre()} ha sido creado")
print(f"Cantidad total de empleados: {Empleado.cant_empleados()}")
print(f"--------------------------------------")

# Agrego otro empleado y verifico el contador
print(f"--------------------------------------")
empleado4 = Empleado("Juancito Miranda", 1900000)
print(f"Empleado: {empleado4.consul_nombre()} ha sido creado")
print(f"Cantidad total de empleados: {Empleado.cant_empleados()}")
print(f"--------------------------------------")