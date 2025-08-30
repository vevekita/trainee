import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conexaodb():
    conexao = sqlite3.connect('banco_curso.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/api/cursos', methods = ['GET'])
def get_cursos():
    conexao = get_conexaodb()
    cursos_cursor = conexao.execute('SELECT * FROM Cursos').fetchall()
    conexao.close()

    cursos = [dict(row) for row in cursos_cursor]
    return jsonify(cursos)

@app.route('/api/cursos', methods = ['POST'])
def add_curso():
    novo_curso = request.get_json()
    nome = novo_curso['nome']
    nivel = novo_curso['nivel']
    duracao = novo_curso['duracao']
    universidade_id = novo_curso['universidade_id']

    conexao = get_conexaodb()
    conexao.execute('INSERT INTO Cursos(nome, nivel, duracao, universidade_id) VALUES (?, ?, ?, ?)',
                    (nome, nivel, duracao, universidade_id))
    conexao.commit()
    conexao.close()
    
    return jsonify({'message': 'Curso adicionado com sucesso!'}), 201 

@app.route('/api/cursos/<int:id>', methods = ['PUT'])
def update_curso(id):
    curso_atualizado = request.get_json()

    nome = curso_atualizado['nome']
    nivel = curso_atualizado['nivel']
    duracao = curso_atualizado['duracao']
    universidade_id = curso_atualizado['universidade_id']

    conexao = get_conexaodb()
    conexao.execute('UPDATE Cursos SET nome = ?, nivel = ?, duracao = ?, universidade_id = ? WHERE id = ?',
                    (nome, nivel, duracao, universidade_id, id))
    conexao.commit()
    conexao.close()

    return jsonify({'message':'Curso atualizado com sucesso!'}), 201

@app.route('/api/cursos/<int:id>', methods = ['DELETE'])
def delete_curso(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Cursos WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()

    return jsonify({'message':'Curso deletado com sucesso!'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5501, debug = True)