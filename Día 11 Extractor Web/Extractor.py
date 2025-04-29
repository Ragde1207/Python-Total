import bs4
import requests

''' Notas y ejemplos tomados durante la clase del curso
resultados = requests.get(urlBase.format('1'))
sopa = bs4.BeautifulSoup(resultados.text, 'lxml')

libros = sopa.select('.product_pod')

#Formas de conseguir el rango de estrellas y el titulo del libro:
ejemplo = libros[0].select('.star-rating.Three')
ejemploT = libros[0].select('a')[1]['title']
#Los espaciós vacios en los nombres de las clases se remplazan con un "."
print(ejemplo)
'''

#Variable para navegar entre páginas del cátalogo de libros:
urlBase = 'https://books.toscrape.com/catalogue/page-{}.html'

#Lista de libros con ratio de 4 o 5 estrellas:
titulosRatingAlto = []

#iterar paginas:
for paginaN in range(1, 51):

    #creacion de sopa de cada pagina:
    urlPagina = urlBase.format(paginaN)
    resultado = requests.get(urlPagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #Seleccion de libros:
    libros = sopa.select('.product_pod')

    #iterar libros:
    for libro in libros:

        #Comprobacion de ratio:
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            #Almacenado de título en una variable:
            tituloL = libro.select('a')[1]['title']

            #Agregado del titulo a la lista:
            titulosRatingAlto.append(tituloL)

#Visualizacion de lista:
for t in titulosRatingAlto:
    print(t)