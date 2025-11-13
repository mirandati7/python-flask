from flask  import Flask,render_template, request

from conexao import conecta_db
from categoria_bd import inserir_categoria, consultar_categoria
from cliente_bd import inserir_cliente, listar_clientes_bd
from produto_db import listar_produtos_bd, inserir_produto_bd

app = Flask(__name__)

@app.route('/')
def principal():
    nome = "Sistema de Vendas"
    return render_template("index.html",nome=nome)


@app.route("/cliente", methods=['GET','POST'])
def salvar_cliente():
    if request.method == 'POST':
        nome = request.form.get('nome')
        celular = request.form.get('celular')
        email = request.form.get('email')
        cpf_cnpj = request.form.get('cpf_cnpj')

        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_cliente(conexao,nome,celular,email,cpf_cnpj)

        return f"<h2> Cliente Salvo com Sucesso:  {nome} </h2>"
    return render_template("cliente_form.html")


@app.route("/categoria", methods=['GET','POST'])
def salvar_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_categoria(conexao,nome)

        return f"<h2> Categoria Salva com Sucesso:  {nome} </h2>"
    return render_template("categoria_form.html")


@app.route("/listar-categorias", methods=['GET','POST'])
def listar_categorias():
    conexao = conecta_db()
    categorias = consultar_categoria(conexao)
    return render_template("categoria_listar.html",categorias=categorias)


@app.route("/listar-clientes", methods=['GET','POST'])
def listar_clientes():
    conexao = conecta_db()
    clientes = listar_clientes_bd(conexao)
    return render_template("cliente_listar.html",clientes=clientes)


@app.route("/listar-produtos", methods=['GET','POST'])
def listar_produtos():
    conexao = conecta_db()
    produtos = listar_produtos_bd(conexao)
    return render_template("produto_listar.html",produtos=produtos)


@app.route("/produto", methods=['GET','POST'])
def salvar_produto():
    if request.method == 'POST':
        nome = request.form.get('nome')
        preco = request.form.get('preco')
        estoque = request.form.get('estoque')
        id_categoria = request.form.get('id_categoria')

        if not nome and not preco:
            return "<h3> Por favor, preencha os campos obrigatório</h3"
        
        conexao = conecta_db()
        inserir_produto_bd(conexao,nome,preco,estoque,id_categoria)

        return f"<h2> Produto Salvo com Sucesso:  {nome} </h2>"
    return render_template("produto_form.html")



if __name__ == '__main__':
    app.run(debug=True)