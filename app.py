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
    
@app.route('/remover/<int:id_livro>')
def remover_livro(id_livro):
    try:
        livro_service.remover_livro(id_livro)
        return redirecionar()

    except ValueError as erro:
        livros = livro_service.listar_livros()
        
        return render_template(
            'livros.html',
            livros=livros,
            erro=str(erro))
    
            
@app.route("/editar/<int:id_livro>", methods=['GET', 'POST'])
def editar_livro(id_livro):
    match request.method:
        case 'GET':
            try:
                livro = livro_service.buscar_livro_id(id_livro)
                return render_template("editar.html",
                                    livro=livro)
                
            except ValueError as erro:
                return render_template('editar.html',
                                        erro=str(erro))
    
        case 'POST':
            titulo = request.form['titulo']
            autor = request.form['autor']
            ano = request.form['ano']

            try:
                livro_service.atualizar_livro(id_livro, titulo, autor, ano)
                return redirecionar()
                
            except ValueError as erro:
                livro = livro_service.buscar_livro_id(id_livro)

                return render_template('editar.html',
                                        livro=livro,
                                        erro=str(erro))

if __name__ == "__main__":
    app.run(debug=True)