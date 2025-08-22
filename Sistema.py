from abc import ABC, abstractmethod
class Productos:
    def __init__(self, codigo,nombre,categoria,precio,stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
    def mostrar_producto(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoria: {self.categoria} | Precio: {self.precio} | Stock: {self.stock}"
class iBuscador(ABC):
    @abstractmethod
    def buscar(self, registro, clave):
        pass
class iAlterarProducto:
    @abstractmethod
    def eliminar(self, registro, clave):
        pass
    def editar(self, objetivo, dato):
        pass
class BusquedaSecuencial(iBuscador):
    def buscar(self, registro, clave):
        for cosa in registro.values():
            if cosa.codigo.upper() == clave.upper():
                return cosa
        return None
class AlterarProducto(iAlterarProducto):
    def eliminar(self, registro, clave):
        if clave.upper() in registro:
            del registro[clave.upper()]
            return True
        return False
    def editar(self, producto, dato):
        producto.precio = dato["precio"]
        producto.stock = dato["stock"]
        return True
class OrdenadorProductos:
    def quicks_nombre(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.nombre.upper() < pivote.nombre.upper()]
        iguales = [x for x in lista if x.nombre.upper() == pivote.nombre.upper()]
        mayores = [x for x in lista[1:] if x.nombre.upper() > pivote.nombre.upper()]
        return self.quicks_nombre(menores) + iguales + self.quicks_nombre(mayores)
    def quicks_preciomen(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.precio < pivote.precio]
        iguales = [x for x in lista if x.precio == pivote.precio]
        mayores = [x for x in lista[1:] if x.precio > pivote.precio]
        return self.quicks_preciomen(menores) + iguales + self.quicks_preciomen(mayores)
    def quicks_preciomay(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.precio < pivote.precio]
        iguales = [x for x in lista if x.precio == pivote.precio]
        mayores = [x for x in lista[1:] if x.precio > pivote.precio]
        return self.quicks_preciomen(mayores) + iguales + self.quicks_preciomen(menores)
