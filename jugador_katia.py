#
# Universidad Nacional de Itapua
# Inteligencia Artificial
# 7mo Semestre
#
# Proyecto#2: Torneo Ta-te-ti 3d
#
# Autor: Katia Chaparro
#

import copy
import math

import random

def jugar(tablero, tiempo) :
   while True :
       z = random.randint(0,len(tablero)-1)
       x = random.randint(0,len(tablero[z])-1)
       y = random.randint(0,len(tablero[z][x])-1)
       if ' ' == tablero[z][x][y] :
           return z,x,y

# intercambia en elemento en la posicion( x1 , y1) por el elemento en la posicion (x2, y2) y viseversa
def intercambiar (camino_original, x1,  y1 , x2 , y2):
    estado = copy.deepcopy(camino_original) #seteo estado
    aux_in = estado[y1][x1] #obtengo el numero que esta en esa posicion
    estado[y1][x1] = estado[y2][x2] #cambio el numero por el 0
    estado[y2][x2] = aux_in #cambio el 0 por el numero
    return estado #retorno ese estado


def get_posicion(numero, estado):
    for (x, fila) in enumerate(estado):
        for (y, numero2) in enumerate(fila):
            if numero == numero2:
                return [x, y]


def sucesores(camino_original) :
    # INGRESA TU CODIGO AQUI
    # Devuelve una lista de caminos a tus soluciones
    camino = copy.deepcopy(camino_original)
    estado = copy.deepcopy(camino[len(camino) - 1])
    estados_resultantes = list()
    #obtengo la posicion del 0
    posicion = get_posicion(0, estado)
    tamano = len(estado) #tamano del estado
    #separo la posicion en fila y columna
    columna = posicion[0]
    fila = posicion[1]

    #arriba
    y1 = copy.deepcopy(columna) - 1
    x = copy.deepcopy(fila)
    if y1 >= 0:
        camino1 = copy.deepcopy(camino_original)
        camino1.append(intercambiar(estado, x, y1, fila, columna))
        estados_resultantes.append(camino1) #guardo ese estado

    #abajo
    y2 = copy.deepcopy(columna) + 1
    if y2 < tamano:
        camino2 = copy.deepcopy(camino_original)
        camino2.append(intercambiar(estado, x, y2, fila, columna))
        estados_resultantes.append(camino2) #guardo ese estado

    #izquierda
    x1 = copy.deepcopy(fila) - 1
    y = copy.deepcopy(columna)
    if x1 >= 0:
        camino3 = copy.deepcopy(camino_original)
        camino3.append(intercambiar(estado, x1, y, fila, columna))
        estados_resultantes.append(camino3) #guardo ese estado

    #derecha
    x2 = copy.deepcopy(fila) + 1
    if x2 < tamano:
        camino4 = copy.deepcopy(camino_original)
        camino4.append(intercambiar(estado, x2, y, fila, columna))
        estados_resultantes.append(camino4) #guardo ese estado

    return estados_resultantes
