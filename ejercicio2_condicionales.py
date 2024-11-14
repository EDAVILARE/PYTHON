print("**************EJERCICIO DE CONDICIONALES *************")
#HACER UN PROGRAMA QUE PIDA 3 NUMEROS Y DETERMINE CUAL ES EL MAYOR

numero1 = float(input("Ingrese un numero 1: "));
numero2 = float(input("Ingrese un numero 2: "));
numero3 = float(input("Ingrese un numero 3: "));

if numero1 >= numero2 and numero1 >= numero3 : #se pone >= para cuando hay dos numeros iguales.
    print("El numero mayor es: ", numero1);
    print (f"El numero menor es: {numero1:.2f}");
elif numero2 >= numero1 and numero2 >= numero3 :
    print("El numero mayor es: ", numero2);
    print (f"El numero menor es: {numero2:.2f}");
elif numero3 >= numero1 and numero3 >= numero2 :
    print("El numero mayor es: ", numero3);
    print (f"El numero menor es: {numero3:.2f}");


















