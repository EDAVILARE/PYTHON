'''
print("*******CONDICIONALES COMBINADAS **********");
edad = int(input("Ingrese su edad: "));
if edad >= 18:
    print("Usted es mayor de edad 😀😃😄");
    print("Usted puede votar");
elif edad < 0:
    print("El numero es negativo 😅🙁☹️🥺😲😥")
else:
    print("Usted es menor de edad 😀😃😄");
    print("Usted no puede votar");

print("*******CONDICIONALES ANIDADAS **********");
edad1 = int(input("Ingrese su edad: "));
if  0<edad<=110: # ES IGUAL QUE PONER   edad1 > 0 and edad1 <=110
    print("Edad correcta");
    if edad1 >= 18:
        print("Usted es mayor de edad 😀😃😄");
        print("Usted puede votar");
    else:
        print("Usted es menor de edad ������");
        print("Usted no puede votar");
else:
    print("Edad incorrecta");

print("*******CONDICIONALES COMBINADAS **********");
edad2 = int(input("Ingrese su edad: "));
if edad2 > 0 and edad2 <=110: # ES IGUAL QUE PONER  0<edad2<=110
    print("Es una edad correcta.");
    if  18<=edad2<65:
        print("Usted es mayor de edad. 😀😃😄");
        print("Usted puede votar.");
    elif edad2 >= 65:
        print("Usted es mayor de edad. 😀😃😄");
        print("No es obligatorio votar para usted, sino va  a votar no le ponen multa.");
    else:
        print("Usted es menor de edad. 😀😃😄");
        print("Usted no puede votar.");
else:
    print("Es una edad incorrecta.");
    '''
print("*******CONDICIONALES COMBINADAS **********");
edad3 = int(input("Ingrese su edad: "));
if edad3 > 0 and edad3 <=110: # ES IGUAL QUE PONER  0<edad2<=110
    print("Es una edad correcta.");
    if  18<=edad3:
        print("Usted es mayor de edad. 😀😃😄");
        print("Usted puede votar.");
        if edad3 >= 65:
            print("No es obligatorio votar para usted, sino va  a votar no le ponen multa. 😀😃😄");
        else:
            print("Es obligatorio que vaya a votar, sino le van a aponer una multa. 🥺😲😥")
    else:
        print("Usted es menor de edad. 😀😃😄");
        print("Usted no puede votar.");
else:
    print("Es una edad incorrecta.");










