'''
Los metodos especiales, ayudan a definir el que sucedera en ciertos casos
al momento de llamar a la clase
'''

class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    #Metodo que ayuda a definir el como se manifestara el string de la clase cada que sea llamado
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    #Metodo para definir que sucedera cuando se pida el largo de la clase
    def __len__(self):
        return self.canciones

    #Metodo para definir que sucedera cuando se use el metodo "del" para eliminar un objeto
    def __del__(self):
        print("El objeto se ha eliminado")

mi_cd = CD("Ken Ashcorp", "FullDisc", 26)

print(mi_cd)

#Metodo para eliminar un objeto
#del mi_cd