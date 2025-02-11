Nombre = input("Nombre Completo: \n")
Materia = input("Materia: \n")
Cal = float(input("Introdusca calificacion: \n"))

print(f"La Calificacion ingresada es: {Cal} \n y")

if Cal >= 95 and Cal <= 100:
    print(f"La calificacio {Cal} es Excelente")
elif Cal >= 85 and Cal <= 94:
    print(f"La calificacio {Cal} es Muy Buena")
elif Cal >= 75 and Cal <= 84:
    print(f"La calificacio {Cal} es Buena")
elif Cal >= 70 and Cal <= 74:
    print(f"La calificacio {Cal} es Suficiente")
else:
    print("N/A")
