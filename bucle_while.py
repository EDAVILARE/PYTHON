from importlib import import_module

print("******************* BUCLE WHILE *****************")
import math

numero = 10;

while numero > 0:
    print(f"El numero es: {numero}");
    numero = numero - 1;

numero1 = 10;

while numero1 <= 20 and numero1 >= 10:
    print(f"El numero es: {numero1}");
    numero1 = numero1 + 1;

numero2 = float (input("Digite un numero: "));

while numero2 <0:
    print(f"Erro -> El numero digitado es negativo: {numero2}. 😞🙁☹️😮😲🥺");
    numero2 = float (input("Digite un numero positivo: "));

print(f"\tLa raiz cuadrada de {numero2:.2f} es: {(numero2 ** 0.5):.2f}");
print(f"\tLa raiz cuadrada de {numero2:.2f} es: {math.sqrt(numero2):.2f}");
print(f"\tLa raiz cuadrada de {numero2:.2f} es: {(numero2 ** (1/2)):.2f}");

saludo = 0;
while saludo <= 10:
    print("Hola mundo. 🤑🤑🤠💥💥💥🤠🤑🤑");
    saludo = saludo + 1; # saludo += 1;
















