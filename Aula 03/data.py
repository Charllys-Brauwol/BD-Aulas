import sqlite3
CREATE_TABLE = "CREATE TABLE linguagens(id integer primary key, nome TEXT, criador TEXT, ano INTEGER)"
INSERT_LINGUAGENS = "INSERT INTO linguagens (nome, criador, ano) values(?, ?, ?)"
BUSCA_LINGUAGENS = "SELECT * from linguagens"

#conexao = sqlite3.connect("linguagens.db")

#Metódo que usavamos
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

def add_linguagens(conexao, nome, criador, ano):
    with conexao:
        conexao.execute(INSERT_LINGUAGENS, (nome, criador, ano))
