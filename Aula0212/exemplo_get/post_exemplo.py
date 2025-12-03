from flask import *

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    nomeUsuario=request.args.get('nomeUsuario') #get = .args.get
    senhaUsuario=request.args.get('senhaUsuario')

    if nomeUsuario == 'Laura' and senhaUsuario == '1234':
        return f"Seja bem-vinda {nomeUsuario}"
    else: 
        return f"Usuário ou senha inválidos"
    
if __name__=='__main__':
    app.run(debug = True)    