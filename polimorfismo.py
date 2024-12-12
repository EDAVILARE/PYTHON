# polimorfismo -> poli = muchas o varias - morfismo --> formas
#sobrecargas
class auto:
    rueda = 4
    def desplazamiento(self):
        print("El auto se esta desplazando sobre 4 ruedas")
class moto:
    rueda = 2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")

auto1  = auto()
auto1.desplazamiento()
moto1 = moto()
moto1.desplazamiento()

class animales:
    def __init__(self, nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass

class leon(animales):
    def tipo_animal(self):
        print( f"{self.nombre} es un león, un animal salvaje")

class perro(animales):
    def tipo_animal(self):
        print( f"{self.nombre} es un perro, un animal domestico")


nuevo_animal = leon("Simba")
nuevo_animal.tipo_animal()
nuevo_animal1 = perro("Buddy")
nuevo_animal1.tipo_animal()

















