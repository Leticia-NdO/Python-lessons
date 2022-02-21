# Laços de repetição fazem com que um comando seja executado em looping eternamente ou por uma quantidade específica de
# vezes, de acordo com as especificações. A estrutura de repetição for

for e in range(0, 3):  # in range() é o número de vezes que eu quero que o loop se repita. Lembrando que ele não
    print('Hello World')  # considera o último número, então se eu escrevesse (1, 3) o comando só seria repetido 2 vezes
print('Fim')

print('-+'*20)

for c in range(0, 6):
    print(c)           # ao pedir que o pŕoprio laço seja impresso, o comando irá exibir os números do range.

print('-+' * 20)

for c in range(0, 6, 2):  # vai imprimir do 0 até o 6 de 2 em 2.
    print(c)

print('-+' * 20)

for d in range(6, 0, -1):
    print(d)           # ao pedir que imprima (0,6) nada vai acontecer, porém se eu colocar -1, eu indico que eu quero q
                       #  seja impresso do 6 até o 0 de um em um.
print('-+' * 20)

for d in range(6, 0, -2):
    print(d)           # aqui é a mesma coisa do exemplo anterior, mas de 2 em 2.

print('-+' * 20)

n = int(input('Digite um número: '))
for a in range(0, n):  # dessa forma, só será impresso até o número anterior a n, pois o último número não é impresso.
    print(a)

print('-+' * 20)

j = int(input('Digite um número: '))
for h in range(0, j+1):  # agora vai contar de 0 até j
    print(h)

print('-+' * 20)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for k in range(i, f+1, p):  # início é onde o loop vai começar, fim é onde ele vai terminar, e passo é de quanto em
    print(k)                # quanto a sequência vai pular.

print('-+'*20)

s = 0
for t in range(0, 3):
    l = int(input('Digite um valor: '))  # ele vai repetir a pergunta Digite um valor três vezes.
    s = s + l  # o python também entende s = s + l como s += l
print('A soma dos valores digitados é:', s)
