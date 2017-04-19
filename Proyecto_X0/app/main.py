'''
Proyecto Final juego TIC TAC TOE (X0)
'''
from app.funciones import evalua_ganardor, IA
from flask import Flask, render_template, request

app = Flask(__name__)
# contadores usados durante la ejecucion del programa. Se inicializan en 0 al inicio
contador = 0
xgana = 0
ogana = 0
empate = 0
p = ['a'] # Array que contiene los datos de las posiciones que se juegan. Por comodidas mias la posicion 0 del array no se usa por eso la 'a'
for i in range(1, 10):  #inicializar con datos diferentes
    p.append(i)


@app.route('/')
def inicio():
    '''
    Funcion inicial. Reinicia los datos de las posiciones para un juego nuevo.
    
    :return: Enseña el 'index.html' en blanco y le envia los datos que necesita para funcionar
    '''
    for i in range(1,10):
        p[i]=i
    global contador
    contador=0
    return render_template('index.html', p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9], gx=xgana, g0=ogana, em=empate)


@app.route('/jugada', methods=['POST'])
def jugada():
    '''
    Aqui sucede todo lo importante. Se llevan a cabo las jugadas
    
    :return: Enseña 'resultado.html' cuando termina el juego o 'index.html' para seguir jugando
    '''
    if request.method == 'POST':
        global contador, xgana, ogana, empate
        pos = int(request.form.get("posicion"))
        p[pos] = 'x'
        contador+=1
        ganador = evalua_ganardor(p)
        if ganador == 'x':
            xgana+=1
            return render_template('resultado.html', gana=ganador, p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9], gx=xgana, g0=ogana, em=empate)
        if contador ==5:
            empate+=1
            return render_template('resultado.html', gana="NADIE", p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9], gx=xgana, g0=ogana, em=empate)
        else:
            a = IA(p)
            p[a] = '0'
            ganador = evalua_ganardor(p)
            if ganador == '0':
                ogana+=1
                return render_template('resultado.html', gana=ganador, p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9], gx=xgana, g0=ogana, em=empate)
        return render_template('index.html', p1=p[1], p2=p[2], p3=p[3], p4=p[4], p5=p[5], p6=p[6], p7=p[7], p8=p[8], p9=p[9], gx=xgana, g0=ogana, em=empate)


if __name__ == "__main__":
    app.run()
