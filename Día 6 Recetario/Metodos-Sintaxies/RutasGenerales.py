#Para crear rutas que cualquier sistema operativo pueda entender, se utiliza el metodo path
from pathlib import Path

#Gracias a "Path" podemos eliminar el disco (D:,C:,etc.) de la ruta
carpeta = Path("/Día 6 Recetario/Metodos-Sintaxies")

            #El "/" permite concatenar con los siguientes caracteres
archivo = carpeta / "Prueba.txt"
#Forma de abrir el archivo con la ruta general
mi_archivo = open(archivo)

print(mi_archivo.read())

