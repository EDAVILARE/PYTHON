print("************EJERCICIO 4 DE CONDICIONALES**************")
operador = str(input("Ingrese Sumar, Restar, Multiplicar o Dividir: ").lower());

numero1 = float(input("Ingrese un numero: "));
nuemero2 = float(input("Ingrese otro numero: "));

if operador == "sumar":
    print(f"La suma de {numero1} + {nuemero2} = ", numero1 + nuemero2);
elif operador == "restar":
    print(f"La resta de {numero1} - {nuemero2} = ", numero1 - nuemero2);
elif operador == "multiplicar":
    print(f"La multiplicacion de {numero1} * {nuemero2} = ", numero1 * nuemero2);
elif operador == "dividir":
    print(f"La division de {numero1} / {nuemero2} = ", numero1 / nuemero2);
else:
    print("\nLa operacion no es valida, ingrese Sumar, Restar, Multiplicar o Dividir");
#OTRO MODO DE HACER EL CONDICIONAL ES:

operador = str(input("Ingrese Sumar, Restar, Multiplicar o Dividir: ").lower());

numero1 = float(input("Ingrese un numero: "));
nuemero2 = float(input("Ingrese otro numero: "));

if operador == "sumar":
    suma = numero1 + nuemero2;
    print(f"\nLa suma de {numero1} + {nuemero2} = {suma:.2f}");
elif operador == "restar":
    resta = numero1 - nuemero2;
    print(f"\nLa resta de {numero1} - {nuemero2} = {resta:.2f}");
elif operador == "multiplicar":
    multiplicacion = numero1 * nuemero2;
    print(f"\nLa multiplicacion de {numero1} * {nuemero2} = {multiplicacion:.2f}");
elif operador == "dividir":
    division = numero1 / nuemero2;
    print(f"\nLa division de {numero1} / {nuemero2} = {division:.2f}");
else:
    print("\nLa operacion no es valida, ingrese Sumar, Restar, Multiplicar o Dividir");















