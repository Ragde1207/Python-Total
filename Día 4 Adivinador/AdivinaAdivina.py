from random import *
jugador = input("Ingresa tu nombre... ")

print(f"\nBienvenido, {jugador}!\n"
      f"Este es un pequeño juego de adivinanza\n"
      f"Deberas adivinar el numero que pense\n"
      f"El numero se encuentra entre 1 y 100\n"
      f"Tienes 8 intentos para adivinarlo!\n")

numero = randint(1,100)
intento = 0
adivinado = False

while intento  < 8 and not adivinado:
    opcion = int(input(f"Ingresa tu {intento + 1}° numero: "))

    if opcion > 100:
        print("\nOi! El numero que elegiste es muy grande\n"
              "Te dije entre 1 y 100! 1 y 100~!\n"
              "Vamos, ingresa otro!\n")
    else:
        if opcion > numero:
            print("\nError~!\nElegiste un numero más grande\n")
            intento += 1
        elif opcion < numero:
            print("\nError~!\nElegiste un numero más pequeño\n")
            intento += 1
        else:
            print(f"\nOooh~! Felicidades, {jugador}!\n"
                  f"Adivinaste el numero!\n"
                  f"Y en {intento} intentos\n"
                  f"Eso es todo~, ya puedes irte...")
            break

if not adivinado:
    print("...Buuh~!\n"
          "Bueno, no lo adivinaste...\n"
          "Aunque puedes volver a intentarlo~")