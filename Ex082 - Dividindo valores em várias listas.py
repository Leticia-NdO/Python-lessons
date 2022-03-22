lista = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    resp = str(input('Quer continuar? [S/N] ')).upper()
    while resp not in 'SN':
        print('Por favor, digite uma opção válida.')
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
