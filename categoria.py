from conexao import conecta_db

# DML = Linguagem de manipulação de Dados
#CRUD => Create, Read, Update , Delete
#        INSERT, SELECT , UPDATE, DELETE 


# DDL = Linguagem de Criação de tabelas
#  Create table 
#  DROP table
#  Alter table 

def consultar(conexao):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria order by id asc")
    registros = cursor.fetchall()
    return registros


def inserir(conexao, nome):
    cursor = conexao.cursor()
    sql_insert = "insert into categoria (nome) values ('"+ nome +  "')"
    cursor.execute(sql_insert)
    conexao.commit()
        
def alterar(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    nome_categoria = input('Digite o nome da categoria: ')
    sql_update = "update categoria set nome ='" + nome_categoria + "' where id = " + id
    cursor.execute(sql_update)
    conexao.commit()


def deletar(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from  categoria where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()
