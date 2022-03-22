pessoa = {}
banco = []
count = 0
média = 0
mulheres = []
velhos = [{}]
while True:
    pessoa['Nome'] = str(input('Nome: ')).capitalize()
    pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()
    count += 1
    while pessoa['Sexo'] not in 'MF':
        del pessoa['Sexo']
        print('Por favor, digite um valor válido.')
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()
    pessoa['Idade'] = int(input('Idade: '))
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'])
    banco.append(pessoa.copy())
    pessoa.clear()
    res = str(input('Quer continuar? [S/N] ')).upper()
    while res not in 'SN':
        print('Por favor, digite um valor válido.')
        res = str(input('Quer continuar? [S/N] ')).upper()
    if res == 'N':
        break

print(banco[0]['Idade'])
print('-='*30)
print(f'A) Ao todo, temos {count} pessoas cadastradas.')
for c in range(0, count):
    média += banco[c]['Idade']
print(f'B) A média de idade é de {média/count:.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for c in range(0, len(mulheres)):
    print(mulheres[c], end='... ')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
for c in range(0, len(banco)):
    if banco[c]['Idade'] >= média/count:
        for k, v in banco[c].items():
            print(f'{k} == {v}', end='; ')
        print()
print('\n<<< ENCERRADO >>>')
