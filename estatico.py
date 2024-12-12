#estatico
import math
class pastel:
    def __init__(self, ingredientes,tamaño):
        self.ingredientes = ingredientes
        self.tamaño = tamaño

    def __repr__(self):
        return f"Pastel({self.ingredientes}, {self.tamaño})"

    def area(self):
        return self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaño_area(A):
     return math.pi * A ** 2

nuevo_pastel  = pastel(['harina', 'azucar','leche', 'crema'],4)
print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
print(nuevo_pastel.area())
print(nuevo_pastel.tamaño_area(4))













