from funciones.Bienvenida import Bienvenidas
from decouple import config

#print(config("nombre_secreto"))

bienvenida = Bienvenidas("Alejandro")

bienvenida.dias()