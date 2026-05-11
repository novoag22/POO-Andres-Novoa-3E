# 1. CLASE BASE (Abstracción y Encapsulamiento)
class Personaje:
    def __init__(self, vida, ataque, defensa):
        self.__vida = 0
        self.set_vida(vida) # Valida la vida al nacer
        self.__ataque = ataque
        self.__defensa = defensa

    # Getters y Setters
    def get_vida(self):
        return self.__vida

    def set_vida(self, vida):
        if vida < 0:
            self.__vida = 0
        elif vida > 100:
            self.__vida = 100
        else:
            self.__vida = vida

    def get_ataque(self): return self.__ataque
    def set_ataque(self, ataque): self.__ataque = ataque

    def get_defensa(self): return self.__defensa
    def set_defensa(self, defensa): self.__defensa = defensa

    def atacar(self, objetivo):
        pass

# 2. CLASES DERIVADAS (Herencia y Polimorfismo)
class Guerrero(Personaje):
    def atacar(self, objetivo):
        ataque_real = self.get_ataque() * 1.20
        dano = ataque_real - objetivo.get_defensa()
        if dano < 0: dano = 0
        objetivo.set_vida(objetivo.get_vida() - dano)
        print(f"El Guerrero ataca con furia! Causa {dano:.1f} de daño.")

class Mago(Personaje):
    def atacar(self, objetivo):
        dano = self.get_ataque() # Ignora defensa
        objetivo.set_vida(objetivo.get_vida() - dano)
        print(f"El Mago lanza un hechizo! Causa {dano:.1f} de daño (Ignora defensa).")

class Arquero(Personaje):
    def atacar(self, objetivo):
        if self.get_ataque() > objetivo.get_defensa():
            ataque_real = self.get_ataque() * 2
        else:
            ataque_real = self.get_ataque()
            
        dano = ataque_real - objetivo.get_defensa()
        if dano < 0: dano = 0
        objetivo.set_vida(objetivo.get_vida() - dano)
        print(f"El Arquero dispara! Causa {dano:.1f} de daño.")

# 3. INTERACCIÓN CON EL USUARIO
def crear_personaje(num_jugador):
    print(f"\n--- Creación del Jugador {num_jugador} ---")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Arquero")
    
    # Ciclo para asegurar que elija una opción válida
    while True:
        opcion = input("Elige la clase de tu personaje (1/2/3): ")
        if opcion in ['1', '2', '3']:
            break
        print("Opción no válida. Intenta de nuevo.")

    # Captura de estadísticas
    vida = float(input("Ingresa la vida (0-100): "))
    ataque = float(input("Ingresa el poder de ataque: "))
    defensa = float(input("Ingresa el nivel de defensa: "))

    # Instanciación según la elección (Factory)
    if opcion == '1':
        return Guerrero(vida, ataque, defensa), "Guerrero"
    elif opcion == '2':
        return Mago(vida, ataque, defensa), "Mago"
    else:
        return Arquero(vida, ataque, defensa), "Arquero"

def iniciar_batalla(p1, p2, nombre_p1, nombre_p2):
    print(f"\n---  INICIA LA BATALLA: {nombre_p1} vs {nombre_p2}  ---")
    turno = 1
    
    while p1.get_vida() > 0 and p2.get_vida() > 0:
        input(f"\n[Presiona ENTER para iniciar el Turno {turno}]")
        print(f"--- Turno {turno} ---")
        
        # Ataca P1
        p1.atacar(p2)
        print(f"Salud de {nombre_p2}: {p2.get_vida():.1f}")
        if p2.get_vida() == 0:
            print(f"\n¡{nombre_p1} ha ganado la batalla!")
            break
            
        # Ataca P2
        p2.atacar(p1)
        print(f"Salud de {nombre_p1}: {p1.get_vida():.1f}")
        if p1.get_vida() == 0:
            print(f"\n¡{nombre_p2} ha ganado la batalla!")
            break
            
        turno += 1

# --- PUNTO DE ENTRADA DEL PROGRAMA ---
if __name__ == "__main__":
    print("Bienvenido a Guardians of the Ancient Kingdom")
    
    # Creamos ambos personajes interactivamente
    jugador1, nombre_j1 = crear_personaje(1)
    jugador2, nombre_j2 = crear_personaje(2)
    
    # Iniciamos el enfrentamiento
    iniciar_batalla(jugador1, jugador2, nombre_j1, nombre_j2)