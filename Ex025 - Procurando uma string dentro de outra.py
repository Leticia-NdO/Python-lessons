nome = input('Qual é o seu nome completo? ').strip().lower().split()
print('Seu nome tem Silva?', 'silva' in nome)
'''a linha dois também poderia ser: print('Seu nome tem Silva?', 'silva' in nome.lower()'''
