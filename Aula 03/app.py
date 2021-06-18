import data

def menu():
    conexao = data.conect()
    data.create(conexao)

menu()