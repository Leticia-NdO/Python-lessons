print('*='*20)
print('Sequência de Fibinacci')
print('*='*20)
termos = int(input('Quantos termos você deseja visualizar? '))
count = 3
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end=' → ')
while termos >= count:
    t3 = t1 + t2
    print(f'{t3}', end=' → ')
    t1 = t2
    t2 = t3
    count += 1
print('Fim')
