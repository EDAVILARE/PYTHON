#herencia ejemplo practico
class calculadora:
    def __init__(self, numeros):
        self.n = numeros
        self.datos = [0 for i in range(numeros)]
    def ingresardato(self):
        self.datos = [int(input("Ingresar datos: "+str(i+1)+" = ")) for i in range(self.n)]

class operaciones_basicas(calculadora):
    def __init__(self):
        calculadora.__init__(self, 2 ) # que funcione con dos valores

    def suma(self):
        a,b, = self.datos
        sumar = a+b
        print("La suma entre los numeros es: ",sumar)

    def resta(self):
        a,b, = self.datos
        restar = a - b
        print("La resta entre los numeros es: ", restar)

class raiz(calculadora):
    def __init__(self):
        calculadora.__init__(self,1)# solo se neceta un numero

    def cuadrada(self):
        import math
        a,  = self.datos
        print("La raiz cuadrada del numero es: ",math.sqrt(a))

ejemplo = operaciones_basicas()
# print(ejemplo.ingresardato())
# print(ejemplo.suma())
# print(ejemplo.resta())


ejemplo1 = raiz()
# print(ejemplo1.ingresardato())
# print(ejemplo1.cuadrada())

objeto = operaciones_basicas()

print(isinstance(objeto,operaciones_basicas)) #verifica si el objeto esta instanciao o creado
print(isinstance(ejemplo1, raiz))
print(isinstance(ejemplo,operaciones_basicas))


print(issubclass(operaciones_basicas,calculadora)) # verifica si es una subclase
print(issubclass(raiz,calculadora)) # verifica si es una subclase





