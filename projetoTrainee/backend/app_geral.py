import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_conexaodb():
    conexao = sqlite3.connect('bancos.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/api/universidade', methods = ['GET'])
def get_universidade():
    conexao = get_conexaodb()
    universidade_cursor = conexao.execute('SELECT * FROM Universidade').fetchall()
    conexao.close()

    universidade = [dict(row) for row in universidade_cursor]
    return jsonify(universidade)

@app.route('/api/universidade/<int:id>', methods=['GET'])
def get_universidadee(id):
    conexao = get_conexaodb()
    universidade_cursor = conexao.execute('SELECT * FROM universidade WHERE id = ?', (id,))
    row = universidade_cursor.fetchone()
    conexao.close()
    if row:
        return jsonify(dict(row))
    else:
        return jsonify({'error': 'Universidade não encontrada'}), 404

@app.route('/api/universidade', methods = ['POST'])
def add_universidade():
    nova_universidade = request.get_json()
    nome = nova_universidade['nome']
    sigla = nova_universidade['sigla']
    data_criacao = nova_universidade['data_criacao']
    publica = nova_universidade['publica']

    conexao = get_conexaodb()
    conexao.execute('INSERT INTO Universidade (nome, sigla, data_criacao, publica) VALUES (?, ?, ?, ?)',
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
    conexao.execute('UPDATE Universidade SET nome = ?, sigla = ?, data_criacao = ?, publica = ? WHERE id = ?',
                    (nome, sigla, data_criacao, publica, id))
    conexao.commit()
    conexao.close()

    return jsonify({'message':'Universidade atualizado com sucesso!'}), 201

@app.route('/api/universidade/<int:id>', methods = ['DELETE'])
def delete_universidade(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Universidade WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()

    return jsonify({'message':'Universidade deletada com sucesso!'})


#--------------------------------------------------------------------------------------------------------------------------------

@app.route('/api/cursos', methods = ['GET'])
def get_cursos():
    conexao = get_conexaodb()
    cursos_cursor = conexao.execute('SELECT Cursos.*, Universidade.nome AS universidade_nome FROM Cursos \
                                    JOIN Universidade ON Cursos.universidade_id = Universidade.id').fetchall()
    conexao.close()

    cursos = [dict(row) for row in cursos_cursor]
    return jsonify(cursos)

@app.route('/api/cursos/<int:id>', methods=['GET'])
def get_cursoss(id):
    conexao = get_conexaodb()
    cursos_cursor = conexao.execute('SELECT Cursos.*, Universidade.nome AS universidade_nome FROM Cursos \
                                    JOIN Universidade ON Cursos.universidade_id = Universidade.id \
                                    WHERE Cursos.id = ?', (id,))
    row = cursos_cursor.fetchone()
    conexao.close()
    if row:
        return jsonify(dict(row))
    else:
        return jsonify({'error': 'Curso não encontrado'}), 404

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

#-------------------------------------------------------------------------------------------------------------------------

@app.route('/api/disciplinas', methods = ['GET'])
def get_disciplina():
    conexao = get_conexaodb()
    disciplinas_cursor = conexao.execute('SELECT Disciplinas.*, Cursos.nome as curso_nome FROM Disciplinas \
                                         JOIN Cursos ON Disciplinas.curso_id = Cursos.id').fetchall()
    conexao.close()

    disciplinas = [dict(row) for row in disciplinas_cursor]
    return jsonify(disciplinas)

@app.route('/api/disciplinas/<int:id>', methods=['GET'])
def get_disciplinass(id):
    conexao = get_conexaodb()
    disciplinas_cursor = conexao.execute('SELECT Disciplinas.*, Cursos.nome as curso_nome FROM Disciplinas \
                                         JOIN Cursos ON Disciplinas.curso_id = Cursos.id \
                                         WHERE Disciplinas.id = ?', (id,))
    row = disciplinas_cursor.fetchone()
    conexao.close()
    if row:
        return jsonify(dict(row))
    else:
        return jsonify({'error': 'Disciplina não encontrada'}), 404

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
def delete_disciplina(id):
    conexao = get_conexaodb()
    conexao.execute('DELETE FROM Disciplinas WHERE id = ?', (id,))

    conexao.commit()
    conexao.close()

    return jsonify({'message':'Disciplina deletada com sucesso!'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)