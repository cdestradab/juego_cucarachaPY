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

# PANTALLA DE BIENVENIDA

bienvenida.mensajeBienvenida()

# CONFIGURACION DE JUEGO
valoresConfig = config.configInicio()

# TABLERO DE PARTIDA

cabecera = tablero.CrearCabecera("LA CUCARACHA", 42)
print(cabecera)

cucaracha = tablero.CrearCucaracha()
cuadroInformativo = tablero.CrearCuadroInformativo(infoTurno, infoJugador, ultimaTirada, 20)

tablero.PrintTablero(cucaracha, cuadroInformativo)

piePagina = tablero.CrearPiePagina("nada", 42)
print(piePagina)

print('---pruebas---')