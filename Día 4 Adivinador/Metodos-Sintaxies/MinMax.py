#Minimo y maximo de una cadena de datos
minimo = min(1,2,3,4,5)
maximo = max(1,2,3,4,5)

print(minimo)
print(maximo)

print("\n--------------------------------------------------------------\n")

nombres = ["Alice","Maya","Rin","Rabi","Ena"]

print(min(nombres))
print(max(nombres))

print("\n--------------------------------------------------------------\n")

#Las funciones min y max verifican primero las mayusculas, esto quiere decir
#que inclusi si hay una "a" minuscula, en el caso de haber una o mas letra minuscula
#se realizara la comprobacion con las mayusculas primero

nombreMay = "Rabi"

print(min(nombreMay))

nombreMinu = "rabi"

print(min(nombreMinu))

print("\n--------------------------------------------------------------\n")

#Las funciones min y max utilizan por defecto los indices en el caso de los diccionarios
#por lo que se debe especificar que es lo que se busca

dic = {'a1':10,'a2':6,'a3':76}

print(min(dic))
print(min(dic.values()))