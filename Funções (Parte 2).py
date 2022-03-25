# docstring == uma string que explica uma função
# ''' ''' logo depois da def, documenta a string

def contador(i, f, p):
    '''
    => FAZ UMA CONTAGEM E MOSTRA NA TELA
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('fim')

# PARÂMETROS OPCIONAIS:


def somar(a, b, c=0):   # o = 0 indica que aquele parâmetro é opcional, ou seja, a função funciona com ou sem ele.
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2)
somar(5, 9, 67)


# ESCOPO DE VARIÁVEIS
# Escopo é o local que uma variável existe e onde ela deixa de existir.


def teste():
    x = 8
    print(f'Na função teste, n vale {n}')    # mesmo eu tendo declarado essa variável só lá embaixo, ela é reconhecida
    print(f'Na função teste, x vale {x}')    # aqui também. Isso porque n tem escopo global.

                                             # Já a varável x só tem valor dentro da função, e não fora dela. Isso
# programa principal                         # porque x tem escopo local.
n = 2
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}')

# RETORNO DE VALORES
# As funções em python podem retornar ou não um valor. Para retornar um valor usa-se o return


def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s   # assim o s passa a ser a variável que está atribuída à função


r1 = somar2(3, 2, 5)
r2 = somar2(6, 2)
r3 = somar2(3, 1)
print(f'As somas valem {r1}, {r2} e {r3}')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual à {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
