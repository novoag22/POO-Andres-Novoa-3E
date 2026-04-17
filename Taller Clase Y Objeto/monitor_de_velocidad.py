class vehiculo:
    
    def __init__(self, marca, modelo, vel_max):
        self.marca = marca
        self.modelo = modelo
        self.vel_max = vel_max
        self.vel_actual = 0
 
# Metodo para acelerar        
    def acelerar(self, incremento):
        nueva_velocidad = self.vel_actual + incremento
        if nueva_velocidad > self.vel_max:
            self.vel_actual = self.vel_max
            print(f"Va a la velocidad maxima de este vehiculo: {self.vel_max} Km/h")
            
        else:
            self.vel_actual = nueva_velocidad
            print(f"Acelerando. Va a {nueva_velocidad} Km/h")
            
# Metodo para desacelerar
    def descelerar(self, decremento):
        nueva_velocidad = self.vel_actual - decremento
        if nueva_velocidad <= 0:
            self.vel_actual = 0
            print(f"El vehiculo ha frenado totalmente. {nueva_velocidad} Km/h")
            
        else:
            self.vel_actual = nueva_velocidad
            print(f"Disminuyendo velocidad. La nueva velocidad es: {self.vel_actual} Km/h")
            
# Metodo para validar el limite de velocidad
    def limite(self, vel_limite):
        if self.vel_actual > vel_limite:
            print(f"¡Cuidado!. Está superando la velocidad limite permitida en esta zona")
            return True
        
        else:
            print(f"Vas dentro de los limites de velocidad permitidos en esta zona")
            return False
        
        
# Menú de opciones. TEST

automovil1 = vehiculo ("Toyota", "Land Cruiser Prado", 180)

while True:
    print(f"--- MONITOR DE VELOCIDAD---")
    print("-" * 30)
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite de velocidad")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        valor = int(input("¿Cuánto quieres acelerar?: "))
        automovil1.acelerar(valor)

    elif opcion == "2":
        valor = int(input("¿Cuánto quieres frenar?: "))
        automovil1.descelerar(valor)

    elif opcion == "3":
        limite = int(input("Ingresa el límite de la zona (ej. 80): "))
        automovil1.limite(limite)

    elif opcion == "4":
        print("Gracias por usar nuestros servicios. ¡Buen viaje!")
        break

    else:
        print("Entrada inválida. Selecciona la opción correcta.")