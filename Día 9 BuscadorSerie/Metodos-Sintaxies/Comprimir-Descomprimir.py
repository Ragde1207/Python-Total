import zipfile

mi_zip = zipfile.ZipFile("Mi_zip.zip","w")

mi_zip.write("Moviendo.txt")

mi_zip.close()

zip_abierto = zipfile.ZipFile("Mi_zip.zip","r")
zip_abierto.extractall()

'''
import shutil
carpeta_origen = ("C:\\Users\\ragde\\OneDrive\\Escritorio")

archivo_destino = "Todo_comprimido"

#Forma de comprimir con shutil, ("nombre del archivo","tipo del archivo","ruta de archivos")
shutil.make_archive(archivo_destino,"zip",carpeta_origen)
#Forma de descomprimir con shutil
shutil.unpack_archive(archivo_zip, nombre_carpeta_extraccion,"zip")
'''