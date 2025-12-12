from flask  import Flask,render_template, request, redirect,url_for

from conexao import conecta_db
from categoria_bd import inserir_categoria, consultar_categoria, deletar_categoria_bd
from cliente_bd import inserir_cliente, listar_clientes_bd
from produto_db import listar_produtos_bd, inserir_produto_bd
from usuario_bd import inserir_usuario_bd, listar_usuarios_bd, deletar_usuario_db

app = Flask(__name__)

@app.route('/home')
def home():
    nome = "Sistema de Vendas"
    return render_template("home.html",nome=nome)



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Valida campos obrigatórios; ajuste aqui para autenticar de verdade
        if not usuario or not senha:
            erro = "Preencha usuário e senha para entrar."
            return render_template("login.html", erro=erro)

        return redirect(url_for('home'))

    return render_template("login.html")


@app.route("/clientes/novo", methods=['GET','POST'])
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


@app.route("/categorias/novo", methods=['GET','POST'])
def salvar_categoria():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_categoria(conexao,nome)

        return f"<h2> Categoria Salva com Sucesso:  {nome} </h2>"
    return render_template("categoria_form.html", titulo="Cadastro de Categoria")

@app.route("/usuarios/novo", methods=['GET','POST'])
def salvar_usuario():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        if not login and senha:
            return "<h3> Por favor, preencha todos os campos</h3"
        
        conexao = conecta_db()
        inserir_usuario_bd(conexao,login,senha,'S')
        return f"<h2> Usuário Salvo com Sucesso:  {login} </h2>"
    return render_template("usuario_form.html",titulo ="Cadastro de Usuário")


@app.route("/usuarios/listar", methods=['GET','POST'])
def usuario_listar():
    conexao = conecta_db()
    usuarios = listar_usuarios_bd(conexao)
    return render_template("usuario_listar.html",usuarios=usuarios)

@app.route("/categorias/listar", methods=['GET','POST'])
def categoria_listar():
    conexao = conecta_db()
    categorias = consultar_categoria(conexao)
    return render_template("categoria_listar.html",categorias=categorias)


@app.route("/clientes/listar", methods=['GET','POST'])
def cliente_listar():
    conexao = conecta_db()
    clientes = listar_clientes_bd(conexao)
    return render_template("cliente_listar.html",clientes=clientes)


@app.route("/produtos/listar", methods=['GET','POST'])
def produto_listar():
    conexao = conecta_db()
    produtos = listar_produtos_bd(conexao)
    return render_template("produto_listar.html",produtos=produtos)


@app.route("/produtos/novo", methods=['GET','POST'])
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
    return render_template("produto_form.html", titulo ="Cadastro de Produto")



@app.route('/categorias/<int:id>/editar', methods=['GET', 'POST']) 
def categorias_editar(id):    
    return redirect(url_for('categorias_listar'))

@app.route('/categorias/<int:id>/excluir', methods=['POST'])
def categorias_excluir(id):
    conexao = conecta_db()
    deletar_categoria_bd(conexao, id)
    return redirect(url_for('categoria_listar'))

@app.route('/usuarios/<int:id>/excluir', methods=['POST'])
def usuarios_excluir(id):
    conexao = conecta_db()
    deletar_usuario_db(conexao,id)
    return redirect(url_for('usuario_listar'))


if __name__ == '__main__':
    app.run(debug=True)
