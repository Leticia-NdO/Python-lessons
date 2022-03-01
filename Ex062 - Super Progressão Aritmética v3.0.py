print('Gerador de PA')
print('+='*20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
count = 0
total = 0
mais = int(input('Número de termos: '))
while mais != 0:
    total += mais
    while count <= total:
        print(termo, end=' → ')
        termo += razão
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja visualizar? '))
print(f'Consulta encerrada após {count-1} termos consultados.')
print('Fim')
