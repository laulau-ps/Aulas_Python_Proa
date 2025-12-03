from flask import * 

app = Flask(__name__)
@app.route('/')
def mensagem():
    return "<html><body><h1>Mensagem em html interno no python</h1></body></html>"

if __name__ == '__main__':
    app.run(debug=True)