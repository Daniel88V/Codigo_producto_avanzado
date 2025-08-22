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
    def quicks_stock(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.stock < pivote.stock]
        iguales = [x for x in lista if x.stock == pivote.stock]
        mayores = [x for x in lista[1:] if x.stock > pivote.stock]
        return self.quicks_stock(menores) + iguales + self.quicks_stock(mayores)
class ValidarDatosProductos:
    @staticmethod
    def validar_datosyagegar(productos_en_existencia):
        while True:
            codigo = input("Ingrese el código del producto: ").upper()
            if not codigo:
                print("Advertencia. Campo requerido, por favor ingrese el código del producto")
            elif codigo in productos_en_existencia:
                print("Error. Este producto ya existe")
            else:
                break
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre:
                print("Advertencia. Campo requerido, por favor ingrese el nombre del producto")
            else:
                break
        while True:
            categoria = input("Ingrese la categoria del producto: ")
            if not categoria:
                print("Advertencia. Campo requerido, por favor ingrese la categoria")
            else:
                break
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if not precio:
                    print("Advertencia. Campo requerido, por favor ingrese el precio")
                elif precio <= 0:
                    print("Advertencia. El precio del producto no puede ser negativo o 0")
                else:
                    break
            except ValueError:
                print("Error. Ingrese un valor númerico valido")
        while True:
            try:
                stock = int(input("Ingrese el stock del producto: "))
                if not stock:
                    print("Advertencia. Campo requerido, por favor ingrese el stock")
                elif stock <= 0:
                    print("Advertencia. El stock no puede ser negativo o 0")
                else:
                    break
            except ValueError:
                print("Error. Ingrese un valor númerico valido")
        return {'código': codigo, 'nombre': nombre, 'categoria': categoria, 'precio': precio, 'stock': stock}
    @staticmethod
    def validar_datosamodificar(existencia):
        print("Ingrese los nuevos datos del producto (deje en blanco si no desea cambiarlo): ")
        while True:
            try:
                precio = input(f"Ingrese el nuevo precio del producto {existencia.precio}: ")
                stock = input(f"Ingrese el nuevo stock del producto {existencia.stock}: ")
                nuevo_precio = float(precio) if precio else existencia.precio
                nuevo_stock = int(stock) if stock else existencia.stock
                if nuevo_precio <= 0 or nuevo_stock <= 0:
                    print("Advertencia. El precio o el stock no pueden ser valores negativos o 0")
                    return None
                return {'precio': nuevo_precio, 'stock': nuevo_stock}
            except ValueError:
                print("Error. El precio y el stock deben de ser números")
class GestionProductos:
    def __init__(self, buscador: iBuscador, alterar: iAlterarProducto):
        self.productos = {}
        self.buscador = buscador
        self.alterar = alterar
    def agregar(self, datosp):
        self.productos[datosp['codigo']] = Productos(**datosp)
    def buscar(self, codigo):
        return self.buscador.buscar(self.productos, codigo)
    def eliminar(self, codigo):
        return self.alterar.eliminar(self.productos, codigo)
    def actualizar(self, codigo, datos):
        producto = self.buscar(codigo)
        if producto:
            return self.alterar.editar(producto, datos)
        return False
class Visualizacion:
    def __int__(self, gestor: GestionProductos, validador: ValidarDatosProductos, ordenar: OrdenadorProductos):
        self.gestor = gestor
        self.validador = validador
        self.ordenar = ordenar
