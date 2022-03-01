count = homem = mulher = 0
while True:
    print('-='*15)
    print('CADASTRE UMA PESSOA')
    print('-=' * 15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo != 'M' and sexo != 'F':
        print('Por favor, insira um valor válido.')
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idade > 18:
        count += 1
    elif idade < 18 and sexo == 'F':
        mulher += 1
    if sexo == 'M':
        homem += 1
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    if sn == 'N':
        break
print('-='*15)
print(f'Total de pessoas com mais de 18 anos: {count}')
if homem == 0:
    print('Temos apenas um homem cadastrado.')
else:
    print(f'Ao todo temos {homem} homens cadastrados')
if mulher == 0:
    print(f'E temos apenas uma mulher com menos de 20 anos.')
else:
    print(f'E temos {mulher} mulheres com menos de 20 anos.')