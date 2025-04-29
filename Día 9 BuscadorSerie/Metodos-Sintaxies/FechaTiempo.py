'''
manejo separado de fecha y hora
import datetime

#datetime.time: manejo de horas
mi_hora = datetime.time(17,35,12)
#datetime.date: manejo de fechas
mi_fecha = datetime.date(2025,7,12)
'''

'''
from datetime import datetime

#Al importar datetime de datetime no se necesita especificar que tipo de dato es (fecha/hora)
mi_fecha = datetime(2025,4,10,18,14,52)
print(mi_fecha)

#Para remplazar o actualizar un dato se usa el metodo .replace()
mi_fecha = mi_fecha.replace(minute=15,second=00)
print(mi_fecha)

despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)

#Resta que dara los segundos entre 2 fechas
vigilia = duerme - despierta

print(vigilia)
'''

'''
from datetime import date

nacimiento = date(1999,7,12)
defuncion = date(2040,4,2)

#Resta que dara los días entre 2 fechas
vida = defuncion - nacimiento

print(vida)
'''

