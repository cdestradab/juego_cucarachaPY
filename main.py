import sys

sys.path.append('/control/')
sys.path.append('/modelo/')
sys.path.append('/vista/')

import libreria as lib
from vista import vista_tablero as tablero
from vista import vista_bienvenida as bienvenida
from vista import vista_inicio as config
from control import control_partida as partida

infoConfig = {'monto': 0, 'penalizacion': 0, 'jugadores': 0}
infoTurno = {'turno': 0, 'jugador': 0, 'tirada':0}
#infoJugador = {'id': 0, 'montoActual':0, 'puntaje':[0,0,0]}
ultimaTirada = [0,0,0,0,0]

# PANTALLA DE BIENVENIDA

'''bienvenida.mensajeBienvenida()'''

# CONFIGURACION DE JUEGO
'''valoresConfig = config.configInicio()
infoConfig['jugadores'] = valoresConfig[0]
infoConfig['monto'] = valoresConfig[1]
infoConfig['penalizacion'] = valoresConfig[2]'''

##----PRUEBA----
infoConfig['jugadores'] = 2
infoConfig['monto'] = 100000
infoConfig['penalizacion'] = 2000
##----PRUEBA----

# GENERAR PERFIL DE JUGADORES

perfiles = partida.GenerarPerfiles(infoConfig['jugadores'], infoConfig['monto'])
  
# GENERAR TABLERO DE PARTIDA INICIAL

cabecera = tablero.CrearCabecera("LA CUCARACHA", 42)
cucaracha = tablero.CrearCucaracha()
cuadroInformativo = tablero.CrearCuadroInformativo(infoTurno, perfiles[0], ultimaTirada, 20)
piePagina = tablero.CrearPiePagina("¡Comienza la partida!", "", 42)
  
# GENERAR ALGORITMO DE TURNOS

juegoContinua = True

while juegoContinua:
  infoTurno['turno'] += 1
  
  for jugador in perfiles:
    #Actualizar cuadro informativo
    cuadroInformativo = tablero.CrearCuadroInformativo(infoTurno, jugador, ultimaTirada, 20)
    #Imprimir tablero
    tablero.PrintIU(cabecera, cucaracha, cuadroInformativo, piePagina)
    #Elegir si pasar o tirar los dados.
    print('/n')

    turnoContinua = True
    while turnoContinua:
      pasaOTira = partida.PasarOTirar()
      if pasaOTira == "t":
        ultimaTirada = lib.TirarDados(6, 5)

        cuadroInformativo = tablero.CrearCuadroInformativo(infoTurno, jugador, ultimaTirada, 20)
        tablero.PrintIU(cabecera, cucaracha, cuadroInformativo, piePagina)
      elif pasaOTira == "p":
        turnoContinua = False
        
    break
    
  juegoContinua = False
  
print('---pruebas---')

# LO SIGUIENTE SERA PROGRAMAR EL ALGORITMO QUE EVALUA LO QUE PROCEDE AL HACER EL LANZAMIENTO DE DADOS