print("**************COLAS CON LISTAS****************");
#avanzan como las colas del banco FIFO

cola = ["Edwin","Juan","Carlos","Luis","Maria","Pedro"];
print(cola);

print("Tamaño de la cola: ", len(cola));
print("Primer elemento de la cola: ", cola[0]);
print("Ultimo elemento de la cola: ", cola[-1]);
print("Ultimo elemento de la cola a eliminar: ", cola.pop());
print(cola);

#AGREGANDO ELEMENTOS A LA COLA
cola.append("Enrique");
cola.append("Alberto");
print(cola);

#SACANDO ELEMENTOS DE LA COLA
print("Atendiendo a ",cola.pop(0)," en el banco");
print(cola);
print("Atendiendo a ",cola.pop(0)," en el banco");
print(cola);
print("Atendiendo a ",cola.pop(0)," en el banco");
print(cola);
print("Atendiendo a ",cola.pop(0)," en el banco");
print(cola);
print("Atendiendo a ",cola.pop(0)," en el banco");
print(cola);
a = cola.pop(0);
print("Atendiendo a ",a," en el banco");
print(f"Atendiendo a {a} en el banco");
print(cola);
a = cola.pop(0);
print("Atendiendo a ",a," en el banco");
print(f"Atendiendo a {a} en el banco");
print(cola);

cola.append("Enrique");
cola.append("Alberto");
cola.append("Juan");
cola.append("Maria");
print(cola);

cola.insert(0,"Luis");
cola.insert(0,"Carlos");
print(cola);

from collections import deque
cola = deque(["Edwin","Juan","Carlos","Luis","Maria","Pedro"]);
print("Se elimina a: ",cola.popleft())
print(cola);
print("Se elimina a: ", cola.pop());
print(cola);
cola.append("Enrique");
print(cola);
cola.insert(4,"Luis");#agraga un elemento en la posicion 4 o en la posicion que se escoga
print(cola);




















