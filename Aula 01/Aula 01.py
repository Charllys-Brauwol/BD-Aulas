
import sqlite3# informa qual BD está utilizando
conexao = sqlite3.connect("agenda.db") #a variável que cria coneção e o nome do BD

#Tupla de listas para facilitar a inserção de dados
#OBS: muda para cursor.executemany
dados = [
    ("Charllys", "111"),
    ("Amor", "112"),
    ("Zion", "114"),
    ("Zack", "411")
]

#criando cursor - objeto que vai se comunicar com o BD
#cursor - nome do objeto, conexao - metódo, da classe cursor
cursor = conexao.cursor()

#criando a tabela BD
#"cursor.execute(
#    '''
#    CREATE TABLE agenda(
#        nome TEXT,
#        telefone TEXT
#    )
#    '''
#)

#inserindo dados
#OBS: os ? são máscaras, para não dá erro de segurança
#cursor.executemany para pegar vários dados
#cursor.executemany(
#    '''
#    INSERT INTO agenda(nome, telefone) VALUES(?,?)
#    ''',(dados)
#)

#fzd uma busca pelo fetchone - Retorna apenas um resgistro
cursor.execute("SELECT * FROM agenda")
#resultado = cursor.fetchone()

#imprimindo busca
#print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")

#Faz busca por fatchall - todos dados
resultado = cursor.fetchall()
#loop na lista
for registro in resultado:
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")


conexao.commit() #modificando o BD
cursor.close() #Fechando o cursor 
conexao.close() #Fechado a conexão

#OBS: como a tabela está criada, tem que comentar a parte referente a isso
#para não criar outra tabela ou dar erro