lista = ["Tipos", "y", "caracteristicas", "de las", "listas"]

print(type(lista))

lista1 = [1,2,3,4]
lista2 = ["a","b","c","d"]

print(lista1)
print(lista2)
print(lista1 + lista2)

print("\n--------------------------------------------------------------\n")

#para agregar un nuevo elemento a una lista se utiliza el metodo append

lista1.append(5)

print(lista1)

#para eliminar elementos de una lista se utiliza el metodo pop

lista1.pop()
lista2.pop(3)

print(lista1)
print(lista2)

print("\n--------------------------------------------------------------\n")

#metodo para ordenar listas, sort y reverse

desordenN = [5,1,3,2,4]
desordenC = ["b","c","d","a"]

print(desordenN)
print(desordenC)
print("Tras usar el metodos sort:")
desordenN.sort()
print(desordenN)

print("Tras usar el metodos reverse:")
desordenC.reverse()
print(desordenC)

#para contar la cantidad de datos en una lista se usa el metodo len()

largo = len(desordenC)
print(largo)

print("\n--------------------------------------------------------------\n")

