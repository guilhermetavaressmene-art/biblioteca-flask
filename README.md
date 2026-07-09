# Biblioteca Flask

Projeto de estudo em Back-End Python com Flask e SQLite.

## Objetivo

Construir uma aplicação de biblioteca usando arquitetura em camadas, separando responsabilidades entre rotas, regras de negócio, acesso ao banco de dados e interface HTML.

## Tecnologias

- Python
- Flask
- SQLite
- HTML/Jinja

## Arquitetura

- `app.py`: rotas Flask, requisições HTTP, redirecionamentos e renderização de templates
- `livro_service.py`: regras de negócio, validações e formatação de dados
- `livro_repository.py`: acesso ao banco de dados e execução de comandos SQL
- `database.py`: conexão com SQLite e criação da tabela
- `templates/`: páginas HTML com Jinja

## Funcionalidades

- Listar livros
- Cadastrar livros
- Editar livros
- Remover livros por id
- Validar campos obrigatórios
- Validar título duplicado
- Exibir disponibilidade em formato legível
- Utilizar rotas dinâmicas com parâmetros
- Aplicar PRG: Post/Redirect/Get após cadastro e edição

## Conceitos praticados

- Arquitetura em camadas
- Separação de responsabilidades
- Rotas GET e POST
- Formulários HTML integrados ao Flask
- Templates com Jinja
- Operações SQL: SELECT, INSERT, UPDATE e DELETE
- Tratamento de erros com `raise` e `try/except`
- Uso de `url_for` com parâmetros
- Versionamento com Git e GitHub

## Como executar

```bash
pip install flask
python app.py
Acesse: http://127.0.0.1:5000