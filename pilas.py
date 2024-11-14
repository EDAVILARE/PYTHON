print("****************PILAS*********************");

pila = ["libro1","libro2","libro3","libro4","libro5"];
#AGREGAR ELEMENTOS A LA PILA
pila.append("libro6"); #agrega un elemento al final de la pila
pila.append("libro7"); #agrega un elemento al final de la pila
print(pila);
#ELIMINAR ELEMENTOS DE LA PILA
pila.pop(); #elimina el ultimo elemento de la pila
print(pila);

n=pila.pop(); #elimina el ultimo elemento de la pila
print("Eliminando el elemento",n,"de la pila");
print(pila);

n1=pila.pop(); #elimina el ultimo elemento de la pila
print(f"Eliminando el elemento {n1} de la pila");
print(f"Los elemntos de la pila son: {pila}");










