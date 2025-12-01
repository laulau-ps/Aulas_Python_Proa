from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Texto a ser exibido na rota /home"

if __name__ == '__main__':
    app.run(debug = True)