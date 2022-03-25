from random import randint
from time import sleep
lista = []
print('SORTEANDO 5 VALORES: ', end=' ')
for c in range(0, 5):
    lista.append(randint(0, 10))
for c in range(0, 5):
    print(lista[c], end=' ')
    sleep(0.5)


def somapar(lst):
    soma = 0
    for c in range(0, len(lst)):
        if lst[c] % 2 == 0:
            soma += lst[c]

    print(soma)


print(f'\nSomando os valores pares de {lista}, temos ', end=' ')

somapar(lista)
