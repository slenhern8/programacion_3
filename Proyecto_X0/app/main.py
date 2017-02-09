
def fin_juego(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    ganador = "no"    # determina si alguno de los jugadores a ganado
    if p1 == p2 == p3:
        ganador = p1
    if p4 == p5 == p6:
        ganador = p4
    if p7 == p8 == p9:
        ganador = p7
    if p1 == p4 == p7:
        ganador = p1
    if p2 == p5 == p8:
        ganador = p2
    if p3 == p6 == p9:
        ganador = p3
    if p3 == p5 == p7:
        ganador = p3
    if p1 == p5 == p9:
        ganador = p1
    return ganador

if __name__ == "__main__":
    p1 = "p1"  # inicializar cada posicion con su nombre para evitar confucion
    p2 = "p2"
    p3 = "p3"
    p4 = "p4"
    p5 = "p5"
    p6 = "p6"
    p7 = "p7"
    p8 = "p8"
    p9 = "p9"

    ganador = fin_juego(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if ganador == "x" or ganador == "0":
        print("Ganador: " + str(ganador))
    else:
        print("Siguiente turno")
