class inventario:
    def __init__(self, nom_prod, precio_uni, stock):
        self.nom_prod = nom_prod
        self.precio_uni = precio_uni
        self.stock = stock
        
# Metodo para mostrar la info del producto.
    def info_prod(self):
        print(f"Nombre del articulo: {self.nom_prod}")
        print(f"Precio unitario: {self.precio_uni}")
        print(f"Cantidad disponible: {self.stock}")
        
# Metodo para verificar la disponibilidad.
    def verificar_disponibilidad(self, cantidad):
        if self.stock >= cantidad:
            print(f"Stock disponible para la venta")
            return True
                    
        else:
            print(f"No hay stock suficiente para la venta solicitada")
            return False

# Metodo para realizar la venta.

    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Venta realizada exitosamente")
            print(f"Nuevo stock disponible: {self.stock}")
            
        else:
            print(f"No hay stock suficiente para la cantidad solicitada. Stock actual: {self.stock}")
            
# Metodo para reabastecer stock.

    def reabastecer_stock(self, cantidad):
        self.stock += cantidad
        print(f"Cantidad ingresada al inventario exitosamente. Nuevo stock disponible: {self.stock}")
        
        
producto1 = inventario ("Laptop", 1200, 10)
producto2 = inventario ("Play Station 5", 899, 10)

# TEST #

# Verificar si hay 5 unidades disponibles
print(f"Verificando inventario")
producto1.verificar_disponibilidad(5)
print(f"------------------------------")

# Vender
print(f"Realizando venta")
producto1.vender(3)
print (f"------------------------------")

# Verfico si hay 8 unidades disponibles
print(f"Verificando inventario")
producto1.verificar_disponibilidad(8)
print(f"------------------------------")

#Intentar vender 8 unidades
print(f"Realizando venta")
producto1.vender(8)
print (f"------------------------------")

#Reabastecer el inventario
print(f"Reabasteciendo el inventario")
producto1.reabastecer_stock(10)
print (f"------------------------------")

#Validar nuevamente el inventario con 8 unidades
print(f"Verificando inventario")
producto1.verificar_disponibilidad(8)
print(f"------------------------------")

#Intentar vender nuevamente 8 unidades
print(f"Realizando venta")
producto1.vender(8)
print (f"------------------------------")