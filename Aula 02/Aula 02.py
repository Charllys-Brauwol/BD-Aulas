#importa BD
import sqlite3
#Fecha BD automaticamente
from contextlib import closing

#inserindo dados de uma vez
dados = [
    ("João", 123-234),
    ("Carlos", 1-97),
    ("Patricia", 564-456)
]

with sqlite3.connect("agenda2.db") as conexao:
    #Fecha cursor automaticamente
    with closing(conexao.cursor()) as cursor:
#        cursor.execute(
#            '''
#            CREATE TABLE agenda2(
#                nome TEXT,
#                telefone INTERGER
#            )
#            '''
#        )

#inserindo dados
        cursor.executemany(
            '''
            INSERT INTO agenda2(nome, telefone) values(?,?)
            ''', (dados)
        )

conexao.commit()