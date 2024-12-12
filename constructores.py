#constructor

class  persona:
    pass
    def __init__(self,nombre, año, frase):
        self.nombre = nombre
        self.año = año
        self.frase = frase
    def descripcion(self):
        return " {} tiene {} años.".format(self.nombre,self.año)
    def comentario(self):
        return " {} dice: {}".format(self.nombre, self.frase)

doctor = persona("Edwin", 33,"Hola que tal")
print(doctor.nombre)
print(doctor.año)
print(doctor.descripcion())
print(doctor.comentario())

#modificar un atributo
class email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)












