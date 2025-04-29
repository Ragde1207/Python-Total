set1 = set([1,2,3,4,5])

print(type(set1))
print(set1)

print("\n--------------------------------------------------------------\n")

#Los sets no permiten la asignación, además, cada uno tiene elementos unicos, en caso de repetirse algun elemento
#este sera eliminado, otra caracteristica es que los sets no tienen orden por lo que no puede realizarse una busqueda
#especifica

set2 = set((6,6,6,6,6,6,6,6,7,8,8,8,9))

print(set2)

#Las listas y diccionarios no son permitidos en los sets, sin embargo, los tuple sí son permitidos

print("\n--------------------------------------------------------------\n")

print(len(set1))
print(len(set2))

print(2 in set1)
print(1 in set2)

set3 = set1.union(set2) #metodo para unir 2 sets

print("\n--------------------------------------------------------------\n")

#Metodo para agregar y eliminar datos a los set

set2.add(10)
print(set2)
set2.remove(10) #también se puede usar el discard, el cual no dara error en caso de que el elemento no exista en el set
print(set2)
#el metodo .pop() elimina un elemento aleatoreo del set
set2.clear()#metodo para vaciar un set
print(set2)
