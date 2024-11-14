print("************ EJERCICIO DE CONDICIONALES ************");
#hacer un programa que pida un caracter e indique si es una vocal o no
letra =str(input("Ingrese una letra: "));

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra es una vocal");
elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("La letra es una vocal");
else:
    print("La letra no es una vocal");


#OTRO MODO DE HACER EL CONDICIONAL
letra2 = str(input("Ingrese un caracter: ").lower()); # .lower() -> tranforma la letra a minuscula
if letra2 == "a" or letra2 == "e" or letra2 == "i" or letra2 == "o" or letra2 == "u":
    print("El caracter es una vocal");
else:
    print("El caracter no es una vocal");
















