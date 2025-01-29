###  UEA ###
###  JUAN GABRIEL ZURITA MANOBANDA  ###


#### AGREGAMOS LA CLASE PRODUCTO
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


    def __str__(self):  ##### devolvemos una representación de cadena de un objeto.

        return f"{self.nombre:15} {self.cantidad:10} {self.precio:10.2f}"


#### AGREGAMOS LA CLASE DE INVENTARIO PARA REVISAR LOS VALES QUE AGREGAMOS PREVIAMENTE
class Inventario:
    def __init__(self):
        """Inicializa un inventario vacío."""
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al inventario."""
        self.productos.append(producto)

    def imprimir_inventario(self):
        """Imprime todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        print(f"{'Nombre':15} {'Cantidad':10} {'Precio':10}")
        print("-" * 40)
        for producto in self.productos:
            print(producto)


#### REALIZAMOS UNA FUNCIÓN PARA AGREGAR PRODUCTOS MIRAR Y SALIR DEL INVENTARIO 
def main():
    inventario = Inventario()

    while True:
        print("\nMenú del Inventario")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del productoS: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.") #### LA CANTIDAD NO PODRA SER NEGATIVA PARA EVITAR ERRORES 
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero válido para la cantidad") ### TAMPOCO DECIMALES 
            
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio < 0:
                        print("El precio no puede ser negativo. Intente de nuevo")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para el precio")

            inventario.agregar_producto(Producto(nombre, cantidad, precio))
            print(f"Producto '{nombre}' agregado con éxito")
        
        elif opcion == "2":
            print("\nInventario actual:")
            inventario.imprimir_inventario()

        elif opcion == "3":
            print("Saliendo del programa ")
            break

        else:
            print("Opción no válida, intente de nuevo")


if __name__ == "__main__":
    main()
