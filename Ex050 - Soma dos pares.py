s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
if cont > 1:
    print(f'A soma entre os {cont} números pares digitados é {s}')
elif cont == 1:
    print(f'O único número par digitado foi {s}')
else:
    print('Nenhum número par foi digitado.')
