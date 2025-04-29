#Frase usada en las pruebas: Rūru wa yaburu tame ni aru

text = input("ingresa un texto a tu elección: ")
original = text

print("\n-----------------------------------------------------------------------\n")

print("Primer analisis - Cantidad de letras")

elecciones = []

elecciones.append(input("Elige una letra: ").lower())
elecciones.append(input("Elige una segunda letra: ").lower())
elecciones.append(input("Elige una tercera letra: ").lower())

text = text.lower()

print("\n")
print("La cantidad de tus letras elegidas en el texto ingresado es:")
print(f"{elecciones[0]} aparece {text.count(elecciones[0])} veces")
print(f"{elecciones[1]} aparece {text.count(elecciones[1])} veces")
print(f"{elecciones[2]} aparece {text.count(elecciones[2])} veces")

print("\n-----------------------------------------------------------------------\n")

print("Segundo analisis - Cantidad de palabras")

listaT = original.split(" ")

print(f"Tu frase tiene {len(listaT)} palabras")
print(listaT)

print("\n-----------------------------------------------------------------------\n")

print("Tercer analisis - Primera y ultima letra")
print(f"La primera letra de tu frase es \"{original[0]}\" y la ultima letra es \"{original[-1]}\"")

print("\n-----------------------------------------------------------------------\n")

print("Cuarto analisis - Tu texto invertido")

listaT.reverse()
invertida = " ".join(listaT)

print(f"Tu frase invirtiendo el orden de las palabras quedaría como: {invertida}")

print("\n-----------------------------------------------------------------------\n")

print("Quinto analisis - Buscando...")
python = 'python' in text
resp = {True:"si",False:"no"}
print(f"La palabra \"Python\" {resp[python]} se encuentra en tu frase")