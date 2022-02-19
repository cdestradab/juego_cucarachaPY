import sys
sys.path.append('../control/')
sys.path.append('../modelo/')
sys.path.append('../vista/')

import libreria as lib

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
  print("||  ,------/ >< \------' ")
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