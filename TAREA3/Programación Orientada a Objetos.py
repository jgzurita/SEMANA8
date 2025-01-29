### UEA ###
### JUAN GABRIEL ZURITA MANOBANDA ###

### PROGRAMACIÓN ORIENTADA A OBJETOS (P00) ###


class ClimaSemanal: #CLASE DONDE INGRESAREMOS LA PEEMPERATURA
    
    def __init__(self):        ### ESTABLECEMOS EL CONDUCTOR 
        self.temperaturas = []   # ENCAPSULAMOS LOS DATOS 

    def ingresar_temperaturas(self):  #INGRESAMOS LA TEMPERATURA        
        print("Ingresa las temperaturas diarias de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):     ##PROEDIAMOS 
       
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


clima = ClimaSemanal()   # EJECUTAMOS LLAMADO A LA CLASE
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()    # IMPRIMIMOS 
print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")