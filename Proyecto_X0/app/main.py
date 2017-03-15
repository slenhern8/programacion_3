from app.funciones import evalua_ganardor, leer_posicion, IA


if __name__ == "__main__":
    p = ['a']
    for i in range(1, 10): #inicializar con datos diferentes
        p.append(i)

    flag = True
    i=1
    while flag:
        if i%2 == 0:   #decide a quien le toca jugar
            print("\nturno de 0")
            a = IA(p)
            p[a] = '0'
            print(" IA juega en la posicion: "+ str(a))
        else:
            print("\nturno de X")
            p[leer_posicion()] = 'x'



        ganador = evalua_ganardor(p)
        if ganador == "x" or ganador == "0":
            print("Ganador: " + str(ganador))
            flag = False
        else:
            if i == 9:
                print("Empate")
            else:
                print("Siguiente turno")

        if i == 9:  #rompe el ciclo si luego de 9 turnos no hay ganador
           flag = False
        i +=1

    print("\n Fin del juego")
