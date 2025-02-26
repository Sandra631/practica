datos_temperatura= {
    "mañana": 20,
    "tarde": 25,
    "noche":18
}

def predecir_temperatura(hora):
    if hora == "mañana":
        return datos_temperatura["mañana"]
    elif hora == "tarde":
        return datos_temperatura["tarde"]
    elif hora== "noche":
        return datos_temperatura["noche"]
    else:
        return "Hora no valida"
    
    hora = "tarde"
    print(f"La temperatura promedio en la {hora} es: {predecir_temperatura(hora)}°C")