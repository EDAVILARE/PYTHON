print("*****************ejercicio de condicionales *****************");
#VERIFICAR SI LOS NUMEROS SON PARES O IMPARES
numero1 = float(input("Ingrese un numero: "));
numero2 = float(input("Ingrese otro numero: "));

if numero1%2 == 0 :
    print("El primer numero ingresado es par :) ");
else:
    print ("El primer numero ingresado es impar :(");
if numero2%2 == 0 :
    print("El segundo numero ingresado es par :) ");
else:
    print("El segundo numero ingresado es impar :( ");

#OTRO MODO DE HACER EL CONDICIONAL

if numero1%2 == 0  and numero2%2 == 0:
    print("Ambos numeros son pares :) ");
elif numero1%2!= 0 and numero2%2!= 0:
    print("Ambos numeros son impares :( ");
elif numero1%2 == 0 and numero2%2!= 0:
    print(f"El numero {numero1:.0f} es par y el numero {numero2:.0f} impar :( ");
else:
    print(f"El numero {numero2:.0f} es par y el numero {numero1:.0f} impar :( ");














