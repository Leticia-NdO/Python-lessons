print('='*30)
print(' '*5, 'BANCO CEV', ' '*5)
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
if valor > 50:
    print(f'Total de {valor//50} cédulas de R$ 50')
    if valor % 50 >= 10:
        print(f'Total de {(valor % 50)//10} cédulas de R$ 10')
        if ((valor % 50) % 10) >= 1:
            print(f'Total de {((valor % 50)%10)//1} cédulas de R$ 1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
