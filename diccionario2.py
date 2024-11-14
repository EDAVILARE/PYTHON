print("**********************diccionario******************");

equipo = {10:"Edwin", 11:"Messi", 12:"Ronaldo", 13:"Neymar", 14:"Ronaldiño", 15:"Pele"};
print(equipo);
print(equipo[10]); #el 10 es la clave no el indice o la posicion del elemento
print(equipo[13]);#el 13 es la clave que esta tipeado dentro del diccionario

print(equipo.keys()); #imprime las claves del diccionario
print(equipo.values()); #imprime los valores del diccionario
print(len(equipo)); #imprime la cantidad de elementos del diccionario

equipo[16] = "Paolo Guerrero"; #agrega un elemento al diccionario
print(equipo);

print(equipo.get(16)); #imprime el valor del elemento de la clave 16
print(equipo.get(17,"No existe ese jugador")); #imprime el mensaje pues la clave 17 no existe

print(equipo.pop(16)); #elimina el elemento de la clave 16
print(equipo);

print(equipo.popitem()); #elimina el ultimo elemento del diccionario
print(equipo);

print(equipo.clear()); #elimina todos los elementos del diccionario
print(equipo);

print(equipo.update({16:"Paolo Guerrero"})); #actualiza el valor de la clave 16
print(equipo);
equipo.update({11:"Edwin"});
print(equipo);
equipo.update({12:"Messi",13:"Ronaldo",14:"Neymar",15:"Cristiano"}); #actualiza o agrega en el diccionario
print(equipo);

print(10 in equipo); #verifica si existe la clave 10
print(10 not in equipo); #verifica si no existe la clave 10
print(11 in equipo); #verifica si existe la clave 11








