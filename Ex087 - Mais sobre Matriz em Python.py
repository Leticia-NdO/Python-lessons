matriz = [[], [], []]
pares = []
for c in range(0, 3):
    num = int(input(f'Digite um valor para [0,{c}]: '))
    matriz[0].append(num)
    if num % 2 == 0:
        pares.append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para [1,{c}]: '))
    matriz[1].append(num)
    if num % 2 == 0:
        pares.append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para[2,{c}]: '))
    matriz[2].append(num)
    if num % 2 == 0:
        pares.append(num)
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('-='*30)
print(f'A soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
