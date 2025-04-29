x = 15
y = 3

print(f"Tenemos dos numeros, {x} y {y}")
print(f"La suma de {x} y {y} es igual a {x+y}")
print(f"La resta de {x} y {y} es igual a {x-y}")
print(f"La multiplicacion de {x} y {y} es igual a {x*y}")
print(f"La divicion de {x} y {y} es igual a {x/y}")

print("--------------------------------------------")

z = 5

print(f"Ahora tenemos tres numeros, {x}, {y} y {z}")
print(f"La divicion de {x} y {z} es igual a {x//z}")
print(f"La divicion de {y} y {z} es igual a {y//z}")

print(f"El modulo/sobrante entre {z} y {y} es igual a {z%y}")
print(f"{x} elevado a la {y} potencia es igual a {x**y}")
print(f"{y} elevado a la 3 es igual a {y**3}")
print(f"La raiz cuadrada de {z} es igual a {z**0.5}")

print("----------------------------------------------")

#Redondeo, se utiliza el comando round(parametro1,parametro2)
#Parametro1 = a el numero a redondear, puede ser directamente el numero, operaciones, variables o funciones
#Parametro2 = la cantidad de decimales
#Una variable redondeada solo se volvera int si se redondea dentro de la misma variable

print(90/7)
print(round(90/7,2))

redondeo=90/7

print(round(redondeo))
