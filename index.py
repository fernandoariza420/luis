from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/hospedaje')
def eventos():
    return render_template('hospedaje.html')

if __name__ == '__main__':
    app.run(port=5030, debug=True)


