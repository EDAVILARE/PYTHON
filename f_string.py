# f-string
#format %
#str.format()
curso = "Python"
print("Tutoriales de  % s"%curso)

nombre = "Edwin"
edad = 33
print("Hola soy, %s y tengo %s años."%(nombre,edad))

print("Hola, mi nombre es {} y mi edad es: {} años.".format(nombre,edad))
print(f"Hola, mi nombre es {nombre} y mi edad es: {edad} años.")
print("Hola, mi nombre es", nombre ," y mi edad es:",edad,"años.")

class estudiante:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #def __str__(self): #es la representacion informal de una cadena o un objeto
    #    return f"Mi nombre es: {self.nombre}, mi aplellido es: {self.apellido}, y mi edad es: {self.edad} años."
    def __repr__(self):
            return f"Mi nombre es: {self.nombre}, mi aplellido es: {self.apellido}, y mi edad es: {self.edad} años."

nuevo_estudiente = estudiante("Edwin", "Davila",33)
print(f"{nuevo_estudiente !r}") #se imprime este objeto a partir del metodo repr
