class producto:
    
    def __init__(self, nom_prod, precio_prod):
        self.__nom_prod = nom_prod
        self.__precio_prod = precio_prod
        
# Metodo para cambiar el precio del producto.
    def cambiar_precio (self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_prod = nuevo_precio
            print(f"El precio de {self.__nom_prod} ha cambiado. El nuevo precio es: ${self.__precio_prod}")
        else:
            print(f"El nuevo precio ingresado no es valido. El valor debe ser mayor a 0")
            print(f"El valor del articulo {self.__nom_prod} sigue siendo ${self.__precio_prod}")
            
#Metodo para consultar precio actual del producto.
    def consultar_precio(self):
        return self.__precio_prod
    
#Metodo para consultar el nombre del producto.
    def consultar_nombre(self):
        return self.__nom_prod
    
#Metodo para dar descuento.
    def dar_descuento(self, porc_desc):
        if 0 <= porc_desc <= 100:
            descuento = self.__precio_prod * (porc_desc/100)
            self.__precio_prod -= descuento
            print(f"Se ha aplicado un {porc_desc}% de descuento exitosamente. El nuevo precio del articulo {self.__nom_prod} es: ${self.__precio_prod}")
            
        else:
            print(f"El descuento ingresado no es valido. Solo valores entre 0 y 100")
            
 
 
# TEST #             
producto1 = producto ("Cama Doble Almeira", 1279000)

#Consultar nombre y precio.
print(f"Consultando nombre y precio actual del producto.")
print(f"{producto1.consultar_nombre()}")
print(f"${producto1.consultar_precio()}")
print(f"--------------------------------------")

#Cambio el precio del producto
print(f"Cambiando precio del producto")
producto1.cambiar_precio(1299000)
print(f"--------------------------------------")

#Dar descuento.
print(f"Aplicando descuento")
producto1.dar_descuento(20)
print(f"--------------------------------------")