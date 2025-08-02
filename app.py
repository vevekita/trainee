import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conexaodb():
    conexao = sqlite3.connect('banco.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/api/cursos', methods = ['GET'])
def get_cursos():
    conexao = get_conexaodb()
    cursos_cursor = conexao.execute('SELECT * FROM Cursos').fetchall()
    conexao.close()

    cursos = [dict(row) for row in cursos_cursor] # criando dicionário com o que criamos antes.
    return jsonify(cursos)

@app.route('/api/cursos', methods = ['POST'])
def add_curso():
    novo_curso = request.get_json()
    nome = novo_curso['nome']
    nivel = novo_curso['nivel']
    duracao = novo_curso['duracao']
    vagas = novo_curso['vagas']
    carga_horaria = novo_curso['carga_horaria'] # adicionando e forma de dicionário cada uma das informações.

    conexao = get_conexaodb()
    conexao.execute('INSERT INTO Cursos(nome, nivel, duracao, vagas, carga_horaria) VALUES (?, ?, ?, ?, ?)',
                    (nome, nivel, duracao, vagas, carga_horaria))
    conexao.commit()
    conexao.close()
    
    return jsonify({'message': 'Curso adicionado com sucesso!'}), 201 # esse 201 é um protocolo.

@app.route('/api/cursos/<int:id>', methods = ['PUT'])
def update_curso(id):
    curso_atualizado = request.get_json()

    nome = curso_atualizado['nome']
    nivel = curso_atualizado['nivel']
    duracao = curso_atualizado['duracao']
    vagas = curso_atualizado['vagas']
    carga_horaria = curso_atualizado['carga_horaria']

    conexao = get_conexaodb() # abre a conexão.
    conexao.execute('UPDATE Cursos SET nome = ?, nivel = ?, duracao = ?, vagas = ?, carga_horaria = ? WHERE id = ?',
                    (nome, nivel, duracao, vagas, carga_horaria, id))
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
    app.run(host = '0.0.0.0', port = 5000, debug = True)