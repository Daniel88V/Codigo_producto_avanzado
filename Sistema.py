from abc import ABC, abstractmethod
import datetime
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
class Proveedores:
    def __init__(self, NIT_Proveedor, nombre, direccion, telefono, correo):
        self.NITP = NIT_Proveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
    def mostrar_proveedor(self):
        return f"NIT: {self.NITP} | Nombre: {self.nombre} | Dirección: {self.direccion}"
class Empleados:
    def __init__(self, ID_Empleado, nombre, direccion, telefono, correo, puesto):
        self.ID_Empleado = ID_Empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto
    def mostrar_empleado(self):
        return f"ID: {self.ID_Empleado} | Nombre: {self.nombre} | Puesto: {self.puesto}"
class Compras:
    def __init__(self, ID_Compra, FechaIngreso, ID_Empleado, NIT_Proveedor, Total):
        self.ID_Compra = ID_Compra
        self.FechaIngreso = FechaIngreso
        self.ID_Empleado = ID_Empleado
        self.NIT_Proveedor = NIT_Proveedor
        self.Total = Total
class Ventas:
    def __init__(self, ID_Venta, Fecha, ID_Empleado, NIT_Cliente, Total):
        self.ID_Venta = ID_Venta
        self.Fecha = Fecha
        self.ID_Empleado = ID_Empleado
        self.NIT_Cliente = NIT_Cliente
        self.Total = Total
class DetalleVentas:
    def __init__(self, ID_DetalleV, ID_Venta, ID_Producto, cantidad, subtotal):
        self.ID_DetalleV = ID_DetalleV
        self.ID_Venta = ID_Venta
        self.ID_Producto = ID_Producto
        self.cantidad = cantidad
        self.subtotal = subtotal
class DetalleCompras:
    def __init__(self, ID_DetalleC, ID_Compra, ID_Producto, cantidad, precio_compra, fecha_caducidad):
        self.ID_DetalleC = ID_DetalleC
        self.ID_Compra = ID_Compra
        self.ID_Producto = ID_Producto
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.fecha_caducidad = fecha_caducidad
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
            if hasattr(cosa, 'codigo') and cosa.codigo.upper() == clave.upper():
                return cosa
            if hasattr(cosa, 'NITC') and cosa.NITC.upper() == clave.upper():
                return cosa
            if hasattr(cosa, 'ID') and cosa.ID.upper() == clave.upper():
                return cosa
            if hasattr(cosa, 'NITP') and cosa.NITP.upper() == clave.upper():
                return cosa
            if hasattr(cosa, 'ID_Empleado') and cosa.ID_Empleado.upper() == clave.upper():
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
                nuevo_precio = float(precio) if precio else existencia.precio
                if nuevo_precio <= 0:
                    print("Advertencia. El precio no puede ser un valor negativo o 0")
                    return None
                return {'precio': nuevo_precio}
            except ValueError:
                print("Error. El precio debe de ser números")
