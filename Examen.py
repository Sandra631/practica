def ejercicio1():
    codigo = """
Nombre = input("Nombre Completo: ")
Carrera = input("Carrera: ")
Semestre = int(input("Semestre: "))
Materia = input("Materia: ")

print(Nombre)
print(Carrera)
print(Semestre)
print(Materia)
"""
    return f"Código:\n{codigo}\n"


def ejercicio2():
    codigo = """
N = 8
M = 2
S = N + M

print("La suma es: ", S)
"""
    resultado = "La suma es: 10"
    return f"Código:\n{codigo}\n\nResultado:\n{resultado}"


def ejercicio3():
    codigo = """
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

resta = numero1 - numero2
multiplicacion = numero1 * numero2

print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")

print("\\n Programa realizado por Sandra Yolotzin")
"""
    return f"Código:\n{codigo}\n"


def ejercicio4():
    codigo = """
import math

radio = float(input("Introduce el radio del círculo en metros: "))
area = math.pi * (radio ** 2)
print(f"El área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados.")
"""
    return f"Código:\n{codigo}\n"


def ejercicio5():
    codigo = """
def es_par (num):
#Verifica si un número es par.
return num % 2 == 0

def suma_de_pares(a, b):
#Verifica si la suma de dos números pares es par.
if es_par(a) and es_par(b):
suma = a + b
return True, suma
return False, None
# Devuelve True si la suma es par, junto con la suma
# Si no son pares, devuelve False
  
#Interacción con el usuario
print("Bienvenido a la demostración del teorema: La suma de dos números pares es siempre par.")
numero1 = int(input("Introduce el primer número par: "))
numero2 = int(input("Introduce el segundo número par: "))
#Verificar si los números ingresados son pares
if es_par(numero1) and es_par (numero2) :
 es_suma_par, resultado = suma_de_pares(numero1, numero2)
if es_suma_par:
print(f"La suma de {numero1} y {numero2} es {resultado}, que es un número par.")
else:
print (f"Error:la suma de {numero1} y {numero2} no es par.")
else:
print("Al menos uno de los números no es par. Asegurate de ingresar números pares.")
"""
    return f"Código:\n{codigo}\n"


def ejercicio6():
    return "MAYOR QUE 10"


def ejercicio7():
    return "POSITIVO O NEGATIVO"


def ejercicio8():
    codigo = """
import random

NumA = random.randint(1, 10)
adivina = int(input("Adivina el número entre 1 y 10: "))

print(f"El número aleatorio es: {NumA}.")
if adivina == NumA:
    print("Correcto, has adivinado el número.")
else:
    print(f"Incorrecto, el número era: {NumA}.")
"""
    return f"Código:\n{codigo}\n"


def ejercicio9():
    codigo = """
Nombre = input("Nombre Completo: ")
Materia = input("Materia: ")
Cal = float(input("Introduzca calificación: "))

print(f"La calificación ingresada es: {Cal}")

if 95 <= Cal <= 100:
    print(f"La calificación {Cal} es Excelente")
elif 85 <= Cal <= 94:
    print(f"La calificación {Cal} es Muy Buena")
elif 75 <= Cal <= 84:
    print(f"La calificación {Cal} es Buena")
elif 70 <= Cal <= 74:
    print(f"La calificación {Cal} es Suficiente")
else:
    print("N/A")
"""
    return f"Código:\n{codigo}\n"


def ejercicio10():
    codigo = """
num = int(input("Ingrese un número: "))

if num > 0:
    print(f"{num} es positivo")
elif num < 0:
    print(f"{num} es negativo")
else:
    print("El número es cero")
"""
    return f"Código:\n{codigo}\n"


def ejercicio11():
    codigo = """
total_compra = float(input("Ingresa el total de tu compra: "))

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Felicidades! Tienes un descuento del 10%. El total a pagar es: {total_final}")
else:
    print(f"El total a pagar es: {total_compra}")
"""
    return f"Código:\n{codigo}\n"


def ejercicio12():
    return "TICKET"


def ejercicio13():
    return "CICLOS"


def ejercicio14():
    codigo = """
datos_temperatura = {
   10: "Tlaxiaco, Puebla",
   20: "Durango, Chihuahua y Monterrey",
   28: "Veracruz",
   30: "Guerrero",
}

hora = int(input("Ingrese la temperatura: "))

def predecir_temperatura(hora):
    return datos_temperatura.get(hora, "Ciudad no encontrada")

print(f"La ciudad con temperatura de {hora}°C es: {predecir_temperatura(hora)}")
"""
    return f"Código:\n{codigo}\n"


def ejercicio15():
    return "SALIR"


ejercicios = {
    1: ejercicio1, 2: ejercicio2, 3: ejercicio3, 4: ejercicio4, 5: ejercicio5,
    6: ejercicio6, 7: ejercicio7, 8: ejercicio8, 9: ejercicio9, 10: ejercicio10,
    11: ejercicio11, 12: ejercicio12, 13: ejercicio13, 14: ejercicio14, 15: ejercicio15
}


def mostrar_menu():
    while True:
        print("\nMenú de Ejercicios")
        for i in range(1, 16):
            print(f"{i}. Ejercicio {i}")
        print("15. Salir")

        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 15:
                print("Saliendo del programa...")
                break
            elif opcion in ejercicios:
                print(ejercicios[opcion]())
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


if __name__ == "__main__":
    mostrar_menu()
