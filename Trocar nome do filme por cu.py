from random import choice
nome = input('Escreva o nome de um filme: \n')
if(len(nome) < 3):
    print('CU')
else:
    lista = nome.split()
    c = int(1)
    while(c < 3):
        s = choice(lista)
        c = len(s)
    print(nome.replace(s,'CU'))

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

w = int(len(num) - (len(num)+1))
x = int(len(num) - (len(num)+2))
y = int(len(num) - (len(num)+3))
z = int(len(num) - (len(num)+4))