'''
Existen 3 tipos de metodos para las clases, estos son:
    * Metodos de instancia
    * Metodos de clase: se crean usando el decorador @classmethod
    * Metodos estaticos: se crean usando el decorador @staticmethod
'''

class Pollos:

    #Ejemplo de atributo de clase
    alas = True
    #Metodo constructor que asigna atributos a la clase
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    #Ejemplos de metodos de instancia en una clase:
    def piar(self):
        print("Pio, mi color es {}".format(self.color))

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es de color {self.color}")

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    #Ejemplo de metodo de clase
    @classmethod
    def puesta(cls,cantidad):
        print(f"Puso {cantidad} huevos")

    #Ejemplo de metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira y te juzga...")

    pass

mi_gallo = Pollos("cafe","gallo")

mi_gallo.piar()