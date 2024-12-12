#herencia
class pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion (self):
        return "{} es un pokemon de tipo: {}".format(self.nombre,self.tipo)

class pikachu(pokemon):
    def ataque(self, tipoataque):
        return "{} tipo de ataque {}".format(self.nombre, tipoataque)

class charmander(pokemon):
    def ataque(self, tipoataque):
        return "{} tipo de ataque {}".format(self.nombre, tipoataque)

nuevo_pokemon = pikachu("Boby", "Electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impacto trueno"))

nuevo_pkemon1 = charmander("Brandom", "Fuego")
print(nuevo_pkemon1.descripcion())
print(nuevo_pkemon1.ataque("fuego lento"))










