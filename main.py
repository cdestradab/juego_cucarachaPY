import sys

sys.path.append('/control/')
sys.path.append('/modelo/')
sys.path.append('/vista/')

import libreria as lib
from vista import vista_tablero as tablero
from vista import vista_bienvenida as bienvenida
from vista import vista_inicio as config

#bienvenida.mensajeBienvenida()

#valoresConfig = config.configInicio()

cabecera1 = tablero.crearCabecera("LA CUCARACHA", 40)
print(cabecera1)


cucaracha = tablero.crearTablero()
tablero.impTablero(cucaracha)