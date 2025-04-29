'''
    El metodo open() tiene 2 parametros ("nombre del archivo", modo de lectura)
    Modos de lectura:
        * "r" Modo solo lectura, es el modo por defecto y no se necesita especificar al momento de escribir el metodo
            ejemplo: arvhivo = open("Texto.txt")/open("Texto.txt","r")
        * "w" Modo solo escritura, modo en el que, si el archivo ya existe, se vacía el contenido y si no existe lo crea
        * "a" Modo solo escritura al final del archivo, en caso de que no exista el archivo lo crea, y si existe, el
            contenido original se mantiene y lo nuevo es agregado al final
'''

archivo = open("Prueba.txt","w")

#Metodo para escribir en archivos, .write(), este metodo solo escribe una linea de forma normal
#archivo.write("Texto nuevo")
#Para usar el metodo .write() y que escriba varias lineas se haría de la siguiente forma:
#archivo.write('''Texto
#Nuevo''')

'''A diferencia de lo que el metodo pueda parecer, este no escribe varias lineas de texto
    el metodo .writelines() concatena diferentes strings para ingresarlos en 1 misma linea
    en el archivo'''
#archivo.writelines(["Texto"," ","Nuevo"," ","2.0"])

#Para escribir varias lineas usando el metodo .writelines() es más facil usar ciclos:

gatos = ["Oreo","Chimino","Salem","Black"]

for p in gatos:
    archivo.writelines(p + "\n")

archivo.close()