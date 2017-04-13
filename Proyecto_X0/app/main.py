from app.funciones import evalua_ganardor, leer_posicion, IA
from flask import Flask, render_template, request

app = Flask(__name__)

contador = 0
p = ['a']
for i in range(1, 10):  #inicializar con datos diferentes
    p.append(i)


@app.route('/')
def inicio():
    for i in range(1,10):
        p[i]=i
    global contador
    contador=0
    return render_template('index.html', p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9])


@app.route('/jugada', methods=['POST'])
def jugada():
    if request.method == 'POST':
        pos = int(request.form.get("posicion"))
        p[leer_posicion(pos)] = 'x'
        global contador
        contador+=1
        ganador = evalua_ganardor(p)
        if ganador == 'x':
            return render_template('resultado.html', gana=ganador, p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9])
        if contador ==5:
            return render_template('resultado.html', gana="NADIE", p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9])
        else:
            a = IA(p)
            p[a] = '0'
            ganador = evalua_ganardor(p)
            if ganador == '0':
                return render_template('resultado.html', gana=ganador, p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9])
        return render_template('index.html', p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9])



if __name__ == "__main__":
    app.run()


'''  ESTE FUE EL PRIMER PROTOTIPO ANTES DE AÑADIR EL FLASK EN LA VERSION FINAL ESTAS LINEAS SERAN ELIMINADAS
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
'''