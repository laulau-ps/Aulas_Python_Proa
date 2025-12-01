from flask import Flask

app = Flask(__name__)

@app.route('/home/<int:idade>')
def home(idade):
    return f"Idade = {idade}"
   # return "Idade = %d"%idade -> meio de exibir o número inteiro


if __name__ == '__main__':
    app.run(debug = True)