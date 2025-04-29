#Ejemplo de decorador
def decorar_saludo(funcion):#El parametro a recibir es la funcion a decorar

    def otra_funcion(palabra):#Palabra es el contenido a afectar con la funcion
        print("Hola")
        funcion(palabra)
        print("Adios")

    return otra_funcion

#En caso de que no sea necesesario modificar cuando activar o no un decorador se utiliaza:
@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayuscula("Python")

#Para condicionar el decorador y usarlo cada que queramos, podemos crear una variable que contenga el decorador
minuscula_decorada = decorar_saludo(minusculas)

minuscula_decorada("PytHon")