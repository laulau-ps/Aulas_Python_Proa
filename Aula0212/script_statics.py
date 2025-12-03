from flask import *

app = Flask(__name__)

@app.route('/')
def mensagem():
    return render_template('exemplo_statics.html')

if __name__ == '__main__':
    app.run(debug=True)