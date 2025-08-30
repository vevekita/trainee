import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conexaodb():
    conexao = sqlite3.connect('banco_disc.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/api/disciplinas', methods = ['GET'])
def get_disciplina():
    conexao = get_conexaodb()
    disciplinas_cursor = conexao.execute('SELECT * FROM Disciplinas').fetchall()
    conexao.close()

    disciplinas = [dict(row) for row in disciplinas_cursor]
    return jsonify(disciplinas)

@app.route('/api/disciplinas', methods = ['POST'])
def add_disciplina():
    nova_disciplina = request.get_json()
    nome = nova_disciplina['nome']
    carga_horaria = nova_disciplina['carga_horaria']
    semestre = nova_disciplina['semestre']
    curso_id = nova_disciplina['curso_id']

    conexao = get_conexaodb()
    conexao.execute('INSERT INTO Disciplinas(nome, carga_horaria, semestre, curso_id) VALUES (?, ?, ?, ?)',
                    (nome, carga_horaria, semestre, curso_id))
    conexao.commit()
    conexao.close()
    
    return jsonify({'message': 'Disciplina adicionada com sucesso!'}), 201

@app.route('/api/disciplinas/<int:id>', methods = ['PUT'])
def update_disciplina(id):
    disciplina_atualizada = request.get_json()

    nome = disciplina_atualizada['nome']
    carga_horaria = disciplina_atualizada['carga_horaria']
    semestre = disciplina_atualizada['semestre']
    curso_id = disciplina_atualizada['curso_id']

    conexao = get_conexaodb()
    conexao.execute('UPDATE Disciplinas SET nome = ?, carga_horaria = ?, semestre = ?, curso_id = ? WHERE id = ?',
                    (nome, carga_horaria, semestre, curso_id, id))
    conexao.commit()
    conexao.close()

    return jsonify({'message':'Disciplina atualizada com sucesso!'}), 201

@app.route('/api/disciplinas/<int:id>', methods = ['DELETE'])
def delete_curso(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Disciplinas WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()

    return jsonify({'message':'Disciplina deletada com sucesso!'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5500, debug = True)