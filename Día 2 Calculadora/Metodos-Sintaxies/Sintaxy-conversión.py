# type() = permite saber el tipo de dato de una variable

num1 = 7
num2 = 2.5
print(num1)
print(num2)
print(num1 + num2)
print(type(num1 + num2))

#Existen 2 tipos de convercion, Explícita e Implícita
#Implicita: Python genera la convercion de forma automatica en algunos procesos
#Explícita: Es generada por el developer mediante codigo

num3 = int(num2)
print(num3)
print(type(num3))

#Para imprimir una cadena de texto sin alterar el valor de las variables
#se utiliza format

print("Hay demasiados numeros, {} es entero, {} es flotante y {} es la suma de ambos".format(num1,num2,num1+num2))

#Tambien se pueden usar las cadenas literales

print(f"Hay demasiados numeros, {num1} es entero, {num2} es flotante y {num3} fue converdio a entero")