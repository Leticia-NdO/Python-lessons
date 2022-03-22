lista = []
dados = []
count = 0
while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    count += 1
    res = str(input('Quer continuar? [S/N] ')).upper()
    while res not in 'SN':
        print('Por favor, digite um valor válido.')
        res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        break
print('-='*15)
print(f'{"No":<7}{"NOME":<11}{"MÉDIA":>7 }')
print('-='*15)
for c in range(0, count):
    print(f'{c:<4}', f'{lista[c][0]:<10}', f'{(lista[c][1] + lista[c][2])/2:>8.1f}')
while True:
    show = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    while show >= count or show < 0:
        print('Por favor, digite um número válido.')
        show = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if show == 999:
        break
    else:
        print(f'Notas de {lista[show][0]}')
        print(f'Nota 1: {lista[show][1]}\nNota 2: {lista[show][2]}')
