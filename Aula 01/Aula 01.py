
import sqlite3# informa qual BD está utilizando
conexao = sqlite3.connect("agenda.db") #a variável que cria coneção e o nome do BD

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
cursor.execute(
    '''
    INSERT INTO agenda(nome, telefone) VALUES(?,?)
    ''',("Evaldo", "123")
)

conexao.commit() #modificando o BD
cursor.close() #Fechando o cursor 
conexao.close() #Fechado a conexão

#OBS: como a tabela está criada, tem que comentar a parte referente a isso
#para não criar outra tabela ou dar erro