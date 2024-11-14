print("******************* BUCLE FOR ******************")

for i in range(10):
    print(i)
    if i == 4:
        break
print("Hola mundo. 🤑🤑🤠💥💥💥🤠🤑🤑 ")

for i in range(50): #rango de 0 al 50
    print(i,end=", ")
    #i += 1; #es opcional igual imprime el bucle
print("\n");

for i in range(-10,50): #rango de -10 al 50
    print(i,end=", ")
    #i += 1; #es opcional igual imprime el bucle
print("\n");

for i in range(10,20): #rango de 10 al 20
    print(i,end=", ")
    #i += 1; #es opcional igual imprime el bucle
print("\n");

for i in range(10,20+11): #se puede sumar en el rango
    print(i,end=", ")
    #i += 1; #es opcional igual imprime el bucle
print("\n");

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(f"Hola mundo. 🤑🤑🤠💥💥💥🤠🤑🤑 {i} veces")
    i += 1; #i = i + 1;
    if i == 5:
        break;

coleccion = ["Eduardo", "Juan", "Jose", "Teressa", "Pedro", "Claudia", "Diana", "Gabriela", "Edwin"];

for i in coleccion:
    print(f"Los elementos de la coleccion son: {i}");
    if i == "Gabriela":
        break;

print("\n\tbucle for con range(len(coleccion))");
for i in range(len(coleccion)):
    print(f"Los elementos de la coleccion son: {coleccion[i]}");
    if coleccion[i] == "Diana":
        break;

print("\n\tbucle for con diccionarios");
coleccion2 = {"nombre":"Eduardo", "apellido":"Avila", "edad":25};
for i in coleccion2:
    print(f"La clave de la coleccion es: {i}");
    print(f"El valor de la coleccion es: {coleccion2[i]}");
    #print(f"Los elementos de la coleccion son: {coleccion2.get(i)}");
    #print(f"Los elementos de la coleccion son: {coleccion2.get('edad')}");
    print(f"La clave es: {i} y el valor es: {coleccion2[i]}");

coleccion2.update({"Mujer":"Teressa", "Cantante":"Gallardo", "Pais":"Rusia"});
print(coleccion2);
for clave, valor in coleccion2.items():
    print(f"La clave es: {clave} y el valor es: {valor}");
    if clave == "Cantante":
        break;

nombre = "Vanessa";
for letra in nombre:
    print(letra,end="-"); #no hace el salto de linea, sino un guion en vez de un enter
print("\n");
for letra in nombre:
    print(f"{letra}",end=" ");#no hace el salto de linea, sino un espacio en vez de un enter
print("\n");
for letra in nombre:
    print(f"{letra}",end="\t");#no hace el salto de linea, sino un tab en vez de un enter
print("\n");
for letra in nombre:
    print(f"{letra}",end="");#no hace el salto de linea, sino vacio en vez de un enter
print("\n");
for letra in nombre:
    print(f"{letra}",end="😍🥰😇");#no hace el salto de linea, sino un emoji en vez de un enter
print("\n");





















