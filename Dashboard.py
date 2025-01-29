### UEA ###
### JUAN GABRIEL ZURITA MANOBANDA ####
#### TEMA: ORGANIZADOR ORIENTADO A OBJETOS####

                                    #### NOTA #####
#BASADO EN EL CODIGO BRINDADO EN EL ENLACE DE LA TAREA SE ENCONTRO POBLEMAS POR LA VERSIÓN DE PYTHON SEGUN STACKOVERLOW, 
#SE ANALIZO EL OBJETIVO DE LA ACTIVIDAD Y SE ELABORO ESTE ORGANIZADOR MAS COMPACTO Y SE LE AÑADIO
#LA FUNCIÓN DE BORRAR CARPETAS.

import os
import subprocess
import shutil  # IMPORTE DE LIBRERIA PARA ELIMINAR ARCHIVOS Y CARPETAS

def listar_archivos_y_carpetas(path):      ### LISTAMOS LOS ARCHIVOS EN EL PATH 
    print("\nContenido de la carpeta actual:")
    for i, item in enumerate(os.listdir(path)):
        print(f"[{i}] {item}")
    print("\nSeleccione un número para interactuar con el archivo o carpeta, o use:")
    print("[x] Volver a la carpeta anterior")     ### AGREGAMOS LAS OPCIONES PARA INTERCATUAR QUE SE IMPRIMIRAN EN CONSOLA
    print("[q] Salir del programa")
    print("[d] Borrar archivo o carpeta")

def ejecutar_archivo(ruta):
    if ruta.endswith(".py"):    ## ESTABLECEMOS LA RUTA COMO LOCAL
        print(f"Ejecutando el archivo {ruta}...")
        subprocess.run(["python", ruta])
    else:
        print("Solo se pueden ejecutar archivos Python (.py)")

def borrar_item(ruta):
    if os.path.isfile(ruta):
        os.remove(ruta)
        print(f"Archivo {ruta} borrado correctamente.")
    elif os.path.isdir(ruta):
        try:
            os.rmdir(ruta)  # SI ES CARPETA VACIA
            print(f"Carpeta {ruta} borrada correctamente.")
        except OSError:
            shutil.rmtree(ruta)  #SI NO ES CARPETA VACIA
            print(f"Carpeta {ruta} y su contenido han sido borrados correctamente.")
    else:
        print("El archivo o carpeta no se puede borrar.") ### EN CASO DE QUE LOS ARCHIVOS NO SE PUEDAS BORRAR

def dashboard_consola():
    current_path = os.getcwd()
    while True:
        listar_archivos_y_carpetas(current_path)
        opcion = input("\nIngrese su opción: ").strip()

        if opcion.lower() == 'q':          
            print("Saliendo del programa")
            break
        elif opcion.lower() == 'x':
            current_path = os.path.dirname(current_path)
            print(f"\nRetrocediendo a: {current_path}")
        elif opcion.lower() == 'd':
            opcion = input("\nIngrese el número del archivo o carpeta que deseaS borrar: ").strip()
            if opcion.isdigit():
                opcion = int(opcion)
                items = os.listdir(current_path)

                if 0 <= opcion < len(items):
                    seleccionado = os.path.join(current_path, items[opcion])
                    borrar_item(seleccionado)
                else:
                    print("Número fuera del rango, prueba otro")
            else:
                print("Opción no válida.")
        elif opcion.isdigit():
            opcion = int(opcion)
            items = os.listdir(current_path)

            if 0 <= opcion < len(items):
                seleccionado = os.path.join(current_path, items[opcion])

                if os.path.isdir(seleccionado):   ## se ingresa a la carpeta seleccionada.
                    current_path = seleccionado
                    print(f"\nIngresando a la carpeta: {current_path}")
                elif os.path.isfile(seleccionado):
                    ejecutar_archivo(seleccionado)
                else:
                    print("La opción seleccionada no es válida.")
            else:
                print("Número fuera de rango.")
        else:
            print("Opción no válida. Inténtelo nuevamente.")

if __name__ == "__main__":
    dashboard_consola()