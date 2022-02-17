# Cadeias de texto (strings) são aquilo que interpretamos como frases.
# Para o Python, toda cadeia de texto está entre aspas simples ou duplas.

''' Atribui-se uma string a uma variável do seguinte modo: frase = 'Curso em vídeo Python'.
Essa string pode ser indexada. Cada caracter (inclusive os espaços) corresponde a um número, sendo o primeiro caracter
sempre o zero. Essa propriedade permite fazer o fatiamento: para fazer isso basta escrever o nome da variável e, entre
 colchetes, o número do caracter.'''
frase = 'Curso em Vídeo Python'
print(frase[0])  # primeira letra
print(frase[5])  # espaço
print(frase[20])  # última letra
print(frase[0:7])  # determinado trecho da string, do caracter 0 ao 7, sendo o caracter 0 incluso, mas o 7 não.
print(frase[0:7] + frase[7:21])  # Como o último caracter indicado é ignorado, é possível fazer essas somas sem
# repetição (nesse caso o 7 seria repetido). Além disso, a string tem 20 caracteres (a partir do zero), mas se eu quiser
# que ela seja escrita por completo, terei que colocar [0,21], porque o último caracter é sempre ignorado,portanto, se
# eu quero que o caracter 20 seja exibido, eu preciso colocar [~0,21].

''' Outra forma de incluir o último caracter é simplesmente omitindo o último número [n:].'''
print(frase[0:])
''' Quando se omite a primeiro número, ordena-se que seja exibido do zero até n ponto [:n] '''
print(frase[:5])

print(frase[9:21:2])  # ao inserir outro número depois do último, esse indicará uma certa alternância. Nesse caso, que pulará numa casa e exibirá a segunda
# na sua frente. Por isso, serão exibidas uma sim e outra não.

print(frase[9::3])  # esse comando indica que deverão ser exibidos os caractéres do 9 até o final, de três em três casas.
print(frase[::2])  # esse comando vai me dar toda a string frase com pulos de duas casas.

''' [ANÁLISE] '''
# A função embutida len() devolve o comprimento de uma string, ou seja, quantos espaços são ocupados na memória:
print(len(frase))

# a função frase.count() indica quantos caracteres como aquele susbcrito no parenteses existem na string:
print(frase.count('o'))  # no caso, são três.
print(frase.count('o', 0, 13))  # aqui, o comando é que conte quantas letras o existem no fatiamento [0:13]
print(frase.upper().count('O'))  # aqui, o comando pede que sejam contadas quantas letras "O" (maiúscula) existem
# em frase.upper(), ou seja, não a frase original, mas aquela posta em letras maiúsculas.

# a função frase.find() me mostra em que posição começa o trecho que eu estou procurando:
print(frase.find('deo'))

# Se dentro da função frase.find() for posta uma string que não pode ser encontrado dentre de
# frase, o resultado será -1.

''' a função 'curso' in frase é uma pergunta. Me dirá true se tiver, e false se não tiver '''
print('Curso' in frase)

''' [TRANSFORMAÇÃO] '''
# Via de regra, uma lista de string é imutável. Porém, é possível mudar suas formas de exibição através de métodos.
# o método frase.replace('Python', 'Android'), procuraria a palavra Python na string frase e a substituiria por Android:
print(frase.replace('Python', 'Android'))  # o comando replace não altera de fato a string, só exibe ela da maneira
# desejada.

print(frase.upper())  # esse método faz com que a string fique toda em maiúsculo.
print(frase.lower())  # esse método faz com que a string fique toda em minúsculo.
print(frase.capitalize())  # esse método faz com que a primeira palavra da string comece com letra maiúscula.
print(frase.title())  # esse método faz com que todas as palavras da string comecem com letra maiúscula.
'''frase.strip()  # esse método remove os espaços inúteis da string. Exemplo, se a string frase fosse '   Aprenda python  '
# esse método removeria os espaços inúteis no início e no fim da string, assim, a letra A seria o 0 e a contagem ocorreia
# normalmente.
frase.rstrip()   esse r indica que só espaços inúteis do final (o lado direito) serão removidos.
frase.lstrip()   esse r indica que só espaços inúteis do início (o lado esquerdo) serão removidos.'''

''' [DIVISÃO] '''
print(frase.split())  # esse comando gera uma lista com todas as palavras de uma cadeia de caracteres.
# Cada palavra vira uma string individual, ou seja, a primeira letra de cada palavra é
# 0 e assim por diante. Além disso, cada palavra recebe uma indexação individual, no caso da nossa frase,
# a palavra 'Curso" seria 0, 'em' seria 1, 'vídeo' seria 2 e 'Python' seria 3

''' [JUNÇÃO] '''
# do mesmo jeito que é possível dividir, é possível juntar. Usa-se o comando:
print(''.join(frase))
print('-'.join(frase.split()))  #aqui eu decidi colocar - entre as palavras, ao juntá-las.

nome = input('Qual o seu nome? ')
print('Olá, {:5}. Seja bem vindo'.format(nome))  # preencher a chave com :n faz com que o input
#  seja exibido juntamente com n espaços.

nome = input('Qual o seu nome? ')
print('Olá, {:>5}. Seja bem vindo'.format(nome))  # :>n faz com que o input seja exibido com n espaços para a direita.

nome = input('Qual o seu nome? ')
print('Olá, {:<5}. Seja bem vindo'.format(nome))  # :<n faz com que o input seja exibido com n espaços para a esquerda.

nome = input('Qual o seu nome? ')
print('Olá, {:^5}. Seja bem vindo'.format(nome))  # :^n faz com que o input seja centralizado em n espaços

nome = input('Qual o seu nome? ')
print('Olá, {:=^5}. Seja bem vindo'.format(nome))