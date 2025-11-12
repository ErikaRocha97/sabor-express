# importar biblioteca
import os

print('''Sabor Express
''')

print('1. Cadastrar restaurante')
print('2. Listar restaurantes')
print('3. Ativar restaurante')  
print('4. Sair\n')

# não precisa definir tipo
# padrao de nomeclatura: snake_case (variáveis, funções e métodos)
# Aceita aspas duplas ou simples

opcao_escolhida = int(input('Escolha uma opção: '))

# por padrão o input recebe uma string
# print(type(opcao_escolhida))

# definir função

def finalizar_app():
    # os.system('clear') no mac
    os.system('cls')    
    print('Finalizando o aplicativo')    

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else: 
    finalizar_app()

