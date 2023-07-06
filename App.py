from funciones.Bienvenida import Bienvenidas
from funciones.Despedida import Despedida
from funciones.Consulta import Consulta
#from decouple import config

#print(config("nombre_secreto"))

bienvenida = Bienvenidas("Mario")

despedida = Despedida("Felipe")

consulta = Consulta("Alex")

bienvenida.dias()
despedida.chao()
consulta.ordenar()
