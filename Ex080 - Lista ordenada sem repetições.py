lista = []
# for c in range(0, 5):
#     numero = int(input('Digite um valor: '))
#     lista.append(numero)
#     lista.sort()
#     print(f'Adicionado na posição {lista.index(numero)} da lista...')
# print(f'Os valores digitados em ordem foram {lista}')
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print(f'Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
