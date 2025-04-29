#Ejemplo de herencia
class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

    def hablar(self):
        print("Este animal emite sonido")

    pass

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        #En caso de tener atributos heredados, se puden redefinir con el metodo: super().__init__
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    #Si al heredar un metodo, se crea otro del mismo nombre, el propio se superpone al heredado
    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")

    pass

mi_gallo = Pajaro(2,"cafe")

print(mi_gallo.color)