def cheq(lista):

    listad3 = []

    for n in lista:
        if n in range(100,1000):
            listad3.append(n)
        else:
            pass

    return listad3

resultado = cheq([533,71,101])

print(resultado)

print("\n--------------------------------------------------------------\n")

#Ejemplo de funcion con taples

precios_cafe= [("Capuchino",1.5),("Expresso",4),("Moka",1.9)]

def cafe_caro(lista_precios):

    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro,precio_mayor)

cafe, precio = cafe_caro(precios_cafe)

print(f"El café más caro es {cafe}, con un precio de {precio}")