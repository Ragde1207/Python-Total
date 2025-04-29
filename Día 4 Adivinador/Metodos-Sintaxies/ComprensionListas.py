#La comprension de listas es el manejo dinamico de las mismas

pastel = "Selva Negra"

lista = []

for letra in pastel:
    lista.append(letra)

print(lista)

print("\n--------------------------------------------------------------\n")

lista.clear()

lista = [letra for letra in pastel]
#Se pueden generar los datos de una lista simplemente colocando la "condicion" al momento
#de declarar la lista

print(lista)

print("\n--------------------------------------------------------------\n")

lista.clear()

lista = [letra for letra in "Selva Negra"]
#También funciona con palabras directas y sin necesidad de variables

print(lista)

print("\n--------------------------------------------------------------\n")

lista.clear()

lista = [numero for numero in range(0,16,3)]
#O con numeros

print(lista)

print("\n--------------------------------------------------------------\n")

lista.clear()

lista = [numero for numero in range(0,16,3) if numero * 2 > 15]
#Una ventaja es que se pueden colocar condiciones para el llenado de la lista

print(lista)

print("\n--------------------------------------------------------------\n")

lista.clear()

lista = [numero  if numero * 2 > 15 else "Numero insuficiente" for numero in range(0,16,3)]
#Sin embargo, en caso de querer colocar una condicion else, se debera colocar antes del "for"
#para entender mejor se leería de la siguiente forma:
#Se agregara numero si numero * 2 es mayor que 15, sino, se ingresara "Numero insuficiente" por cada numero en el rango

print(lista)

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [par for par in valores]