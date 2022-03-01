caro = count = total = menor = menor_custo = 0
while True:
    print('-='*15)
    print(' '*5, 'LOJA SUPER BARATÃO', ' '*5)
    print('-=' * 15)
    produto = str(input('Nome do Produto: ')).strip().title()
    preço = float(input('Preço: '))
    total += preço
    count += 1
    if preço > 1000:
        caro += 1
    if count == 1:
        menor = produto
        menor_custo = preço
    elif count > 1:
        if preço < menor_custo:
            menor = produto
            menor_custo = preço
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    if sn == 'N':
        break
print('-'*5, 'FIM DO PROGRAMA', '-'*5)
print(f'O total de compra foi de R$ {total:.2f}')
if caro == 1:
    print(f'Temos apenas um produto custando mais de R$ 1000.00')
else:
    print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {menor} que custa R$ {menor_custo:.2f}')
