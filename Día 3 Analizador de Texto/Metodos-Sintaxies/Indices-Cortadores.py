#1.- Conocer el índice de un caracter, ejemplos de uso de index
print("Prueba de Index usando el nombre de mi gata, Oreo")

texto = "Oreo"
print(f"La letra \"e\" se encuentra en la posición numero {texto.index("e")}")

poscion = texto[3]

print(f"Y la 4° letra es {poscion}")

print("\n--------------------------------------------------------------\n")

#2.- Almacenar fragmentos de cadenas de texto

textoFrag = "Oreo es una gata color galleta."

print(textoFrag)

print(textoFrag[:16])
print(textoFrag[17:])
print(textoFrag[::3])
print(textoFrag[::-1])