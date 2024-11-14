print("********************ejercico 2 de  listas*****************")
#escriba un programa que tenga dos listas y que a continuacion cree las siguienets listas (en las que no debe haber repeticiones)

lista1  = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
lista2 =[2,4,6,8,9,7,2,7,8,9,6,30,40,50,60,70];
print(lista1);
print(lista2);

#eliminar los elementos repetidos de ambas lista
a = set(lista1); #se convierte la lista1 en un conjunto, para que no haya repeticiones
print(f"Se elimina las repeticiones {a}."); #luego se imprime el conjunto
b = set(lista2); #se convierte la lista2 en conjunto, para que no haya repeticiones
print(f"Se elimina las repeticiones {b}."); #luego se imprime el conjunto

#union de dos conjuntos
union = list(set(lista1) | set(lista2)); # set -> convierte la lista en conjuntos, | -> junta los conjuntos, list -> convierte el conjunto en lista
print(f"Los valores que no se repien de ambas listas son: {union}."); #imprime los valores que no se repiten en ambos conjuntos



solo_lista1 = list(set(lista1) - set(lista2));
print(f"Los valores que solo estan en la lista1 son: {solo_lista1}."); #imprime los valores que solo estan en la lista1

solo_lista2 = list(set(lista2) - set(lista1));
print(f"Los valores que solo estan en la lista2 son: {solo_lista2}."); #imprime los valores que solo estan en la lista2

#interseccion de dos conjuntos
interseccion = list(set(lista1) & set(lista2));
print(f"Los valores que se repiten en ambas listas son: {interseccion}."); #imprime los valores que se repiten en ambos conjuntos


















