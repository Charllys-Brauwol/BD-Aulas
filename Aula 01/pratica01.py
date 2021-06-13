#Prática 01 - crie uma tabela com pelo menos 02 campos
import sqlite3
conexao = sqlite3.connect("time.db")

cursor = conexao.cursor()

#cursor.execute(
#    '''
#    CREATE TABLE time(
#        nome TEXT,
#        ano INTEGER
#    )
#    '''
#)

# Prática 02 - Inserir registros

cursor.execute(
    '''
    INSERT INTO time(nome, ano) VALUES(?,?)
    ''', ("Corinthians", 1910)    
)

conexao.commit()
cursor.close()
conexao.close()