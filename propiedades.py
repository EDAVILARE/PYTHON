#propiedades
class empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre #encapsulamineto
        self.__salario = salario

    def __getnombre(self):
        return self.__nombre
    def __getsalario(self):
        return  self.__salario

    def __setnombre(self, nombre):
        self.__nombre = nombre
    def __setsalario (self, salario):
        self.__salario = salario

    def __delnombre(self):
        del self.__nombre
    def __delsalario(self):
        del self.__salario

    nombre = property(fget = __getnombre,
                                    fset = __setnombre,
                                    fdel = __delnombre,
                                    doc = "Propiedad para el nombre del empleado")
    salario = property(fget = __getsalario,
                                    fset = __setsalario,
                                    fdel = __delsalario,
                                    doc = "Propiedad para el salario del empleado")

empleado2 = empleado("Hector", 3000)
empleado2.nombre = "Sara"
empleado2.salario = 5000
print("El empleado es: ", empleado2.nombre,", el salario es: ", empleado2.salario)
help(empleado2)

# empleado1 = empleado("Victor",2000)
# print("El empleado es: ",empleado1.getnombre(),", el salario es: ",empleado1.getsalario())
#
# empleado1.setnombre("Raul")
# print("El empleado es: ",empleado1.getnombre(),", el salario es: ",empleado1.getsalario())














