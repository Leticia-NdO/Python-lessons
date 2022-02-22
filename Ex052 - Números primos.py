count = 0
n = int(input('Digite um número: '))  # o programa deve contar de 10 até n e dizer se o número é primo ou não.
for c in range(1, n + 1):  # se eu quiser printar c, o último número não aparece, então pra n aparecer tenho que colocar
    if n % c == 0:         # um a mais.
        print('\033[31m', end='')  # se n for divisível por c, colore de vermelho e conta ele.
        count += 1
    else:
        print('\033[m', end='')  # se n não for divisível por c, limpa a coloração e não conta ele.
    print(c, end=' ')
if count == 2:
    print(f'\033[m\nO número {n} foi divisível 2 vezes\nE por isso ele é PRIMO!')
else:
    print(f'\033[m\nO número {n} foi divisível {count} vezes\nE por isso ele NÃO É PRIMO!')
