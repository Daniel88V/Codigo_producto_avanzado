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
    def __init__(self, buscadar: iBuscador, alterar: iAlterarProducto):
        self.productos = {}
        self.buscador = buscadar
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
    def __init__(self, gestor: GestionProductos, validar: ValidarDatosProductos, ordenar: OrdenadorProductos):
        self.gestor = gestor
        self.validador = validar
        self.ordenar = ordenar
    def menu(self):
        while True:
            print("======MENÚ PRINCIPAL======")
            print("1. Agregar productos")
            print("2. Listado de productos")
            print("3. Buscar productos")
            print("4. Editar producto")
            print("5. Salir")
            try:
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    self.agregar_producto()
                elif opcion == "2":
                    self.listado()
                elif opcion == "3":
                    self.buscar_producto()
                elif opcion == "4":
                    self.editar_producto()
                elif opcion == "5":
                    print("Saliendo del programa...")
                    exit()
                else:
                    print("Opción no valida, intente de nuevo")
            except ValueError:
                print("Error. Seleccione un número dentro del rango 1-5")
    def agregar_producto(self):
        while True:
            try:
                cant = int(input("\tIngrese la cantidad de productos que desea agregar: "))
                if not cant:
                    print("Advertemcia. Para continuar por favor ingrese un valor")
                else:
                    for i in range(cant):
                        print(f"Producto #{i + 1}:")
                        datos = self.validador.validar_datosyagegar(self.gestor.productos)
                        if datos:
                            self.gestor.agregar(datos)
                            print("Producto(s) agregado(s) correctamente")
                            break
            except ValueError:
                print("Error. Ingrese un valor númerico valido")
    def listado(self):
        if not self.gestor.productos:
            print("No se han econtrado productos")
            return
        print("\n Menú listado de productos")
        print("1. Ordenado por nombre")
        print("2. Ordenado por precio (menor a mayor)")
        print("3. Ordenado por precio (mayor a menor)")
        print("4. Ordenado por stock")
        print("5. Regresar al menu principal")
        try:
            eleccion = int(input("Seleccione una opción: "))
            lista_productos = list(self.gestor.productos.values())
            if eleccion == 1:
                print("\t Productos ordenados por nombre")
                lista_productos = self.ordenar.quicks_nombre(lista_productos)
            elif eleccion == 2:
                print("\t Productos ordenados por precio (menor a mayor)")
                lista_productos = self.ordenar.quicks_preciomen(lista_productos)
            elif eleccion == 3:
                print("\t Productos ordenados por precio (mayor a menor)")
                lista_productos = self.ordenar.quicks_preciomay(lista_productos)
            elif eleccion == 4:
                print("\t Productos ordenados por stock")
                lista_productos = self.ordenar.quicks_stock(lista_productos)
            elif eleccion == 5:
                return
            else:
                print("Opción no valida")
            for i, producto in enumerate(lista_productos, start = 1):
                print(f"{i}. {producto.mostrar_producto()}")
        except ValueError:
            print("Error. Debes ingresar un número del 1 - 5")
    def buscar_producto(self):
        codigo = input("Ingrese el codigo del producto qie desea buscar: ")
        encontrado = self.gestor.buscar(codigo)
        if encontrado:
            print("\t Producto encontrado")
            print(encontrado.mostrar_producto())
        else:
            print("Producto no encontrado")
    def editar_producto(self):
        codigo = input("Ingrese el código del producto a editar: ")
        encontrado = self.gestor.buscar(codigo)
        if not encontrado:
            print("\tProducto no encontrado")
            return
        print("Producto actual: ")
        print(encontrado.mostrar_producto())
        datos_nuevos = self.validador.validar_datosamodificar(encontrado)
        if datos_nuevos:
            if self.gestor.actualizar(codigo, datos_nuevos):
                print("\t Producto actualizado correctamente")
            else:
                print("\t Error al editar el producto")
if __name__ == "__main__":
    buscador = BusquedaSecuencial()
    modificador = AlterarProducto()
    validador = ValidarDatosProductos()
    ordenador = OrdenadorProductos()
    gestionador = GestionProductos(buscador, modificador)
    menu = Visualizacion(gestionador, validador, ordenador)
    menu.menu()