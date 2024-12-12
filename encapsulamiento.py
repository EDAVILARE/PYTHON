#encapsulamiento
class cliente:
    def __init__(self):
        self.__codigo = 4321 #se encapsula con dos rayas bajas
    def __cuenta(self):
        print("Cuenta de procesamiento")
    def getcodigo(self):
        return self.__codigo

persona = cliente()
# print(persona.__codigo)
#objeto._nombre de la clase__nombre del atributo
print(persona._cliente__codigo)
persona._cliente__cuenta()

























