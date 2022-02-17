num = int(input('Informe um número: '))
print('Analisando o número {}:'.format(num))
u = num % 10  # qualquer número dividido por dez terá como resto o último algarismo desse número.
d = num//10 % 10  # ao fazer a divisão exata por dez, cortaremos um algarismo desse número. Ao di-
# vidir por dez pegaremos o último algarismo do número obtido.
c = num//100 % 10  # ao fazer a divisão exata por cem, cortaremos dois algarismos desse número. Ao di-
# vidir por dez pegaremos o último algarismo do número obtido.
m = num//1000 % 10  # ao fazer a divisão exata por mil, cortaremos três algarismos desse número. Ao di-
# vidir por dez pegaremos o último algarismo do número obtido.

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

''' [ALTERNATIVA 1] '''
n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O numero digitado foi:', n)
print('Unidade: {}'.format(n2[3]))
print('Dezena: {}'.format(n2[2]))
print('Centena: {}'.format(n2[1]))
print('Milhar: {}'.format(n2[0]))

''' [ALTERNATIVA 2] '''
num1 = str(input('Digite um numero de 0 a 9999: ')).zfill(4)  # O comando .zfill() preenche uma string numérica com
# zeros à esquerda. Ou seja, faz a mesma coisa que a alternativa 1, mas de um jeito mais clean e sem converter a
# string pra int.
print('O numero digitado foi:', num1)
print('Unidade: {}'.format(num1[3]))
print('Dezena: {}'.format(num1[2]))
print('Centena: {}'.format(num1[1]))
print('Milhar: {}'.format(num1[0]))
