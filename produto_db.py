from conexao import conecta_db


def listar_produtos_bd(conexao):
    cursor = conexao.cursor()
    # Execução do Select no banco de dados
    cursor.execute(" select p.id, p.nome, p.valor_venda, p.estoque, categoria.nome from produto p " +
                   " inner join categoria on (p.categoria_id = categoria.id)")
    # recuperar todos registros
    registros = cursor.fetchall()
    return registros


def inserir_produto_bd(conexao,nome,valor_venda,estoque,categoria_id):
    cursor = conexao.cursor()
    sql_insert = "insert into produto (nome, valor_venda, estoque, categoria_id) values (%s, %s, %s, %s)"
    dados   = (nome, valor_venda, estoque, categoria_id)
    cursor.execute(sql_insert, dados)
    conexao.commit()


def alterar_produto_bd(conexao,id,nome,valor_venda,estoque,categoria_id):
    cursor = conexao.cursor()
    sql_update = "update produto set nome= %s, valor_venda = %s, estoque = %s, categoria_id= %s where id = %s"
    dados   = (nome, valor_venda, estoque,categoria_id, id)
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar_produto_bd(conexao,id):
    cursor = conexao.cursor()
    sql_delete = "delete from  produto where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()