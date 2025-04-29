def generador_perfumeria():
    n = 1
    while True:
        yield f"P-{n}"
        n += 1

def generador_farmacia():
    n = 1
    while True:
        yield f"F-{n}"
        n += 1

def generador_cosmetica():
    n = 1
    while True:
        yield f"C-{n}"
        n += 1

def decorador_turno(funcion_generadora):
    generador = funcion_generadora()

    def decorada():
        nonlocal generador
        turno = next(generador)
        print(f"Su turno es {turno}")
        print("Aguarde y será atendido.")

    return decorada