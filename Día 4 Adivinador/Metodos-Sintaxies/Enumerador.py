#Enumerate permite ingresar simplificar el acceso a datos dentro de ciclos

lista = ["a","b","c"]
indice = 0

#ejemplo de ciclo sin enumerate

for il in lista:
    print(indice,il)
    indice += 1

print("\n--------------------------------------------------------------\n")

#ejemplo de ciclo con enumerate

for indice,il in enumerate(lista):
    print(il)
    print(indice,il) #dependiendo de las variables a imprimir los datos pueden mostrarse de diferentes formas

print("\n--------------------------------------------------------------\n")

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')