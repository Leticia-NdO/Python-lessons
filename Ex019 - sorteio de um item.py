import random
um = (input('Digite o nome do primeiro aluno: '))
dois = (input('Digite o nome do segundo aluno: '))
tres = (input('Digite o nome do terceiro aluno: '))
quatro = (input('Digite o nome do quarto  aluno: '))
alunos = [um, dois, tres, quatro]  # uma lista é escrita entre colchetes. Cada conteúdo dessa lista tem um número
#  correspondente, começando pelo zero. Ou seja, um corresponde a 0, dois >>> 1, três >>> 2, quatro >>> 3
print('O aluno sorteado foi {}'.format(alunos[random.randint(0, 3)]))  # eu poderia evocar a lista com um elemento
#  fixo assim: alunos[0], e isso seria igual ao elemento "um" da lista. Porém, no lugar do número, coloquei uma
#  função de sorteio de um número entre 0 e 3(random.randint(0,3), assim terei um conteúdo dessa lista sorteado.

print('[UMA OUTRA MANEIRA DE SORTEAR UM ITEM]')

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceito aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))  # o comando choice vai escolher um valor da lista
#  pré-estabelecida.
