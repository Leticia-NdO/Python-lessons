a = float(input)
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if abs(a > b - c and a < b + c and b > a - c and b < c + a and c > b - a and c < b + a):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
# o comando abs() pega só o módulo dos números.
