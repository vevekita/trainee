import sqlite3

conexao = sqlite3.connect('banco_curso.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nivel TINYINT NOT NULL,
               duracao INT NOT NULL,
               universidade_id INT NOT NULL,
               FOREIGN KEY (universidade_id) REFERENCES Universidade(id)
               ''')

print("Banco de dados e tabela 'Cursos Cadastrados' criados!!!")

conexao.commit()
conexao.close()