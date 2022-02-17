n1 = int(input('Digite um número: ')) # o comando input tem como padrão o tipo string. Para converter o seu conteúdo para outro tipo, deve-se indicar esse outro tipo.
n2 = int(input('Digite outro número: '))
s = n1 + n2
print("A soma entre {} e {} é {}.".format(n1, n2, s)) #a sequência das variáveis em .format é a que vai preencher as chaves (as máscaras) da string literal.
print(type(s))
print('''\
Uso: strings
    -RAW            -Com \'r\' na frente.
    -LITERAIS       -Sem \'r\' na frente.
''') # O \ que precede o apóstrofo indica que ele é um caracter especial que faz parte da mensagem e não deve indicar o fim da string.
# As aspas triplas servem para que a string abranja várias linhas. O \ (na frente das aspas iniciais) evita uma linha vazia entre a tabelinha e o resto do script.

