#Los controladores de flujo son:
# if
# elif
# else
from operator import setitem

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

print("\n--------------------------------------------------------------\n")

#match, match es el Switch de Python
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe el modelo")

print("\n--------------------------------------------------------------\n")

cliente = {'nombre':'Stu',
           'edad':"31",
           'oupación':'Maestro'}

pelicula = {'titulo':'Matrix',
            'ficha':{'protagonista':'Keanu Reeves',
                     'director':'Lana y Lilly Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha': {'protagonista': protagonista,
                        'director': director}}:
            print("Esto es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No sé que es esto")

#match también permite detectar patrones dentro de diccionarios