from flask import Flask

app = Flask(__name__)

def sobre():
    return "Essa é página de sobre nós"

app.add_url_rule('/about', 'about', sobre) #outra maneira de chamar a rota
                #rota |             | função

if __name__ == '__main__':
    app.run(debug = True)
    
