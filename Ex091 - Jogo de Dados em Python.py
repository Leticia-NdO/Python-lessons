from random import randint
from time import sleep
from operator import itemgetter
dados = {}
ranking = {}
print('Valores sorteados: ')
dados['Jogador1'] = randint(0, 7)
dados['Jogador2'] = randint(0, 7)
dados['Jogador3'] = randint(0, 7)
dados['Jogador4'] = randint(0, 7)
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('O ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)