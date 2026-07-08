import sqlite3

def conectar():
    return sqlite3.connect('livros.db')
    

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS livros
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL UNIQUE,
                   autor TEXT NOT NULL,
                   ano INTEGER NOT NULL,
                   disponibilidade INTEGER NOT NULL)
                   """)
    
    conexao.commit()
    conexao.close()
