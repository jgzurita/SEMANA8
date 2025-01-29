### UEA ###
### JUAN GABRIEL ZURITA MANOBANDA ###
###  PROGRAMA PARA ALMACENAR LAS GANANCIAS DE LA SEMANA Y OBTENER UN PROMEDIO 
def obtener_promedio(ganancias):
 
    ### CALCULA EL PROMEDIO DE UNA LISTA DE NÚMEROS.
    
    
   
    total = sum(ganancias)    ###SUMAMOS LAS GANANCIAS 
    return total / len(ganancias)  ### PROMEDIAMOS LAS GANANCIAS 

def main():
   ## DEFINIMOS LOS DIAS DE LA SEMANA  
    dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
    
    # LISTA PARA ALMACENAR LAS GANANCIAS 
    ganancias = []
    
    
    registro_ganancias = {}   ### REGISTRAMOS LAS GANANCIAS EN UN DICCIONARIO 
    
    print("ingresa las  ganancias semanales:")
    
    for dia in dias_semana:
        while True:
            try:
                # SOLICITAMOS LA GANACIAS DIARIA 
                ganancia = float(input(f"Introduce la ganancia del {dia}: "))
                ganancias.append(ganancia)  # ## SE AGRAGA A LA LISTA
                registro_ganancias[dia] = ganancia  ### SE AGREGA AL DICCIONARIO 
                break
            except ValueError:     ##EN CASO DE QUE NO SEA UNA ENTRADA O VALOR CORECTO SDAMOS EL AVISO 
                print("Por favor, introduce un número válido.")
    
    
    promedio = obtener_promedio(ganancias)  ### CALCULAMOS PROMEDIO
    
    # MOSTRAMOS EL RESUMEN DE LAS GANANCIAS LLAMANDO LOS VALORES DEL REGISTRO DEL DICCIONARIO 
    print("\nResumen de ganancias:")
    for dia, ganancia in registro_ganancias.items():
        print(f"{dia}: ${ganancia:.2f}")
    
    print(f"\nEl promedio de ganancias de esta semana es: ${promedio:.2f}")   ### SACAMOS EL PROMEDIO 
    
### EJECUTAMOS EL PROGRAMA 
if __name__ == "__main__":
    main()

