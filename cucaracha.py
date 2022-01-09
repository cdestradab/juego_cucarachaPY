import libreria as lib

#============================================
#Funcion ............ : crearTablero
#Descripcion ........ : crea un tablero para iniciar el juego de la cucaracha
#Parametros Entrada . : ninguno
#Retorno Salida ..... : una matriz de 15*17 con la forma de la cucaracha.
#============================================

def crearTablero():
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
#Funcion ............ : mensajeBienvenida
#Descripcion ........ : arroja un mensaje de bienvenida sencillo
#Parametros Entrada . : ninguno
#Retorno Salida ..... : ningno
#============================================

def mensajeBienvenida():
  print("================================================")
  print("||       LA CUCARACHA - MISIONTIC 2022          ")
  print("================================================")
  print("||    ,--.       ,---. ")
  print("||   /    '.    /     \ ")
  print("||          (o o)      (/ ")
  print("||  ,------/ >< \---' ")
  print("|| /)     ;  --  :         ¡Bienvenid@!")
  print("||    ,---| ---- |--. ")
  print("||   ;    | ---- |   :     ")
  print("||  (|  ,-| ---- |-. |) ")
  print("||     | /| ---- |\ | ")
  print("||     |/ | ---- | \|[Presiona enter para jugar]")
  print("||     \  : ---- ;  | ")
  print("||      \  \ -- /  / ")
  print("||      ;   \  /  :  ")
  print("||     /   / \/ \  \ ")
  print("||    /)           (\ ")
  print("================================================")
  print("Cristian Estrada B.    |Docente: Alvaro Galeano.")
  print("================================================")
  print("\n")
  input()
  lib.limpiarPantalla()
  return 0

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
  while numJ<2 or numJ >6:
    numJ = numeroJugadores()
  
  # Definir el bote de apuesta
  print("\n ¿Cuanto dinero apostarán los jugadores?")
  print("a. $1.000")
  print("b. $10.000")
  print("c. $50.000")

  bote = lib.inputOpciones("Debe ingresar la letra que corresponda a su opción", "a", "b", "c")
  
  if bote == "a": bote = 1000
  elif bote == "b": bote = 10000
  elif bote == "c": bote = 50000

  # Definir la sancion
  print("\n ¿Cuanto dinero costará la sancion?")
  print("a. $100")
  print("b. $500")
  print("c. $1000")

  sancion = lib.inputOpciones("Debe ingresar la letra que corresponda a su opción", "a", "b", "c")
  
  if sancion == "a": sancion = 100
  elif sancion == "b": sancion = 500
  elif sancion == "c": sancion = 1000

  return [numJ, bote, sancion]
  


