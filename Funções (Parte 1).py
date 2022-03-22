def linha():
    print('-----------------')


linha()
linha()


def mensagem(msg):  # O que está dentro dos parênteses da função é o parâmetro
    print('-='*20)
    print(msg)
    print('-='*20)


mensagem('BEM VINDO')


def soma(a, b):
    # print(f'A = {a} e B = {b}')
    print(f'A soma de {a} + {b} é {a+b}')


soma(3, 2)
soma(b=7, a=40)  # eu posso mudar as variáveis, contando que eu explicite isso.


def contador(*a):  # o * indica que esse parâmetro não tem um número definido, ou seja, ele pode receber qualquer
    print(a)       # quantidade de parâmetros
    print(len(a))


contador(5, 6, 9)


valores = [4, 6, 2, 8]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


dobra(valores)


def soma2(*valores):    # esse é o processo de empacotamento
    som = 0
    for num in valores:   # esse é o processo de desempacotamento
        som += num
    print(f'Somando os valores {valores} temos {som}')


soma2(3, 6, 4, 9)
