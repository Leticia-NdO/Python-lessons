soma = count = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    count += 1
if count == 1:
    print(f'Você digitou apenas o número {soma}.')
else:
    print(f'Você digitou {count} números e a soma deles é igual à {soma}')
