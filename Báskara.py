a = int(input('Digite o valor de \'a\': '))
b = int(input('Digite o valor de \'b\': '))
c = int(input('Digite o valor de \'c\': '))
x1 = ((-1*b)+((b**2-4*a*c)**(1/2)))/2*a
x2 = ((-1*b)-((b**2-4*a*c)**(1/2)))/2*a
print('O valor de X1 é {:.2f} e X2 é {:.2f}'.format(x1, x2))