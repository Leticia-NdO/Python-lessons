jogador = {}
time = []
count = 0
while True:
    jogador['Gols'] = []
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, jogador['Partidas']):
        jogador['Gols'].append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Total'] = sum(jogador['Gols'])
    time.append(jogador.copy())
    jogador.clear()
    count += 1
    res = str(input('Quer continuar? [S/N]')).upper()
    if res == 'N':
        break

print('-='*30)
print(f'cód, nome, gols, total')
print('-='*30)
for c in range(0, count):
    print(f'{c}', f'{time[c]["Nome"]}', f'{time[c]["Gols"]}', f'{time[c]["Total"]}')
while True:
    print('-=' * 30)
    show = int(input('Mostrar dados de qual jogador? [999 interrompe]: '))
    while show >= count or show < 0:
        print('Por favor, digite um número válido.')
        show = int(input('Mostrar dados de qual jogador? [999 interrompe]: '))
    if show == 999:
        break
    else:
        print(f'Levantamento do jogador {time[show]["Nome"]}')
        for e in range(0, time[show]['Partidas']):
            print(f'No jogo {e+1} fez {time[show]["Gols"][e]} gols.')
print('VOLTE SEMPRE')
