import os
import re
from datetime import datetime
import time
from pathlib import Path
import math

'''Codigo que se uso para descomprimir el .zip con las instrucciones de este proyecto
import shutil
shutil.unpack_archive('Proyecto Dia 9.zip','D:\\Python\\BuscadorSerie','zip')
'''

inicio = time.time()

ruta = "D:\\Python\\BuscadorSerie\\Mi_Gran_Directorio"
patron = r'N\D{3}-\d{5}'
hoy = datetime.now()
nencontrados = []
archivos_encontrados = []

def buscar_num(archivo, pat):
    #Funcion para buscar el patron en los archivos
    este_archivo = open(archivo,'r') #open() se utiliza para abrir el archivo actual en la busqueda
    texto = este_archivo.read() #.read(), su nombre se explica solo
    #If que comprueba si el patron se encuentra en el texto del archivo
    if re.search(pat,texto):
        #En caso de encontrarse el patron, se devuelve la busqueda
        return re.search(pat,texto)
    else:
        return ''

def crealistas():
    #Funcion que ingresa los datos (nombre del archivo y su numero de serie) en listas
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_num(Path(carpeta, a),patron)
            if resultado != '':
                nencontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

def muestra():

    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{nencontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Número encontrados: {len(nencontrados)}')

    fin = time.time()
    total = fin - inicio

    print(f'Duracion de busqueda: {math.ceil(total)} segundos')
    print('-' * 50)

crealistas()
muestra()