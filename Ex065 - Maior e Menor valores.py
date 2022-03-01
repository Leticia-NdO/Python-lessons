soma = num = count = maior = menor = 0
quer = ''
while quer != 'N':
    num = int(input('Digite um número: '))
    quer = str(input('Quer continuar? [S/N] ')).upper().strip()
    soma += num
    count += 1
    if quer != 'S' and quer != 'N':
        print('Por favor, insira uma opção válida.')
        quer = str(input('Quer continuar? [S/N] ')).upper().strip()
    if count == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
if quer == 'N' and count > 1:
    print(f'Você digitou {count} números e a média foi {soma/count}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')
else:
    print(f'Você digitou apenas o número {soma}.')
