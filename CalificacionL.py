cal = int(input("Ingresa Calificacion (0 - 100): \n"))

if 90 <= cal <= 100:
    print("Tu Calificacion es: 'A'")
elif 80 <= cal < 90:
    print("Tu Calificacion es: 'B'")
elif 70 <= cal < 80:
    print("Tu Calificacion es: 'C'")
elif 60 <= cal < 70:
    print("Tu Calificacion es: 'D'")
else:
    print("Tu Calificacion es: 'F'")