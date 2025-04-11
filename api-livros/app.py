#ATENÇÃO: O seguinte código foi feito na aula do youtube 'Como CRIAR uma API com PYTHON [DO ZERO]'
#No canal Dev Aprender

#essa é uma simples api com put, get, post e delete. foi utilizado flask como server
# e as consultas podem ser realizadas no postman ou localhost:5000

#instalando requisitos, flask eh o servidor, jsonify o formato da api,
#  request nos permite acessar dados


from flask import Flask, jsonify, request

app = Flask(__name__)

# os dados serão uma lista de dicionarios

livros = [
    {
        'id': 1,
        'titulo': 'Mo Dao Zu Shi',
        'autor': 'Mo Xiang Tong Xiu'
    },
    {
        'id': 2,
        'titulo': 'Wicked',
        'autor': 'Glinda Upland'
    },
    {
        'id': 3,
        'titulo': 'Hamlet',
        'autor': 'William Shakespeare'
    },
]

#Consultar todos

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        

#Editar por ID
@app.route('/livros/<int:id>', methods=['PUT'])        
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Criar Livro        
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir Livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)

