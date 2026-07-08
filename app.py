from flask import Flask, redirect, render_template, request, url_for
import database
import livro_service

app = Flask(__name__)

database.criar_tabela()

def redirecionar():
    return redirect(url_for('livros'))

@app.route('/')
def inicio():
    return redirecionar()

@app.route('/livros')
def livros():
    livros = livro_service.listar_livros()

    return render_template(
        'livros.html',
        livros=livros
    )

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_livro():
    match request.method:
        case 'GET':
            return render_template('cadastrar.html')

        case 'POST':
            titulo = request.form['titulo']
            autor = request.form['autor']
            ano = request.form['ano']

            try:
                livro_service.cadastrar_livros(titulo, autor, ano)
                return redirecionar()
            
            except ValueError as erro:
                return render_template(
                    "cadastrar.html",
                    erro=str(erro)
                )
    
@app.route('/remover', methods=['GET', 'POST'])
def remover():
    match request.method:
        case 'GET':
            return render_template('remover.html')
        
        case 'POST':    
            livro_removido = request.form['removido']

            try:
                livro_service.remover_livro(livro_removido)
                return redirecionar()

            except ValueError as erro:
                return render_template(
                    'remover.html',
                    erro=str(erro)
                )
            
if __name__ == "__main__":
    app.run(debug=True)