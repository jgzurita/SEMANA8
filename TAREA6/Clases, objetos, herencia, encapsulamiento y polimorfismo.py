### UEA ###
### JUAN GABRIEL ZURITA MANOBANDA ###

#### Realizaremos un registro de libros ###

# Clase productos
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo encapsulados
        self.__precio = precio 

    # Métodos de getters y setters
    def obtener_precio(self):
        return self.__precio

    def establecer_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser positivo.")
    
    def mostrar_info(self):
        return f"{self._nombre} - Precio: ${self.obtener_precio()}"

# Clase derivada Libro  recibe la herencia productos
class Libro(Producto):
    def __init__(self, nombre, precio, autor, genero):
        super().__init__(nombre, precio)
        self.autor = autor
        self.genero = genero

    # Sobrescritura de método para mostrar más detalless
    def mostrar_info(self):
        return f"Libro: {self._nombre}, Autor: {self.autor}, Género: {self.genero}, Precio: ${self.obtener_precio()}"

    
    def aplicar_descuento(self, *porcentajes):  # Polimorfismo 
        for porcentaje in porcentajes:
            descuento = self.obtener_precio() * (porcentaje / 100)
            nuevo_precio = self.obtener_precio() - descuento
            print(f"Descuento del {porcentaje}%: Nuevo precio: ${nuevo_precio:.2f}")


def mostrar_tabla(libros):  # Función para crear y mostrar libros en una tabla
    print(f"{'Nombre':<20} {'Autor':<20} {'Género':<15} {'Precio ($)':<10}")
    print("-" * 65)
    for libro in libros:
        info = libro.mostrar_info().split(", ")
        nombre, autor, genero, precio = [x.split(": ")[1] for x in info]
        print(f"{nombre:<20} {autor:<20} {genero:<15} {precio:<10}")


libros = []  # Crear lista de libros
while True:
    nombre = input("Ingrese el nombre del libro (o 'salir' para terminar): ")
    if nombre.lower() == "salir":   ### si el nombre es salir se imprimira la tabla despues de cerrar el proceso 
        break
    precio = float(input("Ingrese el precio del libro: "))
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")

    libro = Libro(nombre, precio, autor, genero)
    libros.append(libro)


mostrar_tabla(libros)  # Mostrar los libros en una tabla
