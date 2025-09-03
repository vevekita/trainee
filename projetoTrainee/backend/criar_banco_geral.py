import sqlite3

conexao = sqlite3.connect('bancos.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Universidade(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               sigla TEXT NOT NULL,
               data_criacao DATE NOT NULL,
               publica TINYINT NOT NULL)
                ''')
               
cursor.execute('''               
CREATE TABLE IF NOT EXISTS Cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               nivel TEXT NOT NULL,
               duracao INT NOT NULL,
               universidade_id INT NOT NULL,
               FOREIGN KEY (universidade_id) REFERENCES Universidade(id))
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Disciplinas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               carga_horaria INT NOT NULL,
               semestre INT NOT NULL,
               curso_id INT NOT NULL,
               FOREIGN KEY (curso_id) REFERENCES Cursos(id))
               ''')

print("Bancos de dados e tabelas criados!!!")

conexao.commit()
conexao.close()