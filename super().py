#metodo super
class maniferos:
    def __init__(self,nombre):
        print(nombre,"es un animal de sangre caliente.")

class leon(maniferos):
    def __init__(self):
        print("El leon es un animal de cuatra patas.")
        super().__init__("Simba")
        # maniferos.__init__(self,"Simba") # es lo mismo que: super().__init__("Simba")

nuevo_leon = leon()





















