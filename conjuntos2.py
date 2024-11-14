print("*******************CONJUNTOS*********************");
z  =  set();
z = {11,12,13,14,15,16,17,18,19,20};
a = {1,2,3,4,5,6,7,8,9,10};
b = {1,2,3,4,5,6,7,8,9,10};
x = {6,7,8,9,10,11,12,13,14,15}
y = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};

print(a == z); #a es igual a b
print(len(a) == len(z)); #a y b tienen el mismo numero de elementos o longitud)
#UNIR O JUNTAR DOS CONJUNTOS
c = z | a; #union de conjuntos
print(a | b); #union de conjuntos, no imprime valores repetidos
print (c);

#INTERSECCION DE CONJUNTOS
d = x & a; #interseccion de conjuntos
print(d) #imprime los valores que se repiten en ambos conjuntos

#DIFERENCIA DE CONJUNTOS
e = x - a; #diferencia de conjuntos, descuenta los valores de A que estan en X
print(e) #imprime los valores de X que no estan en A
f = a - x; #descuenta los elementos de X que estan en A
print(f);
g = x ^ a; #diferencia simétrica de conjuntos, valores que estan en A y X, descontando los valores que se repiten
print (g);

print(a.issubset(y)); #comprueba si un conjunto esta dentro de otro, A es subconjunto de Y
print(y.issuperset(a)); #comprueba si un conjunto esta dentro de otro, Y es un superconjunto de A, o A esta dentro de Y
print(a.isdisjoint(z)); #comprueba si dos conjuntos son disconexos (los valores no se repiten)

#CONJUNTO INMUTABLE (NO SE PUEDE CAMBIAR O ALTERAR LOS VALORES);
w = frozenset({21,22,23,24,25,26,27,28,29});
#w.add(30); #no se puede añadir un valor a un conjunto inmutable
print(w);





'''
print(a <= b); #esta a dentro de b
print(a >= b); #esta b dentro de a
print(a < b); #esta a dentro de b
print(a > b); #esta b dentro de a
print(a!= b); #esta a dentro de b

'''