class ValidarDatosClientes:
    @staticmethod
    def validar_datosc(clientes_existentes):
        while True:
            nit = input("Ingrese el NIT del cliente: ").upper()
            if not nit:
                return None
            if nit in clientes_existentes:
                print("Error. Este cliente ya existe")
            else:
                break
        while True:
            nombre = input("Ingrese el nombre del cliente: ")
            if not nombre:
                print("Advertencia. Este campo es requerido, por favor ingrese el nombre del cliente")
            else:
                break
        while True:
            direccion = input("Ingrese la dirección del cliente: ")
            if not direccion:
                print("Advertencia. Campo requerido, por favor ingrese la dirección del cliente")
            else:
                break
        while True:
            telefono = input("Ingrese el telefono del cliente: ")
            if not telefono:
                print("Advertencia. Campo requerido, por favor ingrese el telefono del cliente")
            else:
                break
        while True:
            correo = input("Ingrese la correo del cliente: ")
            if not correo:
                print("Advertencia. Campo requerido, por favor ingrese el correo del cliente")
            else:
                break
        return {'NIT_Cliente': nit, 'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo}
class ValidarDatosProveedores:
    @staticmethod
    def validar_datosproveedores(proveedores_existentes):
        while True:
            nit = input("Ingrese el NIT del proveedor: ").upper()
            if not nit:
                print("Advertencia. Campo requerido, por favor ingrese el NIT del proveedor")
            elif nit in proveedores_existentes:
                print("Error. Este proveedor ya existe")
            else:
                break
        while True:
            nombre = input("Ingrese el nombre del proveedor: ")
            if not nombre:
                print("Advertencia. Campo requerido, por favor ingrese el nombre del proveedor")
            else:
                break
        while True:
            direccion = input("Ingrese la dirección del proveedor: ")
            if not direccion:
                print("Advertencia. Campo requerido, por favor ingrese la dirección del proveedor")
            else:
                break
        while True:
            telefono = input("Ingrese el telefono del proveedor: ")
            if not telefono:
                print("Advertencia. Campo requerido, por favor ingrese el telefono del proveedor")
            else:
                break
        while True:
            correo = input("Ingrese el correo del proveedor: ")
            if not correo:
                print("Advertencia. Campo requerido, por favor ingrese el correo del proveedor")
            else:
                break
        return {'NIT_Proveedor': nit, 'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo}
class ValidarDatosEmpleados:
    @staticmethod
    def validar_datesempleados(empleados_existentes):
        while True:
            id_empleado = input("Ingrese el ID del empleado: ").upper()
            if not id_empleado:
                print("Advertencia. Campo requerido, por favor agregue el ID del empleado")
            elif id_empleado in empleados_existentes:
                print("Error. Este empleado ya existe")
            else:
                break
        while True:
            nombre = input("Ingrese el nombre del empleado: ")
            if not nombre:
                print("Advertencia. Campo requerido, por favor ingrese el nombre del empleado")
            else:
                break
        while True:
            direccion = input("Ingrese la dirección del empleado: ")
            if not direccion:
                print("Advertencia. Campo requerido, por favor ingrese la dirección del empleado")
            else:
                break
        while True:
            telefono = input("Ingrese el telefono del empleado: ")
            if not telefono:
                print("Advertencia. Campo requerido, por favor ingrese el número del empleado")
            else:
                break
        while True:
            correo = input("Ingrese el correo del empleado: ")
            if not correo:
                print("Advertencia. Campo requerido, por favor ingrese el correo del empleado")
            else:
                break
        while True:
            puesto = input("Ingrese la puesto del empleado: ")
            if not puesto:
                print("Advertencia. Campo requerido, por favor ingrese el puesto del empleado")
            else:
                break
        return {'ID_Empleado': id_empleado, 'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'puesto': puesto}
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
    def __init__(self, buscadora: iBuscador):
        self.clientes = {}
        self.buscador = buscadora
    def agregar_clientes(self, datos):
        self.clientes[datos['NIT_Cliente']] = Clientes(**datos)
    def buscar_cliente(self, codigo):
        return self.buscador.buscar(self.clientes, codigo)
class GestionProveedores:
    def __init__(self, buscadora: iBuscador):
        self.proveedores = {}
        self.buscador = buscadora
    def agregar_proveedor(self, datos):
        self.proveedores[datos['NIT_Proveedor']] = Proveedores(**datos)
        return True
    def buscar_proveedor(self, nit_proveedor):
        return self.buscador.buscar(self.proveedores, nit_proveedor)
class GestionEmpleados:
    def __init__(self, buscadora: iBuscador):
        self.empleados = {}
        self.buscador = buscadora
    def agregar_empleado(self, datos):
        self.empleados[datos['ID_Empleado']] = Empleados(**datos)
        return True
    def buscar_empleado(self, id_empleado):
        return self.buscador.buscar(self.empleados, id_empleado)
class GestionVentas:
    def __init__(self, gestor_productos, gestor_clientes):
        self.ventas = {}
        self.detallesvemtas = {}
        self.gestor_productos = gestor_productos
        self.gestor_clientes = gestor_clientes
        self.contador_v = 0
        self.contador_det = 0
    def agregar_ventas(self, nit_cliente, id_empleado, detalles_compra):
        self.contador_v += 1
        id_venta = f"Venta_{self.contador_v:04d}"
        fecha_venta = datetime.datetime.today()
        total_venta = 0
        for i in detalles_compra:
            codigo = i['codigo']
            cantidad = i['cantidad']
            producto = self.gestor_productos.buscar_producto(codigo)
            if not producto:
                print(f"Error. No se encontró el producto {codigo}")
                return False
            if cantidad > producto.stock:
                print(f"Error. No hay suficientes existencias del producto {producto.nombre}")
                print(f"Cantidad disponible: {producto.stock}")
                return False
            subtotal = producto.precio * cantidad
            total_venta += subtotal
            producto.stock -= cantidad
            self.contador_det += 1
            id_detalle = f"DetalleV{self.contador_v:04d}"
            detalle = DetalleVentas(id_detalle, id_venta, codigo, cantidad, subtotal)
            self.detallesvemtas[id_detalle] = detalle
        nueva_venta = Ventas(id_venta, fecha_venta, id_empleado, nit_cliente, total_venta)
        self.ventas[id_venta] = nueva_venta
        print(f"\n Venta {id_venta} agregada.")
        print(f"Cliente: {nit_cliente} | Empleado: {id_empleado}")
        print(f"Total: Q.{total_venta:.2f}")
        for detalle in self.detallesvemtas.values():
            if detalle.ID_Venta == id_venta:
                producto_vendido = self.gestor_productos.buscar_producto(detalle.ID_Producto)
                print(f"\t Producto: {producto_vendido.nombre} | Cantidad: {detalle.cantidad} | Subtotal: {detalle.subtotal:.2f}")
        return True
    def registro_ventas(self):
        return self.ventas
class GestionCompras:
    def __init__(self, gestor_productos, gestor_proveedores):
        self.compras = {}
        self.detallecompras = {}
        self.gestor_productos = gestor_productos
        self.gestor_proveedores = gestor_proveedores
        self.contador_compra = 0
        self.contador_det = 0
    def agregar_compra(self, nit_proveedor, id_empleado, detalles_compra):
        self.contador_compra += 1
        id_compra = f"Compra{self.contador_compra:04d}"
        fecha_compra = datetime.datetime.today()
        total_compra = 0
        for i in detalles_compra:
            codigo = i['codigo']
            cantidad = i['cantidad']
            producto = self.gestor_productos.buscar_producto(codigo)
            if not producto:
                print(f"Error. No se encontró el producto: {codigo}")
                return False
            precio_compra = i.get('precio_compra', producto.precio)
            fecha_caducidad = i.get("fecha_caducidad","N/A")
            total_compra += precio_compra * cantidad
            producto.stock += cantidad
            self.contador_det += 1
            id_detalle = f"DetalleC{self.contador_compra:04d}"
            detalle = DetalleCompras(id_detalle, id_compra, codigo, cantidad, precio_compra, fecha_caducidad)
            self.detallecompras[id_compra] = detalle
        nueva_compra = Compras(id_compra, fecha_compra, id_empleado, nit_proveedor, total_compra)
        self.compras[id_compra] = nueva_compra
        print(f"\n Compra {id_compra} agregada.")
        print(f"Proveedor: {nit_proveedor} | Empleado: {id_empleado} | Total: {total_compra:.2f}")
        for detalle in self.detallecompras.values():
            if detalle.ID_Compra == id_compra:
                producto_compra = self.gestor_productos.buscar_producto(detalle.ID_Producto)
                print(f"\t Producto: {producto_compra.nombre} | Cantidad: {detalle.cantidad} | Total: Q.{detalle.total_compra:.2f}")
        return True
class Visualizacion:
    def __init__(self,
                 gestor: GestionProductos,
                 validar: ValidarDatosProductos,
                 ordenar: OrdenadorProductos,
                 gestor_clientes: GestionCliente,
                 validar_clientes: ValidarDatosClientes,
                 gestor_proveedores: GestionProveedores,
                 validador_proveedores: ValidarDatosProveedores,
                 gestor_empleados: GestionEmpleados,
                 validador_empleados: ValidarDatosEmpleados,
                 gestor_ventas: GestionVentas,
                 gestor_compras: GestionCompras,):
        self.gestor = gestor
        self.validador = validar
        self.ordenar = ordenar
        self.gestor_clientes = gestor_clientes
        self.validar_clientes = validar_clientes
        self.gestor_proveedores = gestor_proveedores
        self.validar_proveedores = validador_proveedores
        self.gestor_empleados = gestor_empleados
        self.validador_empleados = validador_empleados
        self.gestor_ventas = gestor_ventas
        self.gestor_compras = gestor_compras
    def menu(self):
        while True:
            print("======MENÚ PRINCIPAL======")
            print("1. Gestionar categorias")
            print("2. Gestionar productos")
            print("3. Gestionar clientes")
            print("4. Gestionar proveedores")
            print("5. Gestionar compras y ventas")
            print("6. Gestionar empleados")
            print("7. Menu registros")
            print("7. Salir")
            try:
                opcion = input("Ingrese una opción: ")
                if opcion == "1":
                    self.menu_categorias()
                elif opcion == "2":
                    self.menu_productos()
                elif opcion == "3":
                    self.menu_clientes()
                elif opcion == "4":
                    self.menu_proveedores()
                elif opcion == "5":
                    self.menu_venta_y_comprar()
                elif opcion == "6":
                    self.menu_empleados()
                elif opcion == "7":
                    self.menu_registros()
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
    def menu_clientes(self):
        while True:
            print("------Menú clientes------")
            print("1. Agregar cliente")
            print("2. Listar clientes")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.agregar_cliente()
            elif opcion == "2":
                self.listar_cliente()
            elif opcion == "3":
                print("Regresando...")
                return
            else:
                print("Opción no valida")
    def agregar_cliente(self):
        datos = self.validar_clientes.validar_datosc(self.gestor_clientes.clientes)
        self.gestor_clientes.agregar_clientes(datos)
        print("Cliente agregado correctamente")
    def listar_cliente(self):
        if not self.gestor_clientes.clientes:
            print("No se han agregado clientes")
            return
        for cliente in self.gestor_clientes.clientes.values():
            print(cliente.mostrar_cliente())
    def menu_proveedores(self):
        print(f"\n------Menú Proveedores------")
        print("1. Agregar proveedor")
        print("2. Listar proveedors")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            self.agregar_proveedor()
        elif opcion == "2":
            self.listar_proveedor()
        elif opcion == "3":
            print("Regresando...")
            return
        else:
            print("Opción no valida")
    def agregar_proveedor(self):
        datos = self.validar_proveedores.validar_datosproveedores(self.gestor_proveedores.proveedores)
        if datos:
            self.gestor_proveedores.agregar_proveedor(datos)
            print("Proveedor agregado correctamente")
    def listar_proveedor(self):
        if not self.gestor_proveedores.proveedores:
            print("No se han encontrado proveedores. Primero agregue proveedores")
            return
        for proveedor in self.gestor_proveedores.proveedores.values():
            print(proveedor.mostrar_proveedor())
    def menu_empleados(self):
        while True:
            print(f"\n------Menú Empleados------")
            print("1. Agregar empleado")
            print("2. Listar empleados")
            print("3. Regresar")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.agregar_empleado()
            elif opcion == "2":
                self.listar_empleado()
            elif opcion == "3":
                print("Regresando...")
                return
            else:
                print("Opción no valida")
    def agregar_empleado(self):
        datos = self.validador_empleados.validar_datesempleados(self.gestor_empleados.empleados)
        if datos:
            self.gestor_empleados.agregar_empleado(datos)
            print("Empleado agregado correctamente.")
    def listar_empleado(self):
        if not self.gestor_empleados.empleados:
            print("No se han encontrado empleados. Por favor, agregue uno primero.")
            return
        for empleado in self.gestor_empleados.empleados.values():
            print(empleado.mostrar_empleado())
    def menu_venta_y_comprar(self):
        print("\n Menú de ventas y compras")
        print("1. Agregar venta")
        print("2. Agregar compra")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            self.agregar_venta()
        elif opcion == "2":
            self.agregar_compra()
        elif opcion == "3":
            print("Regresando...")
            return
        else:
            print("Opción no valida")
    def agregar_venta(self):
        nit_cliente = input("Ingrese el NIT del cliente (presione enter para cancelar): ").upper()
        if not nit_cliente:
            print("Operación cancelada")
            return
        cliente = self.gestor_clientes.buscar_cliente(nit_cliente)
        if not cliente:
            print("Cliente no encontrado")
            nuevo_cliente = input("¿Desea agregar al cliente? (Si/No): ").upper()
            if nuevo_cliente == "SI":
                datos = self.validar_clientes.validar_datosc(self.gestor_clientes.clientes)
                if datos:
                    self.gestor_clientes.agregar_clientes(datos)
                    print(f"Cliente {datos['nombre']} agregado correctamente")
                else:
                    print("Operación cancelada")
                    return
            else:
                print("El cliente no será agregado")
                nit_cliente = "CF"
        id_empleado = input("Ingrese el Id del empleado realizando la venta: ").upper()
        if not id_empleado:
            print("Venta cancelada. Se require el ID del empleado")
            return
        detalles_venta = []
        while True:
            codigo = input("Ingrese el código del producto (enter para cancelar): ").upper()
            if not codigo:
                break
            while True:
                producto = self.gestor.buscar_producto(codigo)
                if not producto:
                    print("Producto no encontrado. Intente de nuevo")
                else:
                    break
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    if cantidad <= 0:
                        print("La cantidad a vender no puede ser menor a 0")
                    else:
                        break
                except ValueError:
                    print("Error. La cantidad debe de ser un valor númerico valido")
            detalles_venta.append({'codigo': codigo, 'cantidad': cantidad})
        if detalles_venta:
            self.gestor_ventas.agregar_ventas(nit_cliente, id_empleado,detalles_venta)
        else:
            print("Venta cancelada")
    def agregar_compra(self):
        nit_proveedor = input("Ingrese el nit del proveedor: ").upper()
        if not nit_proveedor:
            print("Campo requerido. Cancelando compra")
            return
        proveedor = self.gestor_proveedores.buscar_proveedor(nit_proveedor)
        if not proveedor:
            print("Proveedor no encontrado")
            return
        id_empleado = input("Ingrese el Id del empleado que realiza la compra: ")
        if not id_empleado:
            print("Campo requerido. Cancelando compra")
            return
        detalles_compra = []
        while True:
            codigo = input("Ingrese el código del producto a comprar (presione enter para cancelar): ").upper()
            if codigo == "":
                break
            while True:
                producto = self.gestor.buscar_producto(codigo)
                if not producto:
                    print("Producto no encontrado. Intente de nuevo")
                else:
                    break
            try:
                while True:
                    cantidad = int(input(f"Ingrese la cantidad de {producto.nombre} que desea comprar: "))
                    if cantidad <= 0:
                        print("Advertencia. La cantidad a comprar no puede ser negativa o 0")
                    else:
                        break
                precio_compra = float(input("Ingrese el precio de compra: "))
                fecha_caducidad = input("Ingrese la fecha de caducidad (DD/MM/AAAA): ")
                detalles_compra.append({
                    'codigo': codigo,
                    'cantidad': cantidad,
                    'precio_compra': precio_compra,
                    'fecha_caducidad': fecha_caducidad,
                })
            except ValueError:
                print("Cantidad o precios invalidos")
                continue
        if detalles_compra:
            self.gestor_compras.agregar_compra(nit_proveedor, id_empleado, detalles_compra)
        else:
            print("Campos no requeridos. Cancelando compra")
    def menu_registros(self):
        print("1. Registros ventas")
        print("2. Salir")
        opcion = input("Seleccione una opcion")
        if opcion == "1":
            print(self.mostrar_registro_v())
        elif opcion == "2":
            return
    def mostrar_registro_v(self):
        self.gestor_ventas.registro_ventas()
if __name__ == "__main__":
    buscador = BusquedaSecuencial()
    modificador = AlterarProducto()
    ordenamiento = OrdenadorProductos()
    validacion_productos = ValidarDatosProductos()
    validacion_clientes = ValidarDatosClientes()
    validacion_proveedores = ValidarDatosProveedores()
    validaccion_empleados = ValidarDatosEmpleados()
    gestion_productos = GestionProductos(buscador, modificador)
    gestion_clientes = GestionCliente(buscador)
    gestion_proveedores = GestionProveedores(buscador)
    gestion_empleados = GestionEmpleados(buscador)
    gestion_ventas = GestionVentas(gestion_productos, gestion_clientes)
    gestion_compras = GestionCompras(gestion_productos, gestion_proveedores)
    menu = Visualizacion(gestion_productos, validacion_productos, ordenamiento, gestion_clientes, validacion_clientes, gestion_proveedores, validacion_proveedores, gestion_empleados, validaccion_empleados, gestion_ventas, gestion_compras)
    menu.menu()
