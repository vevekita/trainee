import sqlite3

conexao = sqlite3.connect('banco_uni.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Universidade(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               sigla TEXT NOT NULL,
               data_criacao DATE NOT NULL,
               publica TINYINT NOT NULL)
               ''')

print("Banco de dados e tabela 'Universidades cadastradas' criados!!!")

conexao.commit()
conexao.close()