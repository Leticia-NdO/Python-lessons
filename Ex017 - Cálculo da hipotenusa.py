from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(co**2 + ca**2)
print('O comprimento da hipotenusa é igual à {}'.format(h))

print('OUTRO MÉTODO DE CÁLCULA DA HIPOTENUSA')

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('O comprimento da hipotenusa é igual à {}.'.format(h))