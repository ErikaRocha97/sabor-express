# não precisa definir tipo
# padrao de nomeclatura: snake_case (variáveis, funções e métodos)
# Aceita aspas duplas ou simples

# importar biblioteca
import os

# definir funções
def exibir_nome_do_programa():
    print('''Sabor Express
    ''')

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')  
    print('4. Sair\n')

def finalizar_app():
    # os.system('clear') no mac
    os.system('cls')    
    print('Aplicativo finalizado')  

def opcao_invalida():
    print('Opção inválida!\n')
    input('Pressione enter para voltar ao menu principal.')
    main()

# por padrão o input recebe uma string
# print(type(opcao_escolhida))

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                print('Adicionar restaurante')
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

# definir como programa principal

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()