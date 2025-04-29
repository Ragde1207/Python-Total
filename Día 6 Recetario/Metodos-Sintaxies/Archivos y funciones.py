#Ejercicios de Curso, Rutas con Funciones

#Ejempo de funcion para leer archivo
def abrir_leer(archivo):
    archivo = open("ejemplo.txt","r")
    contenido = archivo.read()
    return contenido

#Ejemplo de funcion para reescribir archivo
def sobrescribir(archivo):
    archivo = open("ejemplo.txt", "w")

    return archivo.write("contenido eliminado")
    # TODO: write code...

#Ejemplo de funcion para registrar datos al final del archivo
def registro_error(archivo):
    archivo = open("log_errores.txt","a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    # TODO: write code...

