import sys

sys.path.append('../control/')
sys.path.append('../modelo/')
sys.path.append('../vista/')

import libreria as lib

#============================================
#Funcion ............ : configInicio
#Descripcion ........ : solicita los valores iniciales para jugar
#Parametros Entrada . : ninguno
#Retorno Salida ..... : una lista con tres valores: cantidad de jugadores, cantidad de dinero a apostar y valor de la sanción
#============================================


def configInicio():
  # Definir numero de jugadores, minimo 2, maximo 6
  def numeroJugadores():
      x = lib.inputNumero("\n ¿Cuantos serán los jugadores? (2 a 6)  > ", "entero")
      return x

  numJ = 0
  while numJ < 2 or numJ > 6:
      numJ = numeroJugadores()

  # Definir el bote de apuesta
  def boteApuesta():
      x = lib.inputNumero("\n Ingresa la cantidad del monto de la apuesta  > ", "entero")
      return x

  bote = 0
  while bote < 1000 or bote > 1000000:
      bote = boteApuesta()

  # Definir la sancion
  print("\n ¿Cuanto dinero costará la sancion?")
  print("a. " + str(int(bote / 20)))
  print("b. " + str(int(bote / 10)))
  print("c. " + str(int(bote / 5)))

  sancion = lib.inputOpciones("Debe ingresar la letra que corresponda a su opción", "a", "b", "c")

  if sancion == "a": sancion = int(bote / 20)
  elif sancion == "b": sancion = int(bote / 10)
  elif sancion == "c": sancion = int(bote / 5)

  lib.LimpiarPantalla()
  
  return [numJ, bote, sancion]
