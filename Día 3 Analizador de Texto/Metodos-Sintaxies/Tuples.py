#Similares a las listas, sin embargo, son inmutables

tuplita = (1,2,3,4,1)

print(type(tuplita))
print(tuplita)
print(tuplita[2])
print(tuplita.count(1)) #metodo para contar la cantidad de veces que un dato se encuentra en un tuple
print(tuplita.index(4)) #metodo para mostrar el numero de indice de un dato

listita = list(tuplita) #metodo de convercion de tuple a lista