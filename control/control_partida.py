import sys
sys.path.append('../control/')
sys.path.append('../modelo/')
sys.path.append('../vista/')

import libreria as lib

#============================================
#Funcion ............ : GenerarPerfiles
#Descripcion ........ : Crea los perfiles de los jugadores que contienen la información de la partida y su progreso para cada uno de ellos.
#Parametros Entrada . : cantJugadores, monto
#Retorno Salida ..... : perfiles
#============================================

def GenerarPerfiles(cantJugadores, monto):
  perfiles = []
  for jugador in range(1,cantJugadores+1):
    nuevoPerfil = {'id': jugador, 'montoActual': monto, 'puntaje':[0,0,0], 'continua': True}
    perfiles.append(nuevoPerfil)
  return perfiles

#============================================
#Funcion ............ : PasarOTirar
#Descripcion ........ : Permite al jugador elegir si tirará los dados o pasará
#Parametros Entrada . : 
#Retorno Salida ..... : 
#============================================

def PasarOTirar():
  print("\n")
  eleccion = lib.inputOpciones("Escoge una opción válida", "p", "t")
  return eleccion