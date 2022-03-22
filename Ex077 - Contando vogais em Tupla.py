palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
# vogais = ('a', 'e', 'i', 'o', 'u')
# for p in palavras:
#     print(f'\nNa palavra {p:} existem as vogais: ', end='')
#     for v in vogais:
#         if v in p:
#             print(f'{v}', end=' ')

for p in palavras:
    print(f'\nNa palavra {p.upper()} existem as vogais: ', end=' ')
    for letra in p:
        if letra in 'a, e, i, o, u':
            print(letra, end=' ')
