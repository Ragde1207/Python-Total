texto = "Estos son ejemplos de los metodos string"

print(texto)

print("\n-----------------------------------------------------------------------\n")

#1.- Metodo para convertir todos los caracteres de un string en mayusculas, upper

print(f"Nuestro texto de ejemplo tras usar el metodo upper: {texto.upper()}")

print("\n-----------------------------------------------------------------------\n")

#2.- Metodo para convertir todos los caracteres de un string en minusculas, lower

print(f"Nuestro texto de ejemplo tras usar el metodo lower: {texto.lower()}")

print("\n-----------------------------------------------------------------------\n")

#3.- Metodo para separar los string en listas, split

print(f"Nuestro texto de ejemplo tras usar el metodo split: {texto.split()}\n")


#4.- Metodo para fragmentar/cortar los string y almacenar su contenido en una lista, split

print(f"Nuestro texto de ejemplo tras usar el metodo split especificado: {texto.split()}")
#colocar un caracter dentro de los "()"
# de split, permite seleccionar el limite de los separadores
print(f"Nuestro texto de ejemplo tras usar el metodo split especificado: {texto.split("t")}")

print("\n-----------------------------------------------------------------------\n")

#5.- Metodo para unir diferentes string, join

a = "Nuevo"
b = "texto"
c = "de"
d = "ejemplo"
e = " ".join([a,b,c,d]) #los elementos que el metodo join() unira deben ser de una lista

print(f"Nuestro texto de ejemplo tras usar el metodo join: {e}")

print("\n-----------------------------------------------------------------------\n")

#6.- Metodo de busqueda, find

print(f"Nuestro texto de ejemplo tras usar el metodo find: {texto.find("E")}")

print("\n-----------------------------------------------------------------------\n")

#7.- Metodo para remplazar textos, replace
# Este metodo necesita parametros, el texto a eliminar y el texto a ingresar como remplazo

print(f"Nuestro texto de ejemplo tras usar el metodo replace: {texto.replace("son","son los")}")
print(f"Nuestro texto de ejemplo tras usar el metodo replace: {texto.replace("s","x")}")
