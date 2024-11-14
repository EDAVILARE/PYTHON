print("***************ejercicio de lista*******************");
#escriba un programa donde tenga una lista y que a continuacion elimine los elementos repetidos, por ultimo mostrar la lista
lista = [1,2,3,"Edwin",3,3,2,"Edwin",2,2,1,4];
print(lista);
conjunto = set(lista); #para eliminar los elemntos repetidos, se convierte en un conjunto la lista
lista = list(conjunto);#luego, se convierte el conjunto en una lista, la lista no tendra elementos repetitivos
print (conjunto); #se imprime el conjunto
print(lista);#se imprime la lista

#OTRO MODO DE HACER EL PROGRAMA
lista1 = [1,2,3,"Edwin",3,3,2,"Edwin",2,2,1,4];
lista1 = list(set(lista1)); #primero, convierte la lista en un conjunto, luego, convierte el conjunto en lista
print(lista1);




















