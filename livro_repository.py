import database

def inserir_livros(titulo, autor, ano):
    conexao = database.conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   INSERT INTO livros
                   (titulo, autor, ano, disponibilidade)
                   VALUES (?, ?, ?, 1)
                   """,
                   (titulo, autor, ano)
    )
    
    conexao.commit()
    conexao.close()

def listar_livros():
    conexao = database.conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   SELECT id, titulo, autor, ano, disponibilidade
                   FROM livros
                   ORDER BY titulo
                   """)
    
    livros = cursor.fetchall()

    conexao.close()
    return livros

def remover_livro(titulo):
    conexao = database.conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   DELETE FROM livros
                   WHERE titulo = ?
                   """,
                   (titulo,))
    
    conexao.commit()
    conexao.close()