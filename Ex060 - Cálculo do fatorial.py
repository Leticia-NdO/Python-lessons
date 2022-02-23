import math
numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = math.factorial(numero)
print(f'Calculando {numero}! =', end=' ')
while numero > 1:
    print(numero, 'x', end=' ')
    numero -= 1
print('1 =', fatorial)

'''[ALTERNATIVA 1 - USANDO O FOR]'''

print('+'*20)
n = int(input('Digite um número para calcular seu fatorial: '))
c = math.factorial(n)
print(f'Calculando {n}! =', end=' ')
for f in range(n, 0, -1):
    print(f, end='')
    print(' x ' if f > 1 else ' = ', end='')
print(c)
