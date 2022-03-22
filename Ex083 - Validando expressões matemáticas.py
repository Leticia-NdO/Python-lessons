expressao = input('Digite uma expressão: ')
pe = expressao.count('(')
pd = expressao.count(')')
if expressao.index(')') > expressao.index('('):
    if pe == pd:
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
