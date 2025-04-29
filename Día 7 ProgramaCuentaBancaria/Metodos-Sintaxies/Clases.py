#Sintaxis de las clases en python:
'''
#Nota, el nombre de las clases se inicia en mayuscula

class "NombreClase":
    #En caso de crear la clase para tener una idea general del codigo, se coloca "pass" para evitar errores
    pass

Existen 2 tipos de atributos:
    * Atributos de clase: atributos que pertenecen a la clase y son compartidos con sus instancias
    * Atributos de instancia: atributos exclusivos de cada instancia

    #Sintaxis de un atributo
    def __init__(self,color#Parametro):
        self.color#Nombre de atributo = color

'''

class Pollos:

    #Ejemplo de atributo de clase
    alas = True
    #Metodo constructor que asigna atributos a la clase
    def __init__(self,color):
        self.color = color

    pass

#Ejemplo de instancia
mi_gallo = Pollos("cafe")
                    #Dentro de los parentesis van los parametros
mi_gallina = Pollos("blanco")

print(mi_gallo)
print(type(mi_gallo))
print(Pollos.alas)
print(mi_gallo.alas)

