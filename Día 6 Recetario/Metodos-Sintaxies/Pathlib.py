from pathlib import Path, PureWindowsPath

#Gracias a Path no es necesario abrir y cerrar archivos
carpeta = Path("/Día 6 Recetario/Metodos-Sintaxies/Prueba.txt")

#PureWindowsPath transforma cualquier ruta en una ruta de Windows
rutaPura = PureWindowsPath(carpeta)

#El metodo .read_text() permite leer el contenido del archivo especificado
print(carpeta.read_text())
#.name devuelve el nombre del archivo
print(carpeta.name)
#.suffix devuelve el tipo de archivo del mismo
print(carpeta.suffix)
#.stem devuelve el nombre sin la terminacion (.txt por ejemplo)
print(carpeta.stem)

#.exist devuelve True o False dependiendo de la condición
if not carpeta.exists():
    print("Este archiivo no existe")
else:
    print("Archivo encontrado")

