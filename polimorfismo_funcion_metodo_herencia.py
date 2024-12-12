#polimorfismo por funcion
class tomate:
    def tipo(self):
        print("Vegetal")
    def color(self):
        print("Rojo")

class manzana:
    def tipo(self):
        print("Fruta")
    def color(self):
        print("Verde")

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = tomate()

funcion(nuevo_tomate )

nueva_manzana = manzana()

funcion(nueva_manzana)

#POLIMORFISMO CON METODOS
class colombia:
    def capital(self):
        print("Pais: Colombia - > capital: Bogota.")
    def idioma(self):
        print("Idioma: Español.")

class francia:
    def capital(self):
        print("Pais: Francia - > capital: Paris.")
    def idioma(self):
        print("Idioma: Frances.")

colombiano = colombia()
frances = francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()

#POLIMORFISMO CON HERENCIA
class aves:
    def volar(self):
        print("La mayoria de las aves pueden volar, pero algunas no.")
class aguila(aves):
    def volar(self):
        print("La aguila puede volar mucho mas rapido.")

class gallina(aves):
    def volar(self):
        print("La gallina puede volar poco.")
#polimorfismos -> diferentes clase con el mismo nombre en los metodos
objeto_ave = aves()
objeto_ave.volar()
objeto_aguila = aguila()
objeto_aguila.volar()
objeto_gallina = gallina()
objeto_gallina.volar()








