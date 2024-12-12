#clase

class Auto:
    marca = "nissan";
    modelo = 2024;
    palca = "123-abc";

taxi = Auto()
print("El modelo es: ", taxi.modelo)
print("La marca es: ", taxi.marca)
print("La placa es: ", taxi.palca)

class persona:
    doctor = "Victor"
    apellido = "Gómez"
    edad = 30
print(persona.doctor)
print(persona.apellido," ",persona.edad)

class jugadores_a:
    j1 = "Messi"
    j2 = "C. Ronaldo"

class jugadores_b:
    j3 = "Marcelo"
    j1 = "Falcao"

print(jugadores_b.j3)
print(jugadores_b.j1)
print(jugadores_a.j2)
print(jugadores_a.j1)

class nombre:
    pass
victor = nombre()
maria = nombre()

#objeto.atributo = valor

victor.edad = 33
victor.sexo = "Masculino"
victor.pais = "Bolivia"

maria.edad = 25;
maria.sexo =  "Femenino"
maria.pais = "Colombia"

print("La edad es: ",victor.edad)
print("La edad es: ",maria.edad)

print("El pais es: ",maria.pais)
print("El pais es: ",victor.pais)



