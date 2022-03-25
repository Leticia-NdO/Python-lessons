def jogador(n='', g='' or 0):
    if n == '':
        n = '<desconhecido>'
    if g == '':
        g = 0
    print(f'O jogador {n.capitalize()} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = input('Número de gols: ')
jogador(nome, gols)
