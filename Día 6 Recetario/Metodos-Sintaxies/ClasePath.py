'''
    Permite manipular rutas de sistemas de archivos representando una ruta a
    un archivo o directorio en el sistema de archivos de la pc.

    Su utilidad se encuentra al momento de crear o mover archivos en el
    sistema de archivos, enumerar los archivos coincidentes con una extension
    o patron determinado y crear rutas basadas en strings
'''

from pathlib import Path

#Path.home() permite obtener la ruta absoluta
base = Path.home()
print(base)

#Path crea objetos en formato de una ruta de acceso, y en caso de tener los archivos o las carpetas pueden utilizarse
guia = Path("Cosas","Archivos")
print(guia)

#.with_name() permite usar una ruta (o parte de la misma) ya establecida alterando el directorio final
guia2 = guia.with_name("Juegos")
print(guia2)

#Se pueden concatenar diferentes objetos Path
completo = Path(base, guia)
print(completo)

#.parent el penultimo directorio de una ruta, al agregar más ".parent"s se recorreran más directorios
print(guia.parent)

