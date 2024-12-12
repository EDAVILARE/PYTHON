#metodos
from idlelib.colorizer import prog_group_name_to_tag


class matematica:
    def suma(self):
        self.num1 = 200
        self.num2 = 300
        pass
    pass
s = matematica()
s.suma()
print(s.num1 +s.num2)

class ropa:
    def __init__(self):
        self.marca = "Topitop"
        self.color = "rojo"
        self.talla = "M"
        pass
camisa = ropa()
print(camisa.marca)
print(camisa.color)
print(camisa.talla)

class calculadora:
    def __init__(self, numero1, numero2):
        self.suma = numero1 + numero2
        self.resta = numero1 - numero2
        self.producto = numero1 * numero2
        self.division = numero1 / numero2
        pass
operacion = calculadora(20,10)
print("La multiplicacion es: ",operacion.producto)
print("La division es: ",operacion.division)
print("La resta es: ",operacion.resta)
print("La suma es: ",operacion.suma)





















