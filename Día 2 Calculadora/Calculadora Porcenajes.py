nombre = input("Ingrese nombre de vendedor: ")
print(f"Bienvenido {nombre}")
venta = input(f"Ingresa tus venta del mes, {nombre}: ")

comisión = (int(venta) * 13)/100

print(f"{nombre}, tu comisión de este mes es: {round(comisión,2)}\n"
      f"Mucha suerte este mes!")
