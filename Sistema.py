from abc import ABC, abstractmethod
class Categorias:
    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre
    def mostrar_categoria(self):
        return f"Código: {self.ID} | Nombre: {self.nombre}"
class Productos:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
    def mostrar_producto(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Categoria: {self.categoria} | Precio: {self.precio} | Stock: {self.stock}"
class Clientes:
    def __init__(self, NIT_Cliente, nombre, direccion, telefono, correo):
        self.NITC = NIT_Cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
    def mostrar_cliente(self):
        return f"NIT: {self.NITC} | Nombre: {self.nombre} | Dirección: {self.direccion} | Correo: {self.correo}"
class Ventas:
    def __init__(self, ID_Venta, fecha, ID_empleado, NIT_Cliente, total, detalles_venta):
        self.ID_Venta = ID_Venta
        self.fecha = fecha
        self.ID_empleado = ID_empleado
        self.NIT_Cliente = NIT_Cliente
        self.total = total
        self.detalles_venta = detalles_venta
class iBuscador(ABC):
    @abstractmethod
    def buscar(self, registro, clave):
        pass
class iAlterarProducto(ABC):
    @abstractmethod
    def eliminar(self, registro, clave):
        pass
    @abstractmethod
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
        return self.quicks_preciomay(mayores) + iguales + self.quicks_preciomay(menores)
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
    def validar_datoscategoria(categorias_existentes):
        while True:
            codigo = input("Ingrese el código de la categoria: ").upper()
            if not codigo:
                print("Advertencia. Campo requerido, por favor ingrese el código de la categoria")
            elif codigo in categorias_existentes:
                print("Categoria ya existente. Intente de nuevo")
            else:
                break
        while True:
            nombre = input("Ingrese el nombre de la categoria: ").upper()
            if not nombre:
                print("Advertencia. Campo requerido, por favor ingrese el nombre de la categoria")
            else:
                break
        return {'ID': codigo, 'nombre': nombre}
    @staticmethod
    def validar_datosyagegar(productos_en_existencia, categorias_existentes):
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
            categoria_codigo = input("Ingrese el código de la categoria del producto: ")
            if categoria_codigo not in categorias_existentes:
                print("Error. Categoria inexistente, por favor agreguela")
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
                elif stock < 0:
                    print("Advertencia. El stock no puede ser negativo o 0")
                else:
                    break
            except ValueError:
                print("Error. Ingrese un valor númerico valido")
        return {'codigo': codigo, 'nombre': nombre, 'categoria': categoria_codigo, 'precio': precio, 'stock': stock}
    @staticmethod
    def validar_datosamodificar(existencia):
        print("Ingrese los nuevos datos del producto (deje en blanco si no desea cambiarlo): ")
        while True:
            try:
                precio = input(f"Ingrese el nuevo precio del producto {existencia.precio}: ")
                stock = input(f"Ingrese el nuevo stock del producto {existencia.stock}: ")
                nuevo_precio = float(precio) if precio else existencia.precio
                nuevo_stock = int(stock) if stock else existencia.stock
                if nuevo_precio <= 0 or nuevo_stock < 0:
                    print("Advertencia. El precio o el stock no pueden ser valores negativos o 0")
                    return None
                return {'precio': nuevo_precio, 'stock': nuevo_stock}
            except ValueError:
                print("Error. El precio y el stock deben de ser números")
class GestionProductos:
    def __init__(self, buscadar: iBuscador, alterar: iAlterarProducto):
        self.productos = {}
        self.categorias = {}
        self.buscador = buscadar
        self.alterar = alterar
    def agregar_categoria(self, datos):
        self.categorias[datos['ID']] = Categorias(**datos)
    def agregar_producto(self, datosp):
        self.productos[datosp['codigo']] = Productos(**datosp)
        return True
    def buscar_producto(self, codigo):
        return self.buscador.buscar(self.productos, codigo)
    def eliminar_producto(self, codigo):
        return self.alterar.eliminar(self.productos, codigo)
    def actualizar_producto(self, codigo, datos):
        producto = self.buscar_producto(codigo)
        if producto:
            return self.alterar.editar(producto, datos)
        return False
class GestionCliente:
    def __init__(self, buscador):
        self.clientes = {}
        self.buscador = buscador
    def agregar_clientes(self, datos):
        self.clientes[datos['NITC']] = Clientes(**datos)
        print("Cliente agregado correctamente")

class Visualizacion:
    def __init__(self, gestor: GestionProductos, validar: ValidarDatosProductos, ordenar: OrdenadorProductos):
        self.gestor = gestor
        self.validador = validar
        self.ordenar = ordenar
    def menu(self):
        while True:
            print("======MENÚ PRINCIPAL======")
            print("1. Gestionar categorias")
            print("2. Gestionar productos")
            print("3. Salir")
            try:
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    self.menu_categorias()
                elif opcion == "2":
                    self.menu_productos()
                elif opcion == "3":
                    print("Saliendo...")
                    break
                else:
                    print("Opción no valida, intente de nuevo")
            except ValueError:
                print("Error. Seleccione un número dentro del rango 1-5")
    def menu_categorias(self):
        while True:
            print("------Menú categorias------")
            print("1. Agregar categorias")
            print("2. Listar categorias")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_categoria()
            elif opcion == "2":
                self.listadoc()
            elif opcion == "3":
                print("Regresando...")
                return
            else:
                print("Opcion no valida, intente de nuevo")
    def agregar_categoria(self):
        datos = self.validador.validar_datoscategoria(self.gestor.categorias)
        self.gestor.agregar_categoria(datos)
        print("Categoria agregada correctamente")
    def listadoc(self):
        if not self.gestor.categorias:
            print("No se han encontrado categorias. Por favor primero ingrese categorias")
            return
        for categoria in self.gestor.categorias.values():
            print(categoria.mostrar_categoria())
    def menu_productos(self):
        while True:
            print("------Menú productos------")
            print("1. Agregar productos")
            print("2. Listar productos")
            print("3. Buscar producto")
            print("4. Editar producto")
            print("5. Salir")
            try:
                opcion = int(input("Seleccione una opción (1-5): "))
                if opcion == 1:
                    self.agregar_producto()
                elif opcion == 2:
                    self.listado()
                elif opcion == 3:
                    self.buscar_producto()
                elif opcion == 4:
                    self.editar_producto()
                elif opcion == 5:
                    print("Regresando...")
                    return
                else:
                    print("Opcion no valida, intente de nuevo")
            except ValueError:
                print("Error. Por favor ingrese un número del 1 al 5")
    def agregar_producto(self):
        if not self.gestor.categorias:
            print("No se puede agregar un producto si no existen categorias")
            return
        while True:
            try:
                cant = int(input("\tIngrese la cantidad de productos que desea agregar: "))
                if not cant:
                    print("Advertencia. Para continuar por favor ingrese un valor")
                else:
                    for i in range(cant):
                        print(f"Producto #{i + 1}:")
                        datos = self.validador.validar_datosyagegar(self.gestor.productos, self.gestor.categorias)
                        if datos:
                            self.gestor.agregar_producto(datos)
                            print("Producto(s) agregado(s) correctamente")
                    return
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
        encontrado = self.gestor.buscar_producto(codigo)
        if encontrado:
            print("\t Producto encontrado")
            print(encontrado.mostrar_producto())
        else:
            print("Producto no encontrado")
    def editar_producto(self):
        codigo = input("Ingrese el código del producto a editar: ")
        encontrado = self.gestor.buscar_producto(codigo)
        if not encontrado:
            print("\tProducto no encontrado")
            return
        print("Producto actual: ")
        print(encontrado.mostrar_producto())
        datos_nuevos = self.validador.validar_datosamodificar(encontrado)
        if datos_nuevos:
            if self.gestor.actualizar_producto(codigo, datos_nuevos):
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
