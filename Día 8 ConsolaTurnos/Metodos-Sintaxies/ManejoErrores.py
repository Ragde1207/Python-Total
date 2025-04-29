'''
Los 3 metodos para el maenejo de erores son:
* try: se intentara el codigo especificado
* except: si existe algun error se ejecutara x accion/bloque de codigo
* finally: incluso si hay algun error se ejecutara el codigo
'''

def suma():
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa otro numero: "))
    print(n1 + n2)
    print("Suma realizada")


try: #Obligatorio en la prueba de errores
    suma()
#except: Obligatorio en la prueba de erores
#    print("Error")
except TypeError:
    print("Error de concatenacion")
except ValueError:
    print("Ese no es un numero...")
#opcional
else:
    print("Codigo ejecutado sin errores")
# opcional
finally:
    print("\nGracias por tu tiempo")


