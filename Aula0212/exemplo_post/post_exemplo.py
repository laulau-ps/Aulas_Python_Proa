from flask import *

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    nomeUsuario=request.form['nomeUsuario'] #post = .form
    senhaUsuario=request.form['senhaUsuario']

    if nomeUsuario == 'Laura' and senhaUsuario == '1234':
        return f"Seja bem-vinda {nomeUsuario}"
    else: 
        return f"Usuário ou senha inválidos"
    
if __name__=='__main__':
    app.run(debug = True)    