#### UEA ###
### JUAN ZURITA#####

#### Constructor que inicializa el archivo para almacenar nombres y apellidos.
class RegistroNombres:
    def __init__(self, nombre_archivo):
        
        self.nombre_archivo = nombre_archivo
        try:
            self.archivo = open(nombre_archivo, 'w')
            print(f"Archivo '{self.nombre_archivo}' creado para almacenar nombres y apellidos.")
        except IOError as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None


    ##### Método o entrada  para agregar un nombre y apellido al archivo.

    def agregar_nombre(self, nombre, apellido):
    

        if self.archivo:
            self.archivo.write(f"{nombre} {apellido}\n")
            print(f"Nombre agregado: {nombre} {apellido}")
        else:
            print("No se puede escribir, el archivo no está abierto.")

    def __del__(self):   ###Destructor que cierra el archivo ####
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")


# EJEMPLO
if __name__ == "__main__":
    registro = RegistroNombres("nombres_y_apellidos.txt")
    registro.agregar_nombre("Juan", "Zurita")
    registro.agregar_nombre("Maria", "López")
    registro.agregar_nombre("Carlos", "Manobanda")
    # El destructor cerrará el archivo automáticamente cuando ya no sea necesario 
