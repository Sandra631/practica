datos_temperatura = {
   10: "Tlaxiaco,Puebla",
   20:"DurangoChihuahua y Monterrey",
   28:"Veracruz",
   30:"Guerrero",
}
hora = int(input("Ingrese temperatura: \n"))
def predecir_temperatura( hora ):
    if hora == 10:
        return datos_temperatura[10]
    elif hora == 20:
        return datos_temperatura[20]
    elif hora == 28:
        return datos_temperatura[28]
    elif hora == 30:
        return datos_temperatura[30]
    else:
        return "Ciudad no encontrada"

print(f"La ciudad con temperatura de {hora} °C es: {predecir_temperatura(hora)}")




