import bs4
import requests
import lxml


#Variable para almacenar una busqueda usando el metodo requests.get()
resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/buscas-trabajo-y-no-has-certificado-en.html')
#Dicho de otra forma, para almacenar el codigo fuente de la página donde se realizó la busqueda

#Convertimos la busqueda anterior a un formato lxml con el que podemos trabajar de forma más precisa los textos
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#--------------------------------------Extraer un/a titulo/etiqueta especifica------------------------------------------
#".select()" metodo de bs4 (BeautifulSoup4), permite buscar una etiqueta especifica de una busqueda web
print(sopa.select('title'))

print("\n-----------------------------------------------------------------------\n")

#---------------------------------------------Extraccion de clase-------------------------------------------------------
#Ejemplo de busqueda de datos en una clase:
#<div class="post-body entry-content float-container" id="post-body-7716786200824144634">
caja_texto = sopa.select('.page') #Almacenamos todos los datos de la clase page

#Los imprimimos 1 a 1 usando un loop
for p in caja_texto:
    print(p.getText()) #Con .getText() obtenemos cada parrafo con texto sin los "<>" a inicio y final

print("\n-----------------------------------------------------------------------\n")

#--------------------------------------------Extracción de imagen-------------------------------------------------------

imagenes = sopa.select('img')
print(imagenes)

for im in imagenes:
    print(im)

print("\n-----------------------------------------------------------------------\n")

