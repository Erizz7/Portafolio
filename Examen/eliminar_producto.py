from inventario import *

def eliminar_producto(inventario):
    nombre = input("Ingresa el nombre del producto a eliminar: ")
    inventario.eliminar_producto(nombre)
