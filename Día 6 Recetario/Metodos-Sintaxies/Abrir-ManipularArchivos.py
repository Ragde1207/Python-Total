'''Los metodos para manipular archivos en
    la pc son:
        * open()
        * read()
        * write()
        * close()
    '''

#Para utilizar un archivo se debe almacenar en una variable
archivo = open('Prueba.txt')
#linea = archivo.readline()
todas = archivo.readlines()

#Lee el contenido de todo el archivo
#print(archivo.read())
#readline() lee la primera linea del archivo
'''print(linea.upper()) #Si el archivo es completamente texto se pueden utilizar los metodos que funcionan en strings

linea = archivo.readline()
print(linea)

linea = archivo.readline()
print(linea)'''
#Al repetir varias veces el metodo .readline() se avanza linea por linea del archivo

print("\n-----------------------------------------------------------------------\n")

#También podemos utilizar los archivos para ciclos
'''for l in archivo:
    print("La linea es: " + l)'''

print("\n-----------------------------------------------------------------------\n")

#El metodo readlines transforma el contenido en una lista, por lo que se pueden utilizar los metodos respectivos
print(todas)

#Es recomendable cerrar el archivo siempre para guardar espacio de memeoria
archivo.close()
