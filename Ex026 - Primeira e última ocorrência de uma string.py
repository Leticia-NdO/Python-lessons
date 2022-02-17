frase = input('Digite uma frase: ').strip().lower()
print('A letra \'A\' aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra \'A\' aparece na posição {}'.format(int(frase.find('a'))+1))
print('A última letra \'A\' aparece na posição {}'.format(int(frase.rfind('a'))+1))  # rfind pede que seja procurado
# pela direita.
