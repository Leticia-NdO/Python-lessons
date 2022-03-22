from random import randint
num = randint(0, 11)
num2 = randint(0, 11)
num3 = randint(0, 11)
num4 = randint(0, 11)
num5 = randint(0, 11)
tupla = (num, num2, num3, num4, num5)
print('Os valores sorteados foram: ', end=' ')
for n in tupla:
    print(n, end=' ')
print(f'\nO menor valor sorteado foi {min(tupla)}.\nE o maior valor sorteado foi {max(tupla)}.')
