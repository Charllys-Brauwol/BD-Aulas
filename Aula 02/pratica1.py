#importa BD
from os import name
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

#Fazer uma busca com o que o usuário digitar
        nome = input("Digite o nome que irá ser buscado:")
        cursor.execute("SELECT * from agenda2 where nome = ?", (nome,))
        #Traz o resultado em formato de tupla
        while True:
            resultado = cursor.fetchone()
            #para o código se não achar
            if resultado is None:
                print("Não existe!")
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
#conexao.commit()