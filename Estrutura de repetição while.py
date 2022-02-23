# a estrutura for precisa de um limite específico. Na estrutura while o limite da repetição é umacondição:
# repita tal ação até que determinada condição esteja satisfeita.
c = 1
while c != 10:             # o c é um. E a cada laço será adicionado mais 1 à c.
    print(c, end='')       # Enquanto c for diferente de 10 esse laço será executado.
    c += 1                 # Essa mesma tarefa pode ser feita com o for. Enquanto o limite é conhecido
print('fim')               # pode-se usar qualquer um.

n = ''
while n != 'Leticia':                              # enquanto o valor da variável for diferente do que eu quero o
    n = str(input('Digite o seu nome: ')).title()  # programa vai continuar.
print('Resposta correta.')

w = 1
while not w == 0:                          # enquanto o valor da variável não for o que eu quero, o programa vai
    w = int(input('Digite um valor: '))    # continuar
print('fim')

r = 'S'
while r == 'S':                            # enquanto a resposta do jogador for S, o programa vai continuar, se for N,
    t = int(input('Digite um valor: '))    # ele vai parar.
    r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        print('Obrigado por jogar.')
        break

f = 1
par = impar = 0
while f != 0:                            # enquanto o f for diferente de 0.
    f = int(input('Digite um valor: '))
    if f != 0:                           # se o número for diferente de 0, conta se ele é par ou ímpar. Isso é feito
        if f % 2 == 0:                   # para que o programa não conte o 0 como um número par.
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')

