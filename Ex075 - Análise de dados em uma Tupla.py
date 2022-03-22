num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
pares = []

print(f'O número 9 aparaceu {tupla.count(9)} vezes')
print(f'O número {tupla[1]} aparece na 2º posição.')
for n in tupla:
    if n % 2 == 0:
        pares.append(n)
print(f'Os números pares digitados são', end=' ')
for p in pares:
    print(p, end=', ')
