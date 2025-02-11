Num1 = float(input("Introduce el primer numero de rango: \n"))

Num2 = float(input("Introduce el segundo numero de rango: \n"))

N = float(input("Introduce numero a comparar: \n"))

if N > Num1 and N < Num2:
    print(f"El numero {N} es mayor a {Num1} y menor a {Num2}")

else:
    print(f"El numero {N} no esta en Rango")

