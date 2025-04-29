#Expresiones regulares, permiten crear patrones para busquedas
import re

#ejemplo de expresion regular, el \d significa digito:
telefono = r'\d\d\d-\d\d\d-\d\d\d\d'
telefono2 = r'\d{3}-\d{3}-\d{4}'

frase = "Polleria Kiara, jimmy fresco todo el año! Pedidos 01800-KFP"

patron = "año"

#re.search("que buscar","donde buscar") metodo para buscar
busqueda = re.search(patron,frase)
print(busqueda)