n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O antecessor de {} é {} e o seu sucessor é {}'.format(n, a, s))

print('EXERCÍCIO 006')
n1 = int(input('Digite um número: '))
do = n1 * 2
tri = n1 * 3
raiz = n1 ** (1/2)
print('O dobro desse número é {}, o triplo é {} e sua raíz quadrada é {:.2f}.'.format(do, tri, raiz))

print('EXERCÍCIO 007 \'CÁLCULO DE MÉDIA SIMPLES DE NOTAS\'')
nota1 = int(input('Insira a primeira nota: '))
nota2 = int(input('Insira a segunda nota: '))
m = (nota1 + nota2)/2
print('A média é {}'.format(m))

print('EXERCÍCIO 008 - CONVERSOR DE METROS EM CM E MM')
me = int(input('Digite o valor em metros: '))
cm = me * 100
mm = me * 1000
print('Isso equivale a {} centímetros e {} milímetros'.format(cm, mm))

print('EXERCÍCIO 009 - TABUADA')
n2 = int(input('Digite um número: '))
l1 = n2*1
l2 = n2*2
l3 = n2*3
l4 = n2*4
l5 = n2*5
l6 = n2*6
l7 = n2*7
l8 = n2*8
l9 = n2*9
l10 = n2*10
print('{}x1={} \n{}x2={} \n{}x3={} \n{}x4={} \n{}x5={} \n{}x6={} \n{}x7={} \n{}x8={} \n{}x9={} \n{}x10={}'.format(n2, l1, n2, l2, n2, l3, n2, l4, n2, l5, n2, l6, n2, l7, n2, l8, n2, l9, n2, l10))

print('EXERCÍCIO 010 - CONVERSOR CAMBIAL REAL DÓLAR')
r = int(input('Digite o valor em reais: '))
d = r / 3.27
print('Esse valor corresponde a {:.2f} dólares.'.format(d))

print('EXERCÍCIO 011 - CALCULADOR DE TINTA PARA PINTAR PAREDES')
al = float(input('Digite a altura da parede (com decimais): '))
la = float(input('Digite a largura da parede (com decimais: '))
area = al * la
lt = area/2
print('Será necessário {:.2f} latas de tinta.'.format(lt))

print('EXERCÍCIO 012 - CALCULADOR DE 5% DE DESCONTO')
v1 = float(input("Digite o valor do produto (com decimais): "))
v2 = 95/100 * v1
print('O valor final será {:.2f}'.format(v2))

print('EXERCÍCIO 013 - CÁLCULO DE AUMENTO DE SALÁRIO DE 15%')
s1 = float(input('Digite o valor do salário: '))
s2 = 1.15 * s1
print('O novo salário será de {}.'.format(s2))