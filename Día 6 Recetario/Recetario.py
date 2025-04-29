import os
from pathlib import *

print("Bienvenido, usuario!\n")

rutaRecetario = Path("/Día 6 Recetario/Metodos-Sintaxies/Recetas")
cats = [categoria.name for categoria in rutaRecetario.iterdir() if categoria.is_dir()]


print(f"La ruta del diccionario es: {rutaRecetario}")

def limpiador():

    #Funcion para limpiar la pantalla cada vez que se reinicie el programa
    os.system('cls' if os.name == 'nt' else 'clear')

    return

def mostrar_menu():

    limpiador()
    print("Bien bien, todo limpio, empecemos de nuevo")
    print(f"Ubicación de recetas: {rutaRecetario}")
    print(f"Total de recetas: {contar_recetas()}\n")

    return

def contar_recetas():

    #Funcion para contar todas las recetas en todas las categorías
    return sum(1 for categoria in cats for _ in (rutaRecetario / categoria).glob('*.txt'))

def mostrar_cats():

    #Funcion para desglozar las categorias del recetario
    print("\nCategorías disponibles:")
    for i, categoria in enumerate(cats, 1):
        print(f"{i}. {categoria}")
    return cats

def seleccionar_cats():

    #Funcion de seleccion de categorias
    categorias = mostrar_cats()
    while True:
        try:
            opcion = int(input("\nSeleccione una categoría (número): ")) - 1
            if 0 <= opcion < len(categorias):
                return categorias[opcion]
            print("Opción inválida, intenta nuevamente")
        #En caso de que el dato ingresado no sea un numero mandara error
        except ValueError:
            print("Por favor ingresa un número")


def listar_recetas(categoria):

    #Funcion para mostrar el listado de las recetas
    ruta_categoria = rutaRecetario / categoria
    recetas = [receta.stem for receta in ruta_categoria.glob('*.txt')]

    if not recetas:
        print(f"\nNo hay recetas en la categoría '{categoria}'")
        return None

    print(f"\nRecetas en '{categoria}': ")
    for i, receta in enumerate(recetas, 1):
        print(f"{i}. {receta}")
    return recetas


def seleccionar_receta(categoria):

    #Funcion para que al usuario seleccionar una receta de la categoria elegida
    recetas = listar_recetas(categoria)
    if not recetas:
        return None

    while True:
        try:
            opcion = int(input("\nSeleccione una receta (número): ")) - 1
            if 0 <= opcion < len(recetas):
                return recetas[opcion]
            print("Opción inválida, intente nuevamente")
        #Mismo caso que en seleccionar_cats
        except ValueError:
            print("Por favor ingresa un número.")


def imprect(categoria, receta):

    #Funcion para imprimir el contenido de una receta
    ruta_receta = rutaRecetario / categoria / f"{receta}.txt"
    print(f"\nReceta: {receta}\n")
    print(ruta_receta.read_text(encoding='utf-8'))


def crear_receta(categoria):

    #Funcion para crear un nuevo archivo .txt (receta)
    nombre = input("\nIngresa el nombre de la nueva receta: ").strip()
    contenido = input("Escribe el contenido de la receta: ")
    ruta_receta = rutaRecetario / categoria / f"{nombre}.txt"

    ruta_receta.write_text(contenido, encoding='utf-8')
    print(f"\nReceta '{nombre}' creada exitosamente")


def eliminar_receta(categoria, receta):

    #Funcion para eliminar una receta
    ruta_receta = rutaRecetario / categoria / f"{receta}.txt"
    ruta_receta.unlink()
    print(f"\nReceta '{receta}' eliminada exitosamente")


def crear_categoria():

    #Funcion para crear una nueva carpeta (categoria de recetas)
    nuevacat = input("\nIngrese el nombre de la nueva categoría: ").strip()
    nueva_categoria = rutaRecetario / nuevacat
    nueva_categoria.mkdir(exist_ok=True)
    cats.append(nuevacat)
    print(f"\nCategoría '{nuevacat}' creada exitosamente")


def eliminar_categoria():

    #Funcion para eliminar una carpeta
    categoria = seleccionar_cats()
    ruta_categoria = rutaRecetario / categoria

    if any(ruta_categoria.iterdir()):
        print(f"\nNo se puede eliminar la categoría '{categoria}', contiene recetas")
        return

    ruta_categoria.rmdir()
    cats.remove(categoria)
    print(f"\nCategoría '{categoria}' eliminada exitosamente")


def menu_principal():
    """Muestra el menú principal y maneja las opciones"""
    while True:
        mostrar_menu()
        print("Opciones:")
        print("1. Leer receta")
        print("2. Crear receta")
        print("3. Crear categoría")
        print("4. Eliminar receta")
        print("5. Eliminar categoría")
        print("6. Salir")

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            categoria = seleccionar_cats()
            receta = seleccionar_receta(categoria)
            if receta:
                imprect(categoria, receta)
        elif opcion == "2":
            categoria = seleccionar_cats()
            crear_receta(categoria)
        elif opcion == "3":
            crear_categoria()
        elif opcion == "4":
            categoria = seleccionar_cats()
            receta = seleccionar_receta(categoria)
            if receta:
                eliminar_receta(categoria, receta)
        elif opcion == "5":
            eliminar_categoria()
        elif opcion == "6":
            print("\nHasta luego!")
            break
        else:
            print("\nOpción inválida, intente nuevamente")

        input("\nPresione Enter para continuar...")

menu_principal()