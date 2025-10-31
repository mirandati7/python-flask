from flask  import Flask,render_template, request

from conexao import conecta_db
from categoria import inserir, consultar

app = Flask(__name__)

@app.route('/')
def principal():
    nome = "Sistema de Vendas"
    return render_template("index.html",nome=nome)


@app.route("/categoria", methods=['GET','POST'])
def salvar_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir(conexao,nome)

        return f"<h2> Categoria Salva com Sucesso:  {nome} </h2>"
    return render_template("categoria_form.html")


@app.route("/listar-categorias", methods=['GET','POST'])
def listar_categorias():
    conexao = conecta_db()
    categorias = consultar(conexao)
    return render_template("categoria_listar.html",categorias=categorias)


if __name__ == '__main__':
    app.run(debug=True)