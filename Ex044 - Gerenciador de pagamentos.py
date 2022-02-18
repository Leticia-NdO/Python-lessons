compras = float(input('Preço das compras: R$ '))
op = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (máx. de 12 parcelas)
Digite a opção: '''))
if op == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compras, 0.9*compras))
elif op == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(compras, 0.95*compras))
elif op == 3:
    print('Sua compra será parcelada em 2 vezes de {}, sem juros.'.format(compras/2))
elif op == 4:
    parcelas = int(input('Insira o número de parcelas: '))
    if 3 < parcelas < 12:
        print('''Sua compra será parcelada em {} vezes de R$ {:.2f} com juros. 
Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'''.format(parcelas, (1.2*compras)/parcelas, compras, 1.2*compras)
              )
    else:
        print('Por favor, insira uma quantidade de parcelas válida.')
else:
    print('Por favor, digite uma opção válida.')
