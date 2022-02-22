count = 0
n = int(input('Digite um número: '))  # o programa deve contar de 10 até n e dizer se o número é primo ou não.
for c in range(1, n + 1):  #
    print(c, end=' ')
    if n % c == 0:
        count += 1
if count == 2:
    print(f'\nO número {n} foi divisível 2 vezes\nE por isso ele é PRIMO!')
else:
    print(f'\nO número {n} foi divisível {count} vezes\nE por isso ele NÃO É PRIMO!')
\033[m