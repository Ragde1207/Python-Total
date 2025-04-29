#Ejemplo de herencia en multiples clases
class Madre:
    def reir(self):
        print("Jaja")

    def hablar(self):
        print("Qué tal?")

class Padre:
    def hablar(self):
        print("Hola")

#Una misma clase puede heredar de diferentes clases superiores
class Hijo(Padre, Madre): #El orden de la herencia afecta al uso de los metodos heredados
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()

#Ya que el metodo hablar() se heredo desde la clase Hijo, la clase Nieto es capaz de usarlo
nieto.hablar()
#Esto aplica de igual forma con el metodo reir
nieto.reir()