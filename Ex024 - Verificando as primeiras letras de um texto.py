cidade = input('Em que cidade você nasceu? ').strip().lower()
print('santo' in cidade)

'''[ALTERNATIVA 1]'''
cid = str(input('Em que cidade você nasceu? ')).strip().lower()
print(cid[:5] == 'santo')