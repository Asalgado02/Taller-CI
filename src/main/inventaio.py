class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.nombre in self.productos:
            self.productos[producto.nombre].cantidad += producto.cantidad
        else:
            self.productos[producto.nombre] = producto

    def remover_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]

    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre].cantidad = cantidad