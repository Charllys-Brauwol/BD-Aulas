import sqlite3
from contextlib import closing
from sqlite3.dbapi2 import Cursor

dados = [
    ["Ceará", 85], ["SP", 11], ["Ceará-FORT", 88]
]

with sqlite3.connect("ddd.db") as conexao:
    #Retorno mais organizado da lista
    conexao.row_factory = sqlite3.Row
    print(f"{'id':3s} {'Estado':20s} {'DDD':5s}")
    print("="*37)
    for ddd in conexao.execute("SELECT * from ddd order by ddd"):
        print(f"{ddd['id']:3d} {ddd['nome']:20s} {ddd['ddd']:5d}")
#    with closing (conexao.cursor()) as cursor:
        #criando um bd com id auto-incrementado 
#        cursor.execute(
#            '''
#            CREATE TABLE ddd(
#                id INTEGER PRIMARY KEY autoincrement, 
#                nome TEXT,
#                ddd INTEGER
#            )
#            '''
#        )
#
#        cursor.executemany(
#            '''
#            INSERT INTO ddd(nome, ddd) values (?, ?)
#            ''', dados
#            
#        )
#conexao.commit()