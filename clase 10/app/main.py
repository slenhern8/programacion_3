from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return '<html><body><h1>Hola!</h1></body></html>'
    return render_template('index.html')

@app.route('/hola/<nombre>')
def hola_nombre(nombre):
    return render_template('hola.html', nom=nombre)

@app.route('/vn/<int:nota>')
def validar_nota(nota):
    return render_template('validador.html', n=nota)

@app.route('/promedio')
def calcular_promedio():
    promedio = 0
    notas = {'nota1':95, 'nota2': 75, 'nota3':85}
    for nota in list(notas.values()):
        promedio = promedio + nota
    promedio = promedio/len(notas)
    return render_template('promedio.html', resultado = notas, prom = promedio)

if __name__== "__main__":
    app.run()
