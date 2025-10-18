#importação de bibliotecas
from flask import Flask
from tarefa import buscar_tarefas

#cria o objeto deo flask
app = Flask(__name__)

#criando a rota que retorna as tarefas
@app.route('/api/tarefas')
def get_tarefa():
    tarefas = buscar_tarefas()
    return tarefas

#criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

#identifica que é o arquivo principal e liga o servidor executando o Flask
if __name__ == "__main__":
    app.run(debug=True)
