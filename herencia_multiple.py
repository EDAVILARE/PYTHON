#herencia multiple
class telefono:
    def __init__(self):
        pass
    def llamar(self):
        print("Lamando....")
    def ocupado(self):
        print("ocupado...")
class camara:
    def __init__(self):
        pass
    def fotografia(self):
        print("Tomando Fotografia...")
class reproduccion:
    def __init__(self):
        pass
    def reproduccion_musica(self):
        print("Reproduciendo musica...")
    def reproducir_video(self):
        print("Reproducir un video")

class smartphone(telefono,camara,reproduccion):
    def __del__(self): # es un metodo especial, se usa para limpiar los recursos
        print("Telefono apagado")

movil = smartphone()
print(dir(movil)) #directorio con acciones que se pueden aplicar a movil

print(movil.fotografia())
print(movil.llamar())
print(movil.reproduccion_musica())
print(movil.reproducir_video())
del movil #llama al metodo __del__ para limpiar los recursos















