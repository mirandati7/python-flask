from conexao import conecta_db

# DML = Linguagem de manipulação de Dados
#CRUD => Create, Read, Update , Delete
#        INSERT, SELECT , UPDATE, DELETE 


# DDL = Linguagem de Criação de tabelas
#  Create table 
#  DROP table
#  Alter table 

def consultar_categoria(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria order by id asc")
    registros = cursor.fetchall()
    return registros


def inserir_categoria(conexao, nome):
    cursor = conexao.cursor()
    sql_insert = "insert into categoria (nome) values ('"+ nome +  "')"
    cursor.execute(sql_insert)
    conexao.commit()
        
def alterar_categoria(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    nome_categoria = input('Digite o nome da categoria: ')
    sql_update = "update categoria set nome ='" + nome_categoria + "' where id = " + id
    cursor.execute(sql_update)
    conexao.commit()


def deletar_categoria_bd(conexao, id_categoria):
    cursor = conexao.cursor()    
    cursor.execute("DELETE FROM categoria WHERE id = %s", (id_categoria,))
    conexao.commit()
    cursor.close()
