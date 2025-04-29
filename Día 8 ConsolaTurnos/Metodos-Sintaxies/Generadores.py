#Ejemplo de funcion normal
def funcion():
    lista = []

    for x in range(1,5):
        lista.append(x * 10)
    return lista

#Ejemplo de la funcion anterior como generador
def generador():

    for x in range(1,5):
        yield x * 10

g = generador()

#para imprimir los datos de un generador se utiliza el metodo next()
print(next(g))
print("Los generadores mantienen su posición/dato")
print(next(g))
print("Incluso si no se utiliza de manera continua")
print(next(g))
