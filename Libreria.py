import datetime

nombre = input("NOMBRE: \n")
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\n Nombre del Cliente: {nombre}")
print(f"Fecha y Hora: {fecha}")