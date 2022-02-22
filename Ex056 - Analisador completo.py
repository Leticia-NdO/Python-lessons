soma = 0
m = 0
homi = 0
muie = 0
velho = 0
nome_velho = ''
for c in range(1, 5):
    print('-'*5, f'{c}ª PESSOA', '-'*5)

    nome = str(input('Nome: ')).strip().title()       # inserção das informações
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    if c == 1:
        soma = idade            # a idade da primeira pessoa será a idade total do grupo.
    if c > 1:                   # a partir da segunda pessoa, a soma serão as idades anteriores mais a que o computador
        soma += idade           # tá analisando.

    if c == 1:
        velho = idade           # a primeira pessoa será a mais nova e a mais velha do grupo ao mesmo tempo.
    else:                       # a partir da segunda, o programa comparará com os valores anteriores para verificar se
        if idade > velho:       # é o indivíduo mais velho.
            velho = idade
            if sexo == 'M':        # se o indivíduo mais velho for masculino, o nome dessa pessoa vira nome_velho.
                homi += 1
                nome_velho = nome
            else:
                muie += 1          # se o indivíduo mais velho for feminino, o nome dessa pessoa vira nome_velho.
                nome_velho = nome

    if sexo == 'F' and idade < 20:
        m += 1
print('+='*30)
print(f'A média de idade do grupo é de {soma/4} anos.')

if homi > muie:
    print(f'O homem mais velho tem {velho} anos e se chama {nome_velho}')
if muie > homi:
    print(f'A mulher mais velha do grupo tem {velho} anos e se chama {nome_velho}')

if m > 1:
    print(f'Ao todo são {m} mulheres com menos de 20 anos.')
elif m == 1:
    print(f'O grupo possui apenas 1 mulher com menos de 20 anos')
