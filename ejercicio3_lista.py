print("***************ejercicio 3 de colecciones*************");

persona = [];
persona.append({"nombre":"Eduardo", "apellido":"Avila", "edad":25}); #añade un elemento a la lista
persona.append({"nombre":"Juan", "apellido":"Perez", "edad":28});
persona.append({"nombre":"Jose", "apellido":"Garcia", "edad":24});
print(persona);

persona.sort(key=lambda persona: persona["edad"]); #ordena la lista por la edad
print(persona);

persona.sort(key=lambda persona: persona["nombre"]); #ordena la lista por el nombre
print(persona);

persona.sort(key=lambda persona: persona["apellido"]); #ordena la lista por el apellido
print(persona);

persona.pop(-1);#elimina el ultimo elemento de la lista
print(persona);

persona.pop(0);#elimina el primer elemento de la lista
print(persona);

persona.insert(0,{"nombre":"Teressa", "apellido":"Gallardo", "edad":33}); #inserta un elemento en la posicion 0
print(persona);

persona.insert(-1,{"nombre":"Pedro", "apellido":"Perez", "edad":28}); #inserta un elemento en la posicion -1
print(persona);

persona.insert(-1,{"nombre":"Claudia", "apellido":"Ramirez", "edad":38}); #inserta un elemento en la posicion -1
print(persona);

persona.insert(-1,{"nombre":"Diana", "apellido":"Garcia", "edad":28}); #inserta un elemento en la posicion -1
print(persona);

persona.sort(key=lambda persona: persona["edad"]); #ordena la lista por la edad
print(persona);

persona.reverse(); #invierte la lista
print(persona);

print(persona.count({'nombre': 'Claudia','apellido':'Ramirez', 'edad':38})); #cuenta cuantas veces se repite un elemento en la lista

persona.remove({'nombre': 'Claudia','apellido':'Ramirez', 'edad':38}); # remove se usa con la clave no con las posiciones
print(persona);

# append añade un elemento a la lista, extend añade varios elementos a la lista
persona.extend([{"nombre":"Juan", "apellido":"Perez", "edad":28}, {"nombre":"Jose", "apellido":"Garcia", "edad":24}]) #añade varios elementos a la lista
print(persona);

index = persona.index({"nombre":"Juan", "apellido":"Perez", "edad":28}); #busca un elemento en la lista y devuelve la posicion
print(index);

persona.clear(); #limpia la lista o elimina  la lista
print(persona); # imprime la lista vacia, pues, se elimino la lista en la fila anterior

print("Eso es todo en este archivo, hasta luego. 😀😃😄")




