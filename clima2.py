# Diccionario con las temperaturas según la parte del día
datos_temperatura = {
    "mañana": 20,
    "tarde": 25,
    "noche": 18,
    "madrugada": 12
}

# Función para predecir la temperatura según la parte del día
def predecir_temperatura(hora):
    return datos_temperatura.get(hora.lower(), "Hora no válida")

# Preguntar al usuario
hora = input("¿En qué parte del día estás? (mañana, tarde, noche, madrugada): ").strip().lower()

# Mostrar la temperatura
temperatura = predecir_temperatura(hora)
if temperatura == "Hora no válida":
    print("Por favor, ingresa una opción válida: mañana, tarde, noche o madrugada.")
else:
    print(f"La temperatura promedio en la {hora} es: {temperatura}°C")

