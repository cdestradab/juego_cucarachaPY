import sys
sys.path.append('../control/')
sys.path.append('../modelo/')
sys.path.append('../vista/')

import libreria as lib

#============================================
#Funcion ............ : crearCabecera
#Descripcion ........ : crea una cabecera que muestra un título para el tablero
#Parametros Entrada . : titulo, lenghtCabecera
#Retorno Salida ..... : cabecera
#============================================
def CrearCabecera(titulo, lenghtCabecera):
  cabecera = ""
  intCabecera = lenghtCabecera - 2
  blankCabecera = int(((intCabecera/2)-(len(titulo)/2)))
  correctorCabecera = 0

  while (2 + 2*blankCabecera + len(titulo) + correctorCabecera) < lenghtCabecera:
    correctorCabecera += 1
  
  cabecera = cabecera + "╔" + intCabecera*"═" + "╗" + "\n"
  cabecera = cabecera + "║" + " "*blankCabecera + titulo + " "*(blankCabecera + correctorCabecera) + "║" + "\n"
  cabecera = cabecera + "╠" + 19*"═" + "╦" + (intCabecera-20)*"═" + "╣"

  return cabecera

#============================================
#Funcion ............ : CrearPiePagina
#Descripcion ........ : crea una pie de página para mostrar información al jugador.
#Parametros Entrada . : info, lenghtPie
#Retorno Salida ..... : cabecera
#============================================
def CrearPiePagina(info, lenghtPie):
  piePagina = ""
  intPie = lenghtPie - 2
  
  piePagina = piePagina + "╠" + intPie*"═" + "╣" + "\n"
  piePagina = piePagina + "║ " + lib.AdjustLenght(intPie-1, info, " ") + "║" + "\n"
  piePagina = piePagina + "╚" + intPie*"═" + "╝"

  return piePagina
  
#============================================
#Funcion ............ : crearCucaracha
#Descripcion ........ : crea un tablero para iniciar el juego de la cucaracha
#Parametros Entrada . : ninguno
#Retorno Salida ..... : una matriz de 15*17 con la forma de la cucaracha.
#============================================

def CrearCucaracha():
  tablero = lib.crearMatriz(15,17," ")

  # Definir puntos para completar
  tablero = lib.cambElemMatriz(tablero, "o", (0,5),(0,11),(2,7),(2,9),(3,8),(4,6),(4,10))
  tablero = lib.cambElemMatriz(tablero, "o", (2,1),(2,15),(5,0),(5,7),(5,9),(5,16),(7,6),(7,10),(9,0),(9,4),(9,12),(9,16),(13,1),(13,7),(13,9),(13,15))
  tablero = lib.cambElemMatriz(tablero, "o", (14,8))

  # Definir puntos estéticos
  tablero = lib.cambElemMatriz(tablero, "\\", (1,6),(3,2),(4,3),(5,4),(6,1),(6,10),(7,2),(8,11),(10,1),(11,5),(12,6))
  tablero = lib.cambElemMatriz(tablero, "/", (1,10),(3,14),(4,13),(5,12),(6,6),(6,15),(7,14),(8,5),(10,15),(11,11),(12,10))
  tablero = lib.cambElemMatriz(tablero, "_", (5,5),(5,6),(5,10),(5,11),(7,3),(7,4),(7,5),(7,11),(7,12),(7,13))
  tablero = lib.cambElemMatriz(tablero, "_", (5,5),(5,6),(5,10),(5,11),(7,3),(7,4),(7,5),(7,11),(7,12),(7,13))
  tablero = lib.cambElemMatriz(tablero, "—", (9,1),(9,2),(9,3),(9,13),(9,14),(9,15))
  tablero = lib.cambElemMatriz(tablero, "|", (10,4),(10,12),(11,1),(11,15),(12,1),(12,15))
  return tablero

#============================================
#Funcion ............ : crearCuadroInformativo
#Descripcion ........ : crea una matriz con la que se mostrará luego la información del jugador
#Parametros Entrada . : no
#Retorno Salida ..... : una matriz con la información que corresponde al turno del jugador.
#============================================

def CrearCuadroInformativo(infoTurno, infoJugador, ultimaTirada, anchoCuadro):
  prototipo = [" Turno " + str(infoTurno['turno'])," Jugador " + str(infoTurno['jugador']), "" ," Dinero Actual: ", " " + str(infoJugador['montoActual']), "", " Última tirada: ", "", " [" + str(ultimaTirada[0]) + "] " , " [" + str(ultimaTirada[1]) + "] ", " [" + str(ultimaTirada[2]) + "] ", " [" + str(ultimaTirada[3]) + "] ", " [" + str(ultimaTirada[4]) + "] ", "", ""]

  cuadroDefinitivo = []

  for linea in prototipo:
    cuadroDefinitivo.append(lib.AdjustLenght(anchoCuadro, linea, " "))
  
  return cuadroDefinitivo
  
#============================================
#Funcion ............ : impTablero
#Descripcion ........ : imprime matrices en pantalla
#Parametros Entrada . : "matriz" que es la matriz que la función debe leer
#Retorno Salida ..... : no retorna nada, muestra en pantalla una matriz en forma de texto (string)
#============================================

def PrintTablero(cucaracha, info):
  numFila = 0
  for fila in cucaracha:
    impFila = "║ "
    for elem in fila:
      impFila += str(elem[0])
    print(impFila + " ║" + info[numFila] + "║")
    numFila += 1