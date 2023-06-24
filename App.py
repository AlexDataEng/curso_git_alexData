from funciones.Bienvenida import Bienvenidas
from funciones.Despedida import Despedida
from decouple import config

#print(config("nombre_secreto"))

bienvenida = Bienvenidas("Alejandro")

despedida = Despedida("Mirla")

bienvenida.dias()
despedida.chao()