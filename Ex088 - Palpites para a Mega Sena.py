from random import randint
from time import sleep
jogo = []
print('-='*22)
print(' '*6, 'GERADOR DE JOGOS DA MEGA SENA', ' '*5)
print('-='*22)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print('<'*5, f'Sorteando {qtd} jogos', '>'*5)
for j in range(0, qtd):
    for c in range(0, 6):
        num = randint(0, 61)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    print(f'Jogo {j+1}: {jogo}')
    jogo.clear()
    sleep(0.5)
print('-='*8, 'BOA SORTE!', '-='*8)
