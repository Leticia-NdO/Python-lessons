num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão: ')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual à {}'.format(num, bin(num)[2:]))  # esse fatiamento é pra tirar umas
    # indexações que o pycharm coloca, como Ob na frente de cada número binário.
elif op == 2:
    print('{} convertido para OCTAL é igual à {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual à {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
