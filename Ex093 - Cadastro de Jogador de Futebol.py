jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, jogador['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
for i, v in enumerate(gols):
    print(f'Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {jogador["Total"]} gols')
