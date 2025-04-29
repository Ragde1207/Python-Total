#sintaxis de los diccionarios: "nombre de variable" = {'x':'y','x':'y','x':'y'}

diccionario = {'e1':'valor1','e2':'valor2', 'e3':'valor3'}
print(type(diccionario))
print(diccionario)

busqueda = diccionario['e1']
print(busqueda)

print("\n--------------------------------------------------------------\n")

gatos = {'Oreo':'Negro, hembra','Chimino':'Crema, macho','Milanesa':'Crema, hembra'}
consulta = (gatos['Milanesa'])

print(consulta)

print("\n--------------------------------------------------------------\n")

#ejemplo de diccionario con lista y diccionario

diccionario2 = {'v1':2,'v2':['a','b','c','d'],'v3':{'v1.1':2.1,'v2.1':'lista2','v3.1':'diccionario2'}}

print(diccionario2['v2'][3])
print(diccionario2['v3']['v1.1'])
print(diccionario2['v2'][2].upper())

#agregado y sobreescritura de elementos

diccionario2['v4'] = True

print(diccionario2)

diccionario2['v4'] = False

print(diccionario2)

print("\n--------------------------------------------------------------\n")

#revisión de claves y valores

print(diccionario2.keys())
print(diccionario2.values())
print(diccionario2.items())