import random


def evalua_ganardor(p):
    ganador = "no"    # determina si alguno de los jugadores a ganado
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

def leer_posicion():
    pos = int(input("posicion: "))
    # aqui hay que hacer la conecion con la parte grafica del juego
    # al hacer clic en la posicion que se desea jugar debe devolver un valor entre 1-9 segun la posicion
    return pos

def IA(p):
    pos = 0

    i = 1
    flag = True
    while flag:
        if p[i] == i:
            p[i] = '0'
            if evalua_ganardor(p) == '0':
                pos = i
                flag = False
            p[i] = i
        if i == 9:
            flag = False
        i += 1

    if pos == 0:
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

    if pos == 0:
        flag = True
        while flag:
            i = random.randint(1, 9)
            if p[i] == i:
                pos = i
                flag = False

    return pos