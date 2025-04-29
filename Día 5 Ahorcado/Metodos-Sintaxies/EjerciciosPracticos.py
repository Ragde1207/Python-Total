#Ejercicio 1

def devolver_distintos(n,m,nm):
    lista = [n,m,nm]
    suma = n + m + nm

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    elif 10 < suma < 15:
        lista.sort()
        return lista[1]

print(devolver_distintos(1,5,6))

print("\n--------------------------------------------------------------\n")

#Ejercicio 2

def listado(nombre):
    return sorted(set(nombre)) #sorted ordena las letras, mientras que set separa aquellas repetidas

print(listado("Io Ichimonji"))

print("\n--------------------------------------------------------------\n")

#Ejercicio 3

def duple(*args):

    for p in range(len(args) - 1):
        if args[p] == 0 and args[p + 1] == 0:
            return True

    return False

print(duple(2,51,7,8,0,0,51))

print("\n--------------------------------------------------------------\n")

#Ejercicio 4

def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(24))