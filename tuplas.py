print("*****************tupla******************")
#las TUPLAS son listas o arrays que no se pueden modificar
tupla = (1,2,3,4,4,5,6,7,8,9,10,[1,2,4,4,4,4]); #las tuplas usan parentesis y no corchetes
print(tupla[:]);
print(tupla[0]);
print(tupla[1]);
print(tupla[2]);
print(tupla[3]);
print(tupla[-1]);
print(tupla[0:]);

print(4 in tupla); #busca un elemento en la tupla o array
print(tupla.count(4)); #busca el numero de veces que se repite un elemento en la tupla o array

lista = list(tupla); #convierte una tupla en una lista
print (lista);
tupla = tuple(lista); #convierte una lista en una tupla
print(tupla);
tupla = tupla * 3; #repite la tupla 3 veces
print(tupla[:]);












