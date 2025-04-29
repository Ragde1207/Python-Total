#Zip combina dos o más listas entrelazando los elementos en tuples

nombre = ["Oreo","Salem","Chimino"]
edad = [6,4,7]

combinados = list(zip(nombre,edad))

print(combinados)
#Zip mantiene el tamñao de la lista más corta de la combinación

for gato,anios in combinados:
    print(f"{gato} lleva {anios} viviendo conmigo, cómo pasa el tiempo")