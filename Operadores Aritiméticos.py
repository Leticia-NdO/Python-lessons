# Operadores: + adição, - subtração, * multiplicação, / divisão (divisão clássica dá um float), ** potência,
# // divisão inteira (ignora o resto e dá um int), % o resto da divisão, == igualdade.
# Exemplo:
# 5 + 2 == 7      5 ** 2 == 25
# 5 - 2 == 3      5 // 2 == 2 # em uma divisão clássica com chave, a resposta vai ser dois (2*2==4)
# 5 * 2 == 10     5 % 2 == 1 # e vai sobrar um (5-4==1)
# 5/2 == 2.5
# Ordem de Precedência: 1° (), 2° **, 3° *,/,// e % (faz quem aparecer primeiro), 4° + e -
# Também é possível usar o comando pow(4,3) para calcular a potência de 4 elevado a 3, mas ao usar esse comando a ordem
# de precedência não vale mais (pois não é um operador aritmético).
# Para calcular a raiz de um número, basta elevar esse número à uma fração. Ex: 81**(1/2)==9 é a mesma coisa que raiz de
# 81.

print('oi'*20)  # é possível multiplicar strings literais.
print(3*6)
print('py'+'thon')  # é possível concatenar duas strings.
print('py' 'thon')  # duas ou mais strings literais ao lado da outra são automaticamente concatenadas.


n = int(input('Insira um número: '))
nAlt = int(input('Insira outro número: '))
print('A soma de {} e {} é {}'.format(n, nAlt, n+nAlt)) # essa configuração dispensa o uso de uma terceira variável
# (que no exercício anterior foi s) usa-se a variável quando o resultado for um valor importante e que será usado.
# dispensa-se a variável quando o resultado for um valor descartável.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d2 = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {}'.format(s, m, d), end='') # a divisão sempre terá como resultado um
# número flutuante. Para determinar quantas casas decimais serão exibidas usar o comando :.nf dentro da chave da divisão
# (sendo n o número de casas decimais que devem ser exibidas)
print('A divisão inteira é {} e a potência é {}'.format(d2, e))

# o comando end='' no final do primeiro print faz com que tudo fique na mesma linha, mesmo tendo dois prints. O conteúdo
# entre as aspas é o conteúdo que ficará entre o conteúdo do primeiro print e o segundo. Também é possível quebrar uma
# linha inserindo \n no ponto de quebra.