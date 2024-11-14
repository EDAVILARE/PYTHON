print("***************EJERCICIO 5 CONDICIONALES*************")
saldo =1000.00;
print("\t.:MENU PRINCIPAL:.");
print("1. Ingresar dinero en la cuenta.");
print("2. Retirar dinero de la cuenta.");
print("3. mostrar saldo disponible.");
print("4. Salir.\n");
opcion = int(input("Ingrese una opcion del menu principal: "));

if opcion == 1:
    extra = float(input("Cuánto dinero desea ingresar: "));
    saldo = saldo + extra;
    print(f"Dinero en la cuenta: {saldo:.2f}");
elif opcion == 2:
    retiro = float(input("Cuánto dinero desea retirar: "));
    if retiro > saldo:
        print("No se puede retirar esa cantidad, saldo insuficiente");
    else:
        saldo = saldo - retiro;
        print(f"Dinero en la cuenta: {saldo:.2f}");
elif opcion == 3:
    print(f"Dinero en la cuenta: {saldo:.2f}");
elif opcion == 4:
    print("Gracias por utilizar el sistema.");
else:
    print("Error. Ingrese una opcion del menu principal");






















