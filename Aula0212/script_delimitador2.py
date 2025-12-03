from flask import *

app = Flask(__name__)

@app.route('/tabuada/<int:numero>')
def tabuada(numero):
    return render_template('delimitador2.html', numero = numero)

if __name__ == '__main__':
    app.run(debug=True)