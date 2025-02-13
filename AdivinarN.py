import random

NumA = random.randint(1, 10)
adivina = int(input("Adivina el numero ente 1 y 10: \n"))

print(f"El numero aleatorio es: {NumA}.")
if adivina == NumA:
    print("Correcto has adivinado el numero.")
else:
    print(f"Incorrecto, el numero era: {NumA}.")