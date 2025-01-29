#### UEA ####
#### JUAN GABRIEL ZURITA MANOBANDA #####
#### TAREA SEMANA 2 ####
class Musico:
    def __init__(self, nombre, experiencia, creatividad, energia):
        # Encapsulación: Los atributos están encapsulados dentro de la clase Musico
        self.nombre = nombre
        self.experiencia = experiencia
        self.creatividad = creatividad
        self.energia = energia

    def atributos(self):
        # Encapsulación: Métodos para acceder y mostrar los atributos
        print(self.nombre, "(")
        print("  Experiencia:", self.experiencia)
        print("  Creatividad:", self.creatividad)
        print("  Energía:", self.energia)

    def esta_listo(self):
        return self.energia > 0

    def descansar(self):
        # Encapsulación: Lógica para recuperar energía
        self.energia += 10
        print(self.nombre, "ha recuperado energía. Energía actual:", self.energia)

    def tocar(self):
        # Abstracción: Método abstracto que obliga a las subclases a implementarlo
        raise NotImplementedError("Este método debe ser implementado por subclases")


class Guitarrista(Musico):
    def __init__(self, nombre, experiencia, creatividad, energia, tipo_guitarra):
        # Herencia: Uso del constructor de la clase base
        super().__init__(nombre, experiencia, creatividad, energia)
        self.tipo_guitarra = tipo_guitarra

    def atributos(self):
        super().atributos()
        print("  Tipo de guitarra:", self.tipo_guitarra)

    def tocar(self):
        # Polimorfismo: Implementación específica del método tocar
        if self.esta_listo():
            print(self.nombre, "está tocando un impresionante solo de guitarra.")
            self.energia -= 10
        else:
            print(self.nombre, "está demasiado cansado para tocar.")


class Baterista(Musico):
    def __init__(self, nombre, experiencia, creatividad, energia, tipo_bateria):
        # Herencia: Uso del constructor de la clase base
        super().__init__(nombre, experiencia, creatividad, energia)
        self.tipo_bateria = tipo_bateria

    def atributos(self):
        super().atributos()
        print("  Tipo de batería:", self.tipo_bateria)

    def tocar(self):
        # Polimorfismo: Implementación específica del método tocar
        if self.esta_listo():
            print(self.nombre, "está tocando un gran  solo de batería.")
            self.energia -= 15
        else:
            print(self.nombre, "está muy  cansado para tocar.")


class Vocalista(Musico):
    def __init__(self, nombre, experiencia, creatividad, energia, rango_vocal):
        # Herencia: Uso del constructor de la clase base
        super().__init__(nombre, experiencia, creatividad, energia)
        self.rango_vocal = rango_vocal

    def atributos(self):
        super().atributos()
        print("  Rango vocal:", self.rango_vocal)

    def tocar(self):
        # Polimorfismo: Implementación específica del método tocar
        if self.esta_listo():
            print(self.nombre, "está enloquesiendo a la audiencia con su increíble voz.")
            self.energia -= 5
        else:
            print(self.nombre, "está muy cansado para cantar.")


def concierto(banda):
    print("\n=== Inicia el concierto ===")
    for musico in banda:
        # Polimorfismo: Se llama al método tocar sin importar el tipo específico de músico
        musico.tocar()


# Crear instancias de diferentes músicos
guitarrista = Guitarrista("Carlos", 5, 7, 30, "Eléctrica")
baterista = Baterista("Sofia", 8, 6, 25, "Acústica")
vocalista = Vocalista("Luis", 10, 9, 20, "Tenor")

# Mostrar atributos de cada músico
guitarrista.atributos()
baterista.atributos()
vocalista.atributos()

# Iniciar el concierto
banda = [guitarrista, baterista, vocalista]
concierto(banda)
