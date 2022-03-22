lista = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    res = str(input('Quer continuar? [S/N] ')).upper()
    while res not in 'SN':
        print('Por favor, digite uma opção válida.')
        res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista :(')
