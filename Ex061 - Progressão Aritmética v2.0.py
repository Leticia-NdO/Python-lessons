print('Gerador de PA')
print('+='*20)
primo = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
d = int(input('Informe o número de termos: '))
c = primo + d*r
while primo < c:
    print(primo, end=' → ')
    primo += r
print('Fim')

print('')

'''[ALTERNATIVA SEM FÓRMULA]'''
print('Gerador de PA')
print('+='*20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
count = 0
while count <= 9:
    print(termo, end=' → ')
    termo += razão
    count += 1
print('Fim')
