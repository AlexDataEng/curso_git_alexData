from funciones.Bienvenida import Bienvenidas
from funciones.Despedida import Despedida
from decouple import config

#print(config("nombre_secreto"))

bienvenida = Bienvenidas("Mario")

despedida = Despedida("Felipe")

bienvenida.dias()
despedida.chao()
