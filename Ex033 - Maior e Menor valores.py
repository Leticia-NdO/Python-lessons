primo = int(input('Digite o primeiro valor: '))
seg = int(input('Digite o segundo valor: '))
terc = int(input('Digite o terceiro valor: '))

if primo > seg and primo > terc:
    print('O maior valor digitado foi', primo)
if seg > primo and seg > terc:
    print('O maior valor digitado foi', seg)
if terc > seg and terc > primo:
    print('O maior valor digitado foi', terc)
if primo < seg and primo < terc:
    print('O menor valor digitado foi', primo)
if seg < primo and seg < terc:
    print('O menor valor digitado foi', seg)
if terc < seg and terc < primo:
    print('O menor valor digitado foi', terc)

'''ALTERNATIVA 1'''
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))  # A FUNÇÃO MAX ME DÁ O MAIOR VALOR DA LISTA
print('O menor numero digitado foi {}'.format(min(numeros)))  # A FUNÇÃO MIN ME DÁ O MENOR VALOR DA LISTA

'''alternativa 2'''
n1 = int(input('digite o primeiro número:  '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

lista = [n1, n2, n3]
lista_ordenada = sorted(lista)  # o comando sorted coloca os valors da lista em ordem crescente.

print('O menor número é {}'.format(lista_ordenada[0]))
print('O maior número é {}'.format(lista_ordenada[2]))

