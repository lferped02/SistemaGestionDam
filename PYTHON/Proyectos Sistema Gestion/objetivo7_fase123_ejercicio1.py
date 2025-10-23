# Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# Definir una clase Vehiculo y una clase Coche que herede de Vehiculo.
 # Clase Vehiculo: representa un vehículo genérico con marca y velocidad.
class Vehiculo:
  #Constructor que inicializa la marca y la velocidad (por defecto 0).
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad
  #Método acelerar: aumenta la velocidad actual en v unidades.
    def acelerar(self, v):
        self.velocidad += v

  #Método desacelerar: reduce la velocidad actual en v unidades.
    def desacelerar(self, v):
        self.velocidad -= v
  #Método mostrar_velocidad: muestra la velocidad actual del vehículo.
    def mostrar_velocidad(self):
        print(f"Velocidad actual: {self.velocidad:.2f} km/h")
 
 # Clase Coche: hereda de Vehiculo y añade una bocina.
class Coche(Vehiculo):
  # Constructor que inicializa marca, velocidad y bocina.
    def __init__(self, marca, velocidad=0):
        super().__init__(marca, velocidad)
        self.bocina = "¡tuuut!"
  # Método tocar_claxon: muestra el sonido de la bocina.
    def tocar_claxon(self):
        print(self.bocina)

# Ejemplos de uso / pruebas
 #Crear un objeto coche con marca "Peugeot 208" y velocidad inicial 10.5
coche_1 = Coche("Peugeot 208", 10.5)
 #Mostrar la velocidad inicial
print(f"La velocidad inicial del coche es: {coche_1.velocidad}")
 #Acelerar 50 km/h
coche_1.acelerar(50)
 #Desacelerar 15 km/h
coche_1.desacelerar(15)
 #Mostrar la velocidad actual con texto personalizado
print(f"Tu velocidad actual es: {coche_1.velocidad:.1f} km/h")
 #Tocar el claxon
coche_1.tocar_claxon()
