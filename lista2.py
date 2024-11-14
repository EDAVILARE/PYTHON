print("****************LISTA******************");
lista = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
lista.append(100); #agrega un elemento al final de la lista
lista.append(200); #agrega un elemento al final de la lista
lista.append("Edwin"); #agrega un elemento al final de la lista
print("La lista tiene un a longitud de ", len(lista), "elementos");
print(lista);
lista.insert(0, "Davila"); #indicar la posicion en index y contenido en object
lista.insert(1,"Reaño");
print(lista[:]);
lista.remove("enero"); #elimina el primer elemento que encuentra
print(lista[:]);
lista.pop(); #elimina el ultimo elemento de la lista
print(lista[:]);
lista.pop(1); #elimina el elemento en la posicion indicada
print(lista[:]);
print(lista.count("Davila")); #cuenta el numero de veces que se repite un elemlista.extend(["Enero", "Febrero", "Marzo"])); #agrega una lista al final de la lista
lista.extend(["Enero", "Febrero", "Marzo"]); #agrega una lista al final de la lista
print(lista[:]);
lista.clear(); #elimina todos los elementos de la lista
print(lista[:]);
lista.extend(["Enero", "Febrero", "Marzo", "Abril"]); #agrega una lista al final de la lista
lista.extend(["Mayo", "Junio", "Julio"]); #agrega una lista al final de la lista
print(lista[:]);
lista.reverse(); #invierte la lista
print(lista[:]);
lista.sort(); #ordena la lista de forma alfabetica
print(lista[:]);
lista.sort(reverse=True); #ordena la lista de forma alfabetica de Z a A o al reves
print(lista[:]);
lista.sort(key=str.lower); #ordena la lista de forma alfabetica de A a Z
print(lista[:]);
lista.reverse()
print(lista[:]);
lista.sort(key=str.upper); #ordena la lista de forma alfabetica de A a Z
print(lista[:]);

print ("Abril" in lista); #busca un elemento en la lista
print(lista.index("Enero")); #busca el indice de un elemento en la lista
print(lista.count("Enero")); #busca el numero de veces que se repite un elemento en la lista

lista*=3;#multiplica la lista por 3 o repita la lista 3 veces
print(lista[:]);

lista[0] = "Enero"; #cambia el elemento en la posicion 0
print(lista[:]);




