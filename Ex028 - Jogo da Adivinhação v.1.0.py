import random
print('O computador pensará em um número de 0 à 5')
lista = [0, 1, 2, 3, 4, 5]
n = int(random.choice(lista))
u = int(input('Qual número eu pensei? '))
if u == n:
    print('Parabéns! Você ganhou!')
else:
    print('Resposta:', n)
    print('Você errou. Vitória do computador!')

'''[ALTERNATIVA 1]'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('O computador pensará em um número de 0 à 5')
jogador = int(input('Que número o computador pensou? '))
print('PROCESSANDO...')
sleep(3)  # esse comando faz com que demore n segundos para o comando seja executado.
if jogador == computador:
    print('Parabéns! Você ganhou!')
else:
    print('Resposta:', computador)
    print('Você errou. Vitória do computador!')
