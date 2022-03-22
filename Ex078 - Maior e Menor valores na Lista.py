lista = list()
maximos = list()
maior = 0
menor = 0
for n in range(0, 5):
    numero = int(input(f'Digite o valor para a Posição {n}: '))
    lista.append(numero)
    if n == 0:
        maior = numero
        menor = numero
    if n > 0:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print('-=' * 21)
print(f'Você digitou os valores {lista}')
if lista.count(max(lista)) == 1:
    print(f'O maior valor digitado foi {maior} na posição {lista.index(max(lista))}')
else:
    print(f'O maior valor digitado foi {maior} nas posições ', end=' ')
    for i, v in enumerate(lista):
        if v == maior:
            print(i, end='...')
if lista.count(min(lista)) == 1:
    print(f'\nO menor valor digitado foi {menor} na posição {lista.index(min(lista))}')
else:
    print(f'\nO menor valor digitado foi {menor} nas posições ', end=' ')
    for i, v in enumerate(lista):
        if v == menor:
            print(i, end='...')
