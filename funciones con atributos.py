#funciones para atributos
class persona:
    edad = 33
    nombre = "Edwin"
    pais = "Brasil"

doctor = persona()
''' 
print("El nombre es: ",persona.nombre)
print("El nombre es: ",getattr(persona,"nombre"))
print("Tiene atributo nombre: ",hasattr(persona,"nombre"))

print("La edad es: ",persona.edad)
print("La edad es: ",getattr(persona,"edad"))
print("Tiene atributo edad: ",hasattr(persona,"edad"))
print("Tiene atributo sexo: ",hasattr(persona,"sexo"))

print("El nombre es: ",doctor.nombre)
print("El nombre es: ",getattr(doctor,"nombre"))
print("Tiene atributo nombre: ",hasattr(doctor,"nombre"))
print("La edad es: ",doctor.edad)
print("La edad es: ",getattr(doctor,"nombre"))
print("Tiene atributo edad: ",hasattr(doctor,"edad"))
print("Tiene atributo sexo: ",hasattr(doctor,"sexo"))
'''
print(doctor.nombre)
doctor.nombre = "Jorge" # cambia de nombre al atributo nombre
print(doctor.nombre)
setattr(doctor,"nombre","Pedro") #cambia de nombre al atributo nombre
print(doctor.nombre)

delattr(persona, "pais") # elimina el atributo de la clase

print(doctor.nombre)
print(doctor.edad)
# print(doctor.pais) # sale un error, pues, el atributo pais fue eliminado











