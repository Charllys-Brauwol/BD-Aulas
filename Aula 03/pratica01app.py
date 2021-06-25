#Prática01 - Reescreva o código da criação do banco Agenda,
#de forma que os comandos SQL fiquem guardados em constantes
#e essas constantes sejam invocadas por funções. As funções
#devem ficar em um arquivo e os comandos que chamam
#essas funções devem ficar em outro.
#importa o arquivo
import pratica01data

MENU_PROMPT = """
1)Adicionar Contato
2)Todos os Contatos
3)Buscar Contato por Nome
5)Sair
"""

def menu():
    conexao = pratica01data.conect()
    #pratica01data.create(conexao)

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            nome = input("Diga o nome do Contato:")
            telefone = input("Diga o Telefone do Contato:")
            
            #conexão com o BD
            pratica01data.add_contatos(conexao, nome, telefone)
        
        elif user_input == "2":
            agenda = pratica01data.busca(conexao)

            for contato in agenda:
                print(f"{contato[1]} {contato[2]}")
        
        elif user_input == "3":
            nome = input("Digite o nome do contato:")
            agenda = pratica01data.busca_nome(conexao, nome)
        
            for contato in agenda:
                print(f'''
                Contato: {contato[1]}
                Telefone: {contato[2]}
                ''')
        
        elif user_input == "5":
            exit()
        else:
            print("Entrada Inválida")

menu()