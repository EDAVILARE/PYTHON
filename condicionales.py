from gc import is_finalized
from operator import ifloordiv

print ("**********************CONDICIONALES*******************");

#PRIMER MODO DE  HACER LAS CONDICIONALES
numero = int(input("Ingrese un numero: "));
if numero > 0 :
    print ("El numero es positivo");
if numero == 0 :
    print("El numero es igual a 0");
if numero <0 :
    print("El numero es negativo");

#SEGUNDO MODO DE HACER LAS CONDICIONALES
numero1 = float(input("Digite un numero: "));
if numero1 <= 30 and numero1 >= 0 :
    print ("El numero es menor  o igual a 30 y mayor o igual a 0");
    print ("El numero es positivo");
elif numero1 > 30 and numero1 <= 60 :
    print ("El numero es mayor a 30 y menor o igual a 60");
    print ("El numero es positivo");
elif numero1 < 0 :
    print("El numero es negativo");
else:
    print("El numero es mayor a 60");

#OTRO MODO DE HACER AS CONDICIONALES
numero2 = float(input("digite un numero: "));
if numero2 >= 0:
    print ("El numero es positivo 😃😈🤩😘☺️😚✌️💘💖");
else :
    print("El numero es negativo ☹️😮🥺😳🥹😅😓😫😡😈");

print ("******************FIN DEL PROGRAMA****************");





























