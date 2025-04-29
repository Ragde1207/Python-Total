#1.- Los strings son inmutables, el siguiente ejemplo da error

#palabraEj = "Kastorice"
#palabraEj[0] = "C"
#print(palabraEj)

#2.- Los strings son concatenables y multiplicables

palabra1 = "Ora"
palabra2 = "Ora"

print(palabra1 + palabra2)
print(palabra1 * 10)

print("\n--------------------------------------------------------------\n")

#3.- Los strings pueden ser multilinea usando """ """

multiLinea = """Si esto se ha impreso
entonces quiere decir
que el codigo funciona"""

print(multiLinea)

print("\n--------------------------------------------------------------\n")

#4.- Se puede verificar si un sub string se encuentra dentro de un string

busqueda = "Las reglas están para romperlas!/Rūru wa yaburu tame ni aru!"

print("reglas" in busqueda)
print("ruru" in busqueda)
print("ruru" not in busqueda)

print("\n--------------------------------------------------------------\n")

#5.- Los strings son calculables

mapache = "Rūru wa yaburu tame ni aru!"

print(len(mapache))

