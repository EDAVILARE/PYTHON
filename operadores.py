print("****************OPERADORES ARITMETICOS*****************")

numero1 = 1000;
numero2 = 160;

suma = numero1 + numero2; # operador de suma
print(suma);
resta = numero1 - numero2; # operador de resta
print(resta);
division = numero1 / numero2; # operador de division
print(division);
division_entera = numero1 // numero2; # operador de division entera
print(division_entera);
multiplicacion = numero1 * numero2; # operador de multiplicacion
print(multiplicacion);
modulo = numero1 % numero2; # operador de modulo
print(modulo);
exponente = numero1 ** numero2; # operador de exponente
print(exponente);

print("****************OPERADORES RELACIONALES*****************")

numero3 = 1000;
numero4 = 160;

mayor = numero3 > numero4; # operador de mayor
print(mayor);
menor = numero3 < numero4; # operador de menor
print(menor);
igual = numero3 == numero4; # operador de igual
print(igual);
diferente = numero3!= numero4; # operador de diferente
print(diferente);
mayor_igual = numero3 >= numero4; # operador de mayor o igual
print(mayor_igual);
menor_igual = numero3 <= numero4; # operador de menor o igual
print(menor_igual);

print("****************OPERADORES LOGICOS*****************")

numero5 = 1000;
numero6 = 160;

AND = numero5 > numero4 and numero5 > numero6; # operador and
print(AND);
OR = numero5 > numero4 or numero5 > numero6; # operador or
print(OR);
NOT = not numero5 > numero4; # operador not
print(NOT);


print("****************OPERADORES DE ASIGNACION*****************")

numero7 = 1000;
numero8 = 160;

numero7 += numero8; # operador de suma y asignacion
print(numero7); #SE SUMA 160, resultado 1160
numero7 -= numero8; # operador de resta y asignacion
print(numero7);#1160 menos 160, resultado 1000
numero7 *= numero8; # operador de multiplicacion y asignacion
print(numero7);#1000 multiplicado por 160, resultado 160000
numero7 /= numero8; # operador de division y asignacion
print(numero7);#160000 dividido por 160, resultado 1000
numero7 %= numero8; # operador de modulo y asignacion
print(numero7);#1000 modulo 160, resultado 40
numero7 **= numero8; # operador de exponente y asignacion
print(numero7);#40 elevado a la 160, resultado 16777216000000000000000000000000000000000000000000000000000000000000000000000000
numero7 //= numero8; # operador de division entera y asignacion
print(numero7);#167772160000000000000000000000000000000000000000000000000000000000000000000000000000000000000


a = 10;
b = 20;
c = 30;

resultado = not(((a<b) and (b<c)) or ((a<b) and (b>c)));
print(resultado);
resultado1 = (a<b) and (b<c) or (a<b) and (b>c);
print(resultado1);
resultado2 = ((a<b) and (b<c)) or ((a<b) and (b>c));
print(resultado2);
















