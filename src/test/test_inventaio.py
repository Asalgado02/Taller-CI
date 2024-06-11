import unittest
import sys
import os
sys.path.append(os.getcwd() + "\\..\\..\\")

from src.main.inventaio import Inventario
from src.main.producto import Producto
from io import StringIO

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()

    def test_agregar_producto(self):
        producto = Producto("Producto1", 10)
        self.inventario.agregar_producto(producto)
        self.assertEqual(len(self.inventario.productos), 1)

    def test_remover_producto(self):
        producto = Producto("Producto1", 10)
        self.inventario.agregar_producto(producto)
        self.inventario.remover_producto("Producto1")
        self.assertEqual(len(self.inventario.productos), 0)

    def test_actualizar_producto(self):
        producto = Producto("Producto1", 10)
        self.inventario.agregar_producto(producto)
        self.inventario.actualizar_producto("Producto1", 5)
        self.assertEqual(self.inventario.productos["Producto1"].cantidad, 5)

if __name__ == '__main__':
    unittest.main()