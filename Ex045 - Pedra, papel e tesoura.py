import time
import random

jog = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA 
Qual é a sua jogada? '''))
if jog > 2:
    print('JOGADA INVÁLIDA')
else:
    if jog == 0:                            # atribuição de valores da tabela
        jog = 'Pedra'
    if jog == 1:
        jog = 'Papel'
    if jog == 2:
        jog = 'Tesoura'
    lista = ['Pedra', 'Papel', 'Tesoura']

    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!!!')
    time.sleep(0.5)
    print('-='*20)
    comp = random.choice(lista)
    print('Computador jogou {}'.format(comp))
    print('Jogador jogou {}'.format(jog))
    print('-='*20)

    if comp == 'Papel' and jog == 'Tesoura' or jog == 'Pedra' and comp == 'Tesoura' or jog == 'Papel' and \
            comp == 'Pedra':
        print('JOGADOR VENCE!')
    elif comp == 'Tesoura' and jog == 'Papel' or comp == 'Pedra' and jog == 'Tesoura' or comp == 'Papel' and \
            jog == 'Pedra':
        print('COMPUTADOR VENCE!')
    else:
        print('EMPATE!')
