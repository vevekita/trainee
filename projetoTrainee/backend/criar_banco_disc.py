import sqlite3

conexao = sqlite3.connect('banco_disc.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Disciplina(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               carga_horaria INT NOT NULL,
               semestre INT NOT NULL,
               curso_id INT NOT NULL,
               FOREIGN KEY (curso_id) REFERENCES Cursos(id)
               ''')

print("Banco de dados e tabela 'Disciplinas cadastradas' criados!!!")

conexao.commit()
conexao.close()