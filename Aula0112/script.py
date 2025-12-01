from flask import Flask

app = Flask(__name__)

@app.route('/') #rota (URL) da página
def home(): #função do que será feito
    return "Primeiro teste de flask"

if __name__ == '__main__':
    app.run(debug = True)