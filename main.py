import sys

sys.path.append('/control/')
sys.path.append('/modelo/')
sys.path.append('/vista/')

import libreria as lib
from vista import vista_tablero as tablero
from vista import vista_bienvenida as bienvenida
from vista import vista_inicio as config

infoConfig = {'monto': 0, 'penalizacion': 0, 'jugadores': 0}
infoTurno = {'turno': 0, 'jugador': 0, 'tirada':0}
infoJugador = {'id': 0, 'montoActual':0, 'puntaje':[0,0,0]}
ultimaTirada = [0,0,0,0,0]

cuadroInformativo = tablero.crearCuadroInformativo(infoTurno, infoJugador, ultimaTirada, 20)

#bienvenida.mensajeBienvenida()

#valoresConfig = config.configInicio()

cabecera1 = tablero.crearCabecera("LA CUCARACHA", 42)
print(cabecera1)


cucaracha = tablero.crearCucaracha()
tablero.impTablero(cucaracha, cuadroInformativo)

print('---pruebas---')

lib.impMatriz(cuadroInformativo)