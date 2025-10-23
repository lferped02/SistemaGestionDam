class Persona:
    def __init__(self, nombre="Anonimo", edad=0):
        self.nombre = nombre
        self.edad = edad

persona = Persona()
persona2 = Persona("Lucia")
persona3 = Persona("Juan",22)

print (persona)
print (persona2)
print (persona3)