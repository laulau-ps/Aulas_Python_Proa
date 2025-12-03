from flask import * 

app = Flask(__name__)

@app.route('/')
def mensagem():
    #busca na pasta templates o arquivo em questão para renderizar
    return render_template('mensagem.html')

if __name__ == '__main__':
    app.run(debug=True)