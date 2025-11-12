# imprimir com variáveis

nome = 'Erika'
idade = 28

# simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# %
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

# f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# parâmetro sep
print('A','L','U','R','A',sep='\n')

# imprimir valor de pi arredondado

pi = 3.14159

# f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# função round()
print('O valor arredondado de pi é:',round(pi,2))