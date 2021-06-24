import sqlite3

#Constantes para guardar os comandos
CREATE_TABLE = "CREATE TABLE linguagens(id integer primary key, nome TEXT, criador TEXT, ano INTEGER)"
INSERT_LINGUAGENS = "INSERT INTO linguagens (nome, criador, ano) values(?, ?, ?)"
BUSCA_LINGUAGENS = "SELECT * from linguagens;"
BUSCA_LING_NOME = "SELECT * from linguagens where nome = ?;"
BUSCA_LING_ANTIGA = """
SELECT * from linguagens
order by ano asc
limit 1
"""
#Metodo antigo de criar o banco
#conexao = sqlite3.connect("linguagens.db")

#Metódo antigo de criar a tabela
#with conexao:
#    conexao.execute(
#        "CREATE TABLE linguagens(id integer primary key, nome TEXT, criador TEXT, ano INTEGER)"
#    )

#Função que cria o BD
def conect():
    return sqlite3.connect("linguagens.db")

#Função que cria a tabela
def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

#Função de inserir dados
def add_linguagens(conexao, nome, criador, ano):
    with conexao:
        conexao.execute(INSERT_LINGUAGENS, (nome, criador, ano))

#Função para Busca simples
def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_LINGUAGENS).fetchall()

#Função para Busca com algum filtro
def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_LING_NOME, (nome,)).fetchall()

#Função para buscar a linguagem mais antiga
def busca_antiga(conexao):
    with conexao:
        return conexao.execute(BUSCA_LING_ANTIGA).fetchone()