### UEA ###
### JUAN GABRIEL ZURITA MANOBANDA ###

### PROGRAMACIÓN TRADICIONAL ###


def ingresar_temperaturas():      ## INGRESA LAS TEMPERATURAS EN LA FUNCIÓN
    temperaturas = []
    print("Ingresa las temperaturas diarias de la semana:")
    for i in range(7): ## SE ESTABLECE EL RANGO PARA LOS 7 DIAS DE LA SEMANA 
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):    ### FUNCIÓN PARA PROMEDIAR LAS TEMPERATURAS 
    
    return sum(temperaturas) / len(temperaturas)

#  EJECUTA EL PROMEDIO E IMPRIME EL RESULTADO 
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")