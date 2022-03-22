lista = []
dados = []
count = 0
while True:
    dados.append(input('Nome: ').capitalize())
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    count += 1
    resp = str(input('Quer continuar? [S/N] ')).upper()
    while resp not in 'SN':
        print('Por favor, digite uma opção válida.')
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'Ao todo, você cadastrou {count} pessoas.')
peso = []
for c in range(len(lista)):
    peso.append(lista[c][1])
pesomax = max(peso)
pesomin = min(peso)
gordes = []
magres = []
for c in range(len(lista)):
    px = lista[c][1]
    if px == pesomax:
        gordes.append(lista[c][0])
    pm = lista[c][1]
    if pm == pesomin:
        magres.append(lista[c][0])
print(f'O maior peso foi de {pesomax} Kg. Peso de {gordes}')
print(f'O menor peso foi de {pesomin} Kg. Peso de {magres}')
