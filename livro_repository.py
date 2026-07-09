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

def remover_livro(id_livro):
    conexao = database.conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   DELETE FROM livros
                   WHERE id = ?
                   """,
                   (id_livro,))
    
    conexao.commit()
    conexao.close()

def atualizar_livro(id_livro, titulo, autor, ano):
    conexao = database.conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   UPDATE livros
                   SET titulo = ?, autor = ?, ano = ?
                   WHERE id = ?
                   """,
                   (titulo, autor, ano, id_livro))
    
    conexao.commit()
    conexao.close()

def buscar_livro(id_livro):
    conexao = database.conectar()
    cursor = conexao.cursor()

    cursor.execute("""
                   SELECT *
                   FROM livros
                   WHERE id = ?
                   """,
                   (id_livro,))
    
    livro = cursor.fetchone()

    conexao.close()
    return livro
