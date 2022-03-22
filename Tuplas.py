# tupla é um dos três tipos de variáveis compostas: tuplas, listas e dicionários.
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')  # as tuplas são marcadas por parênteses.
jantar = ['arroz', 'feijão', 'frango']
jantar[2] = 'carne bovina'  # é possível mudar listas, mas é impossível fazer a mesma coisa com tuplas.
print(jantar)
print(lanche[0:3])
print(len(lanche))
for c in lanche:
    print(c, end=' ')
print('\n')
for cont in range(0, len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(f'Eu vou comer {comida}')
# se precisar da posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))  # esse comando não muda a tupla, apenas a exibe de uma forma organizada

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(c))
print(c.count(5))
print(sorted(c).index(8))

