lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar!')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        break
    while res not in 'NS':
        print('Por favor, digite uma opção válida.')
        res = str(input('Quer continuar? [S/N] ')).upper()
print(f'Os valores digitados foram {sorted(lista)}')
