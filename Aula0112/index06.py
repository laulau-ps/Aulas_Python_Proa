from flask import *

app = Flask(__name__)

@app.route('/administrador')
def administrador():
    return 'Olá administrador'

@app.route('/bibliotecario')
def bibliotecario():
    return 'Olá bibliotecário'

@app.route('/estudante')
def estudante():
    return 'Olá estudante'

@app.route('/usuario/<tipo_usuario>')
def usuario(tipo_usuario):
    if tipo_usuario == 'administrador':
        return redirect(url_for('administrador')) #redireciona para a url que seja 'adiministrador']
    if tipo_usuario == 'bibliotecario':
        return redirect(url_for('bibliotecario'))
    if tipo_usuario == 'estudante':
        return redirect(url_for('estudante'))
    
if __name__ == '__main__':
    app.run(debug = True)    