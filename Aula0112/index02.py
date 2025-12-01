from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Teste para a rota /home \n Somente a dor coletiva gera união"

@app.route('/')
def inicio():
    return "Não grita"

if __name__ == '__main__':
    app.run(debug = True)