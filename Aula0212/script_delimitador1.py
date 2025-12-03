from flask import *

app = Flask(__name__)

@app.route('/usuario/<nomeUsuario>')
def mensagem(nomeUsuario):
    return render_template('delimitador1.html',nome=nomeUsuario)

if __name__ == '__main__':
    app.run(debug=True)