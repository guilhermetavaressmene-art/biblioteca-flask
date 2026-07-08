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

- `app.py`: rotas Flask e comunicação HTTP
- `livro_service.py`: regras de negócio e validações
- `livro_repository.py`: acesso ao banco de dados
- `database.py`: conexão e criação da tabela
- `templates/`: páginas HTML com Jinja

## Funcionalidades

- Listar livros
- Cadastrar livros
- Remover livros
- Validação de campos obrigatórios
- PRG: Post/Redirect/Get após cadastro e remoção
- Conversão de disponibilidade do banco para texto na camada de serviço

## Como executar

```bash
pip install flask
python app.py

Acesse: http://127.0.0.1:5000