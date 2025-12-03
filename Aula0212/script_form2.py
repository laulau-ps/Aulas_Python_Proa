from flask import *

app = Flask(__name__)

@app.route('/')
def cliente():
    return render_template('form_cliente.html')

@app.route('/sucesso', methods=['POST', 'GET'])
def exibir_dados():
    if request.method == 'POST':
        resultado = request.form
        return render_template('dados_resultado.html', resultado = resultado)
    
if __name__ == '__main__':
    app.run(debug=True)