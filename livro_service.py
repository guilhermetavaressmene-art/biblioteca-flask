import livro_repository

def cadastrar_livros(titulo, autor, ano):
    if not titulo.strip():
        raise ValueError('Título obrigatório.')
    
    if not autor.strip():
        raise ValueError('Autor obrigatório.')
    
    if not ano.strip():
        raise ValueError('Ano obrigatório.')
    
    livro_repository.inserir_livros(titulo, autor, ano)

def listar_livros():
    livros = livro_repository.listar_livros()
    livros_formatados = []

    for livro in livros:
        id_livro = livro[0]
        titulo = livro[1]
        autor = livro[2]
        ano = livro[3]
        disponibilidade = livro[4]

        if disponibilidade == 1:
            texto_disponibilidade = 'disponível'

        else:
            texto_disponibilidade = 'indisponível'

        livros_formatados.append((
            id_livro,
            titulo,
            autor,
            ano,
            texto_disponibilidade
        ))

    return livros_formatados

def remover_livro(titulo):
    if not titulo.strip():
        raise ValueError('Título obrigatório.')
    
    livro_repository.remover_livro(titulo)