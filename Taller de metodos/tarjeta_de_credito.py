class TarjetaCredito:
    def __init__(self, numero):
        self.__numero = str(numero)

    def consulta_num_tarj(self):
        return self.__numero
    
    @staticmethod
    def validador_luhn(numero):
        numero = str(numero)
        suma = 0
        alternar = False
        
        for i in range(len(numero) - 1, -1, -1):
            digito = int(numero[i])
            
            if alternar:
                digito *= 2
                if digito > 9:
                    digito -= 9
            
            suma += digito
            alternar = not alternar
            
        return suma % 10 == 0

    def es_valida(self):
        if TarjetaCredito.validador_luhn(self.__numero):
            return "Es válida."
        else:
            return "NO es válida."

tarjeta1 = TarjetaCredito("79927398713")
tarjeta2 = TarjetaCredito("79927398710")     
  
# TEST #

#Tarjeta Valida.
print(f"Validando tarjetas")
print(f"--------------------------------------")
print(f"Tarjeta 1 de número {tarjeta1.consulta_num_tarj()}: {tarjeta1.es_valida()}")
print(f"Tarjeta 2 de número {tarjeta2.consulta_num_tarj()}: {tarjeta2.es_valida()}")
print(f"--------------------------------------")