import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conexaodb():
    conexao = sqlite3.connect('banco_uni.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/api/universidade' \
'', methods = ['GET'])
def get_universidade():
    conexao = get_conexaodb()
    universidade_cursor = conexao.execute('SELECT * FROM Universidade').fetchall()
    conexao.close()

    universidade = [dict(row) for row in universidade_cursor]
    return jsonify(universidade)

@app.route('/api/universidade', methods = ['POST'])
def add_universidade():
    nova_universidade = request.get_json()
    nome = nova_universidade['nome']
    sigla = nova_universidade['sigla']
    data_criacao = nova_universidade['data_criacao']
    publica = nova_universidade['publica']

    conexao = get_conexaodb()
    conexao.execute('INSERT INTO Universidade(nome, sigla, data_criacao, publica) VALUES (?, ?, ?, ?)',
                    (nome, sigla, data_criacao, publica))
    conexao.commit()
    conexao.close()
    
    return jsonify({'message': 'Universidade adicionada com sucesso!'}), 201

@app.route('/api/universidade/<int:id>', methods = ['PUT'])
def update_universidade(id):
    universidade_atualizada = request.get_json()

    nome = universidade_atualizada['nome']
    sigla = universidade_atualizada['sigla']
    data_criacao = universidade_atualizada['data_criacao']
    publica = universidade_atualizada['publica']

    conexao = get_conexaodb()
    conexao.execute('UPDATE Universidade SET nome = ?, nivel = ?, duracao = ?, data_criacao = ?, publica = ? WHERE id = ?',
                    (nome, sigla, data_criacao, publica, id))
    conexao.commit()
    conexao.close()

    return jsonify({'message':'Universidade atualizado com sucesso!'}), 201

@app.route('/api/universidade/<int:id>', methods = ['DELETE'])
def delete_curso(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Universidade WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()

    return jsonify({'message':'Universidade deletada com sucesso!'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5501, debug = True)