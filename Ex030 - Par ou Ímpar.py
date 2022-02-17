num = int(input('Me diga um número qualquer: '))
if num % 2 == 0:  #
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))

'''ALTERNATIVA 1'''
n = int(input('Digite um número: '))
d = n / 2
if d == int(d):
    print('O número que você digitou é par!')
else:
    print('O número que você digitou é ímpar!')

'''ALTERNATIVA 2'''
numero = int(input('Dê um número qualquer:  '))
if numero//2 == numero/2:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))
