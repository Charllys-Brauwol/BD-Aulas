#importa o arquivo
import data

MENU_PROMPT = """
1)Adicionar Linguagem
2)Ver todas Linguagens
3)Buscar Linguagem por Nome
4)Buscar Linguagem mais antiga
5)Sair
"""

def menu():
    conexao = data.conect()
    #1data.create(conexao)

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            nome = input("Diga o nome da linguagem:")
            criador = input("Diga o nome do criador:")
            ano = int(input("Diga o ano da criação:"))

            #conexão com o BD
            data.add_linguagens(conexao, nome, criador, ano)
        
        elif user_input == "2":
            linguagens = data.busca(conexao)

            for linguagem in linguagens:
                print(f"{linguagem[1]} {linguagem[2]} {linguagem[3]}")
        
        elif user_input == "3":
            nome = input("Digite o nome do criador para buscar:")
            linguagens = data.BUSCA_LING_NOME(conexao, nome)
        
            for linguagem in linguagens:
                print(f"{linguagem[1]} {linguagem[2]} {linguagem[3]}")
        
        elif user_input == "4":
            antiga = data.BUSCA_LING_ANTIGA(conexao)

            print(f'''
            A linguagem mais antiga é: {antiga[1]}
            Criada por {antiga[2]} em {antiga[3]}
            ''')

        elif user_input == "5":
            exit()
        else:
            print("Entrada Inválida")

menu()