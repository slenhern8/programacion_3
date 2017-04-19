'''
En este modulo estan todas las funciones complejas necesarias para que funcione el programa
'''
import random


def evalua_ganardor(p):
    '''
    Esta funcion se usa para ver cuando alguno de los jugadores gana
    :param p: Es el array que contiene la informacion de que posiciones se jugaron
    :type p: str
    
    :return: retorna quien gano ('X' o '0') o 'no' cuando nadie a ganado 
    :rtype: str
    '''
    ganador = "no"    # Estas son todas las posibles formas de ganar en el juego
    if p[1] == p[2] == p[3]:
        ganador = p[1]
    if p[4] == p[5] == p[6]:
        ganador = p[4]
    if p[7] == p[8] == p[9]:
        ganador = p[7]
    if p[1] == p[4] == p[7]:
        ganador = p[1]
    if p[2] == p[5] == p[8]:
        ganador = p[2]
    if p[3] == p[6] == p[9]:
        ganador = p[3]
    if p[3] == p[5] == p[7]:
        ganador = p[3]
    if p[1] == p[5] == p[9]:
        ganador = p[1]
    return ganador


def IA(p):
    '''
    Esta funcion genera las jugadas que va a hacer la computadora
    
    :param p: Es el array que contiene la informacion de que posiciones se jugaron
    :type p: str
    
    :return: regresa la posicion que va a jugar la computadora
    :rtype: int
    '''
    pos = 0
    i = 1
    flag = True
    while flag:     # primero evalua si la IA ganaria al jugar en alguna posicion, de ser asi juega esa para ganar
        if p[i] == i:
            p[i] = '0'
            if evalua_ganardor(p) == '0':
                pos = i
                flag = False
            p[i] = i
        if i == 9:
            flag = False
        i += 1

    if pos == 0:        # si no obtine una posicion que jugar aun, evalua si el jugador ganaria al jugar una posicion, de ser asi juega esa para no perder
        i = 1
        flag = True
        while flag:
            if p[i] == i:
                p[i] = 'x'
                if evalua_ganardor(p) == 'x':
                    pos = i
                    flag = False
                p[i] = i
            if i == 9:
                flag = False
            i +=1

    if pos == 0:        # si aun no obtiene una posicion que jugar escoje una al azar entre las disponibles
        flag = True
        while flag:
            i = random.randint(1, 9)
            if p[i] == i:
                pos = i
                flag = False

    return pos