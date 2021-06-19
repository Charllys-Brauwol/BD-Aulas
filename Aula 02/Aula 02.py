#importa BD
import sqlite3
#Fecha BD automaticamente
from contextlib import closing

#inserindo dados de uma vez
dados = [
    ("João", 123234),
    ("Carlos", 197),
    ("Patricia", 564456)
]

with sqlite3.connect("agenda2.db") as conexao:
    #Fecha cursor automaticamente
    with closing(conexao.cursor()) as cursor:
#Criando tabela
#        cursor.execute(
#            '''
#            CREATE TABLE agenda2(
#                nome TEXT,
#                telefone INTEGER
#            )
#            '''
#        )

#inserindo dados
#        cursor.executemany(
#            '''
#            INSERT INTO agenda2(nome, telefone) values(?,?)
#            ''', (dados)
#        )

#Estrutura de Busca com condição, filtro, where = onde
#        cursor.execute("SELECT * from agenda2 where nome = 'Patricia'")
#        #Traz o resultado em formato de tupla
#        while True:
#            resultado = cursor.fetchone()
#            #para o código se não achar
#            if resultado is None:
#                break
#            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")

#Alterações no BD
#        cursor.execute(
#            '''
#            UPDATE agenda2
#            SET telefone = 1111111
#            WHERE nome = 'Patricia'
#            '''
#        )

#Deletar dados do BD
        cursor.execute(
            '''
            DELETE from agenda2 
            WHERE nome = 'Patricia'
            '''
        )
        #rowcount conta quantidade de dados digitados
        print("Dados deletados: ", cursor.rowcount)
        #Condicional para não excluir todos dados com nomes iguais, mas só um registro
        if cursor.rowcount == 2:
            conexao.commit()
            print("Alteração feita!")
        else:
            conexao.rollback()
            print("Operação Perigosa Não Executada!")
#conexao.commit()