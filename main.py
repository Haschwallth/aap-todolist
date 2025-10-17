#importação de bibliotecas
from flask import Flask

#cria o objeto deo flask
app = Flask(__name__)

#criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

#identifica que é o arquivo principal e liga o servidor executando o Flask
if __name__ == "__main__":
    app.run(debug=True)
