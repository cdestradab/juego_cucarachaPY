import os
import random

#============================================
#Funcion ............ : crearMatriz
#Descripcion ........ : crea matrices
#Parametros Entrada . : n son las filas, m son las columnas, caracter es el valor que tendran todos los elementos de la matriz.
#Retorno Salida ..... : una matriz de tamaño n*m con todos los elementos iguales al valor de "dato"
#============================================

def crearMatriz(n,m, caracter):
  matriz = []
  for i in range(n):
    fila = [caracter]*m
    matriz.append(fila)
  return matriz

#============================================
#Funcion ............ : impMatriz
#Descripcion ........ : imprime matrices en pantalla
#Parametros Entrada . : "matriz" que es la matriz que la función debe leer
#Retorno Salida ..... : no retorna nada, muestra en pantalla una matriz en forma de texto (string)
#============================================

def impMatriz(matriz):
  for fila in matriz:
    impFila = ""
    for elem in fila:
      impFila += str(elem)
    print(impFila)

#============================================
#Funcion ............ : cambElemMatriz
#Descripcion ........ : cambia el valor de varios elementos de una matriz
#Parametros Entrada . : "matriz" que es la matriz a la que se le cambiarán los valores, "valor" será el valor que obtengan los elementos de la matriz, "*coord" se colocarán en forma de tupla las coordenadas a las cuales se les asignará el valor indicado
#Retorno Salida ..... : retorna la matriz modificada
#============================================

def cambElemMatriz(matriz, valor, *coordenadas):
  nuevaMatriz = matriz
  for coord in coordenadas:
    n=coord[0]
    m=coord[1]
    nuevaMatriz[n][m]=valor
  return nuevaMatriz
#============================================
#Funcion ............ : tirarDados
#Descripcion ........ : Arroja un número pseudo-aleatorio
#Parametros Entrada . : "caras" indica cuantas caras tiene el dado, "cantidad" indica cuantos dados son arrojados
#Retorno Salida ..... : arroja una lista con los valores obtenidos
#============================================

def tirarDados(caras, cantidad):
  resultado = []
  for i in range(cantidad):
    resultado.append(random.randint(1,caras))
  return resultado

#============================================
#Funcion ............ : limpiarPantalla
#Descripcion ........ : Limpia la pantalla
#Parametros Entrada . : Ninguno
#Retorno Salida ..... : NInguno
#============================================
def limpiarPantalla():
  os.system('clear')


#============================================
#Funcion ............ : preguntaContinuar
#Descripcion ........ : Pregunta al usuario si continuar con el curso del programa, el usuario debe responder según se indica.
#Parametros Entrada . : Ninguno
#Retorno Salida ..... : Booleano
#============================================
def preguntaContinuar():
  todoOk = False
  snOk = False
  while snOk == False:
    comprobar = input("¿Continuar? (s/n): ")
    if comprobar == "s": 
      todoOk = True
      snOk = True
    elif comprobar == "n": 
      todoOk = False
      snOk = True
    else: 
      print("\n Escriba 's' para continuar 'n' para escoger otra opción. \n")
      snOk = False
  return todoOk

#============================================
#Funcion ............ : checkInputNumero
#Descripcion ........ : Permite solicitar un valor y verificar que sea un valor numérico.
#Parametros Entrada . : "mensajeInput" es el mensaje con el que se solicita el valor a ingresar, "entero0flotante" es el tipo de valor numérico que se requiere obtener si el valor ingresado es, en efecto un número y no un caracter de texto.
#Retorno Salida ..... : el valor numerico que ingrese el usuario convertido en entero o flotante según convenga
#============================================

def inputNumero(mensajeInput, enteroOflotante):
  valorIngresado = input(mensajeInput)
  try:
    if enteroOflotante == "entero":
      valorRevisado = int(valorIngresado)
    elif enteroOflotante == "flotante":
      valorRevisado = float(valorIngresado)
    return valorRevisado
  except ValueError:
    print("ERROR: El valor ingresado debe ser un número \n")
    return inputNumero(mensajeInput,enteroOflotante)


#============================================
#Funcion ............ : inputOpciones
#Descripcion ........ : Permite verificar que el usuario ingrese especificamente los valores de un conjunto de opciones y solo esos
#Parametros Entrada . : "mensajeError" es el mensaje con el que se avisa al usuario que ha cometido un error, "*opciones" serán los valores de las opciones dadas.
#Retorno Salida ..... : el valor que ingrese el usuario que se encuentre dentro del rango de opciones indicadas.
#============================================
def inputOpciones(mensajeError, *opciones):
  todoOk = False
  while todoOk == False:
    valorIngresado = input("Ingrese su opción: ")
    if valorIngresado not in opciones:
      print(mensajeError)
    else: 
      todoOk = preguntaContinuar()
  return valorIngresado