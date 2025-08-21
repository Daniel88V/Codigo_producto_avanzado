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
    def editar(self, objetivo, clave):
        pass
