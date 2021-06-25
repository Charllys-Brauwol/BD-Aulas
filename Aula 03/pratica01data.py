#Prática01 - Reescreva o código da criação do banco Agenda,
#de forma que os comandos SQL fiquem guardados em constantes
#e essas constantes sejam invocadas por funções. As funções
#devem ficar em um arquivo e os comandos que chamam
#essas funções devem ficar em outro.

import sqlite3

#Constantes para guardar os comandos
CREATE_TABLE = "CREATE TABLE agenda(id integer primary key, nome TEXT, telefone TEXT)"
INSERT_CONTATOS = "INSERT INTO agenda (nome, telefone) values(?, ?)"
BUSCA_TODOS_CONTATOS = "SELECT * from agenda;"
BUSCA_CONTATO_NOME = "SELECT * from agenda where nome = ?;"

#Função que cria o BD
def conect():
    return sqlite3.connect("agenda.db")

#Função que cria a tabela
def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

#Função de inserir dados
def add_contatos(conexao, nome, telefone):
    with conexao:
        conexao.execute(INSERT_CONTATOS, (nome, telefone))

#Função para Busca simples
def busca(conexao):
    with conexao:
        return conexao.execute(BUSCA_TODOS_CONTATOS).fetchall()

#Função para Busca com algum filtro
def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_CONTATO_NOME, (nome,)).fetchall()
