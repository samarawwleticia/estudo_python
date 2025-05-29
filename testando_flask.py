from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200))

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'descricao': self.descricao}


# Inicializar o banco de dados
@app.before_request
def criar_tabelas():
    db.create_all()

# Rota principal
@app.route('/')
def home():
    return {'mensagem': 'API Flask CRUD funcionando'}

# Criar (POST)
@app.route('/itens', methods=['POST'])
def criar_item():
    data = request.get_json()
    novo_item = Item(nome=data['nome'], descricao=data.get('descricao', ''))
    db.session.add(novo_item)
    db.session.commit()
    return jsonify(novo_item.to_dict()), 201

# Listar todos (GET)
@app.route('/itens', methods=['GET'])
def listar_itens():
    itens = Item.query.all()
    return jsonify([item.to_dict() for item in itens])

# Obter item por ID (GET)
@app.route('/itens/<int:id>', methods=['GET'])
def obter_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_dict())

# Atualizar (PUT)
@app.route('/itens/<int:id>', methods=['PUT'])
def atualizar_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.nome = data.get('nome', item.nome)
    item.descricao = data.get('descricao', item.descricao)
    db.session.commit()
    return jsonify(item.to_dict())

# Deletar (DELETE)
@app.route('/itens/<int:id>', methods=['DELETE'])
def deletar_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return {'mensagem': 'Item deletado com sucesso'}

if __name__ == '__main__':
    app.run(debug=True)
