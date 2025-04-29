from random import shuffle

palitos = ["-","--","---","----"]

def mezclar(lista):

    #Funcion para mezclar la lista que se ingrese

    shuffle(lista)
    return lista

def eleccion():

    #Funcion para elegir de la lista mezclada una opcion

    opcion = ""

    while opcion not in ["1","2","3","4"]:
        opcion = input("Dije un numero del 1 al 4...")

    return int(opcion)

def comprobar_intento(lista,intento):

    #En caso de salir o no el palito más corto mandara un mensaje dependiendo del resultado

    if lista[intento - 1] == "-":
        print("Perdiste~")
    else:
        print("Hey, te salvaste")

    print(f"Te toco el palito {lista[intento - 1]}")


palitos_mezclados = mezclar(palitos) #Variable para almacenar la lista mezclada
seleccion = eleccion() #Variable para almacenar la eleccion del usuario
comprobar_intento(palitos_mezclados,seleccion) #Llamado de la funcion para imprimir el resultado