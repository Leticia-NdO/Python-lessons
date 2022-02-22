print("="*30)
print(' '*5+'10 TERMOS DE UMA PA'+' '*5)
print('='*30)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(f'{a1 + c*r}', end=' → ')
print('ACABOU')
