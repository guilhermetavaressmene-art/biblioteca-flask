import livro_repository

def cadastrar_livros(titulo, autor, ano):
    if not titulo.strip():
        raise ValueError('Título obrigatório.')
    
    if not autor.strip():
        raise ValueError('Autor obrigatório.')
    
    if not ano.strip():
        raise ValueError('Ano obrigatório.')
    
    titulo_normalizado = titulo.strip().lower()

    verificar = listar_livros()
    
    for categoria in verificar:
        if categoria[1] == titulo_normalizado:
            raise ValueError("Título ja existente.")
    
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

def remover_livro(id_livro):    
    livro_repository.remover_livro(id_livro)

def buscar_livro_id(id_livro):
    livro_encontrado = livro_repository.buscar_livro(id_livro)

    if livro_encontrado is None:
        raise ValueError("ID inválido.")
        
    return livro_encontrado
    

def atualizar_livro(id_livro, titulo, autor, ano):
    if not titulo.strip():
        raise ValueError("Título obrigatório")
        
    if not autor.strip():
        raise ValueError("Autor obrigatório.")
        
    if not ano.strip():
        raise ValueError("Ano obrigatório.")
        
    livro_repository.atualizar_livro(id_livro, titulo, autor, ano)