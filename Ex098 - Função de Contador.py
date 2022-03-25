from time import sleep


def contador(i, f, p):
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.3)
    print('fim')


print('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1')
contador(1, 11, 1)

print(f'Contagem de 10 até 0 de 2 em 2')
contador(10, -1, -2)

print('Agora, é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

if f < 0 and p > 0:
    p = p*(-1)
if i > f:
    f -= 1
if f > i:
    f += 1
contador(i, f, p)
