print("*********************conjuntos******************");
conjunto = set([1,2,3,4,5,6,7,8,9,10]);
print(conjunto);
conjunto2 = set({1,2,3,4,5,6,7,8,9,10});
print(conjunto2);

conjunto3 = set();
conjunto3={1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10}; # no almacena valores repetidos
#imprime solo 10 numeros, pues, no almacena valores repetidos
#tampoco guarda otros conjuntos, listas, tuplas o arrays
print(conjunto3);

conjunto3.add(11); #agrega un elemento al conjunto
print(conjunto3);

conjunto3.update([11,12,13,14,15]); #agrega elementos al conjunto
print(conjunto3);

conjunto3.remove(11); #elimina un elemento del conjunto
print(conjunto3);

conjunto3.discard(12); #elimina un elemento del conjunto
print(conjunto3);

conjunto3.clear(); #elimina todos los elementos del conjunto
print(conjunto3);

conjunto4 = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10};
print(conjunto4);

print(3 in conjunto4); 














