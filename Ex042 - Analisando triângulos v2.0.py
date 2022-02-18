a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if abs(b-c) < a < b + c and abs(a-c) < b < a + c and abs(b-a) < c < b + a and a != b != c != a:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
elif abs(b-c) < a < b + c and abs(a-c) < b < a + c and abs(b-a) < c < b + a and a == b != c or c == a != b or \
        c == b != a:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
elif abs(b-c) < a < b + c and abs(a-c) < b < a + c and abs(b-a) < c < b + a and a == b == c:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')

'''[ALTERNATIVA 1]'''
d = int(input('Primeiro segmento: '))
e = int(input('Segundo segmento: '))
f = int(input('Terceiro segmento: '))
if d < e + f and e < d + f and f < d + e:
    print('Os segmentos PODEM FORMAR um triângulo', end=' ')  # end=' ' vai grudar os dois prints,
    if d == e == f:                                           # mesmo que tenha uns ifs no meio
        print('EQUILÁTERO!')
    if d != e != f != d:
        print('ESCALENO!')
    if d == e != f or d == f != e or e == f != d:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
