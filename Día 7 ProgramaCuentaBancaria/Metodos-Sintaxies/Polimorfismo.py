class Vaca:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice muuu")

class Oveja:

    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "dice beee")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

vaca1.hablar()
oveja1.hablar()