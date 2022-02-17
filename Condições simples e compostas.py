# Algoritmos sequênciais são o contrário de algoritmos condicionais. Nas sequências o programa executa os comandos de
# cima para baixo, sem possibilidades de desvios.
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')  # esse bloco é chamado de 'bloco True', pois só será executad se if for verdadeiro.
else:
    print('Carro velho')  # esse bloco é chamado de 'bloco false', pois só será executado se if for falso.
print('Fim')
'''Essa estrutura em que os subalgoritmos estão mais a direita é chamada de estrutura dentada.
Todo comando que estiver colado no lado esquerdo da tela será executado sempre.'''

# CONDIÇÃO SIMPLIDICADA #
tempo1 = int(input('Quantos anos tem o seu carro? '))
print('Carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

'''é IMPORTANTE NOTAR QUE O ELSE NÃO É OBRIGATÓRIO'''
nome = str(input('Qual o seu nome? '))
if nome == 'Leticia':
    print('Que nome lindo você tem!')
print('Bom dia,', nome)
'''Quando não tem o else é uma estrutura condicional simples, e quando tem é uma estrutura condicional composta.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 7:
    print('Parabéns! Você está aprovado nessa disciplina!')
else:
    print('Você está de recuperação.')
