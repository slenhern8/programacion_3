from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def circunferencia():
    return render_template('circunferencia.html')

@app.route('/resultado', methods = ['POST'])
def resultado():
    if request.method == 'POST':
        radio = float(request.form.get("radio"))
        resultado = radio * radio *3.1416
        return render_template('area.html', re=resultado, ra=radio)

if __name__ == '__main__':
    app.run()
