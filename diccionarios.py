print ("********************DICCIONARIO******************")

diccionario = {"azul":"blue","rojo":"red","amarillo":"yellow","verde":"green"};

print("azul" in diccionario);
print("azul" not in diccionario);
print(diccionario["azul"]); #traduccion de azul
diccionario["morado"] = "purple" #AGREGA UN ELEMENTO AL DICCIONARIO
print(diccionario);
diccionario["azul"] = "BLUE"; #MODIFICA EL VALOR DEL DICCIONARIO porque el elemento ya existe
print(diccionario);

del (diccionario["verde"]); #elimina un elemento del diccionario
print(diccionario);

diccionario2 = {"Edwin":[33,1.70], "Fernando":[23,1.70], "Juan":[45,1.70]};
print(diccionario2);

#en los diccionarios se pueden poner otros tipos de datos como otros diccionarios, tuplas o listas

diccionario3 = {"Edwin":{"Edad":33, "Altura":1.70}, "Fernando":{"Edad":23, "Altura":1.70}, "Juan":{"Edad":45, "Altura":1.70} };
print(diccionario3);
print("Edwin" in diccionario3);
print("Edwin" not in diccionario3);
print(diccionario3["Edwin"]);







