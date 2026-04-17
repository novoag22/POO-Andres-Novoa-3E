class CuentaAhorro:
    def __init__(self, titular, saldo_inicial, interes_anual):
        self.__titular = titular
        self.__saldo = saldo_inicial
        self.__interes_anual = interes_anual

# Métodos que ya conocíamos (hay que volver a ponerlos)
    def consul_tit(self):
        return self.__titular

    def consul_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto debe ser positivo.")

# Método que consulta el interés anual
    def consul_interes(self):
        return self.__interes_anual

# Método para aplicar el interés anual al saldo
    def apl_interes(self):
        monto_interes = self.__saldo * (self.__interes_anual / 100)
        
        if monto_interes > 0:
            self.__saldo += monto_interes
            print(f"Se han aplicado ${monto_interes} de intereses.")
        else:
            print("No se generaron intereses.")
            
cuentaAhorro = CuentaAhorro("Juan Perez", 1500000, 10)

# TEST #

# Consulta saldo actual.

print(f"--------------------------------------")
print(f"Consultando saldo actual")
print(f"Sr/a {cuentaAhorro.consul_tit()}, su saldo actual es: {cuentaAhorro.consul_saldo()}")
print(f"--------------------------------------")

# Consultando el interes anual actual de la cuenta.

print(f"--------------------------------------")
print(f"Consultando interes de la cuenta")
print(f"El % de interes que tiene aplicado la cuenta es del: {cuentaAhorro.consul_interes()}%")
print(f"--------------------------------------")

# Aplicando el interes.
print(f"--------------------------------------")
print(f"Aplicando interes")
cuentaAhorro.apl_interes()
print(f"Su saldo con el interes anual aplicado es: ${cuentaAhorro.consul_saldo()}")
print(f"--------------------------------------")