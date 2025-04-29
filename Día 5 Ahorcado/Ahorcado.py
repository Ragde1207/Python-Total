import random

listaPal = ["cuchara","sabana","patata"]
vidas = 5

print("Bienvenido! Vamos a jugar al ahorcado")

def palabra(listap):
    '''Funcion para elegir y generar
        la serie de "_" que indicaran la
        cantidad de palabras'''

    # Elección de palabra
    pr = random.choice(listap) #random.choice() elige aleatoreamente un elemento de una lista
    # Generación de "_" dependiendo de la palabra
    blanco = ["_"] * len(pr)

    return pr,blanco

palE, epaciado = palabra(listaPal)

def estadp(espacios,v):
    '''Funcion para mostrar el estado
        actual del juego, incluye los
        espacios y las vidas restantes'''
    print("\n" + " ".join(espacios))
    print(f"Vidas restantes: {v}")

    return

def intentos(p,espacios, l,v):
    '''Funcion para procesar la letra
        elegida por el jugador'''
    acierto = False
    for i, char in enumerate(p):
        if char == l:
            espacios[i] = l
            acierto = True

    if not acierto:
        v -= 1
        print(f"Fallaste! La letra {l} no está en la palabra~")
    else:
        print(f"Correcto! La letra {l} se agrego a la palabra")

    return espacios, v

def ahorcado():
    '''Funcion principal que maneja
        al resto de funciones y que
        es el juego en sí'''

    #Almacenamiento de la palabra elegida y la cantidad de espacios vacios para el uso de la función
    palabraE, esp = palabra(listaPal)
    vidasR = vidas

    while True:
        estadp(esp, vidasR)

        #Derrota o victoria
        if "_" not in esp: #Se comprueba que no queden "_" en la palabra
            print(f"Felicidades! Ganaste! La palabra es: {palabraE}")
            break
        if vidasR <= 0:
            print(f"Lastima, perdiste~, la palabra era: {palabraE}")
            break

        #Almacenamiento de la letra del jugador
        letra = input("Ingresa una letra: ").lower()

        # .isalpha() verifica que los caracteres de una cadena sean alfabeticos, osea, letras del alfabeto
        if len(letra) != 1 or not letra.isalpha():
            print("Oi! Te dije una letra!")
            continue

        #Modigicación de las vidas y espacios con ayuda de la función intentos
        esp, vidasR = intentos(palabraE, esp, letra, vidasR)

ahorcado()