import os
import shutil
import send2trash


#getcwd() obtiene ruta actual
print(os.getcwd())

#shutil.move("nombre archivo","nueva direccion"), como su sintaxis indica, es un metodo para mover archivos
shutil.move("Moviendo.txt","C:\\Users\\ragde\\OneDrive\\Escritorio")

'''
os.unlink("",""): metodo para borrar un archivo en una ruta especifica
os.rmdir("",""): borrar una carpeta vacia en una ruta especifica
shutil.rmtree(): elimina TODO lo que este en una ruta

send2trash permite borrar un archivo enviandolo a la papelera de reciclaje
send2trash.send2trash("Moviendo.txt")
'''

ruta = "C:\\Users\\ragde\\OneDrive\\Escritorio"

#os.walk() recorre un directorio especificado y devuelve los nombres de carpetas, subcarpetas y archivos
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {ruta}')
    print(f'Las subcarpetas son:')

    for sub in subcarpeta:
        print(f'\t{sub}')

    print(f'Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')
