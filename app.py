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
    print('Finalizando o aplicativo')  

# por padrão o input recebe uma string
# print(type(opcao_escolhida))

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else: 
        finalizar_app()

# definir como programa principal

def main():
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()