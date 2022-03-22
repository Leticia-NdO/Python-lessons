num = [2, 5, 9, 1]

num[2] = 3  # o elemento da posição 2 da lista agora é 3
print(num)

num.append(7)  # adicionar o 7 à lista
print(num)

num.sort(reverse=True)  # num organizada mas de forma invertida, ou seja, em ordem decrescente
print(num)

num.insert(2, 0)  # na posição 2 será inserido o número 0. Os números da posição 2 em diante serão jogados para frente
print(num)

num.pop()  # exclui o último valor da lista
print(num)

num.insert(2, 2)  # adicionei um novo número 2
print(num)   # lista com o 2 duplicado

num.remove(2)  # o método remove vai tirar o primeiro elemento daquele que ele quer remover.
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

valores = list(range(1, 11))  # o método list vai me dar uma lista com os valores de 1 à 11, lembrando que o último
# elemento não aparece, então vai só até o 10.
print(valores)

valores.append(11)
valores.append(12)
valores.append(13)
for c, v in enumerate(valores):  # o enumerate pega o valor do objeto e a sua posição.
    print(f'Na posição {c} temos o valor {v}')


lista = list()  # uma lista vazia
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)

a = [1, 2, 3]
# b = a  - > estou fazendo uma conexão entre a e b. Todas as mudanças que acontecerem com a acontecerão com b e
# viceversa
b = a[:]  # aqui eu digo que b recebe uma cópia de todos os valores contidos em a. Assim, as duas listas incialmente têm
# os mesmos valores, porém não estão ligadas

