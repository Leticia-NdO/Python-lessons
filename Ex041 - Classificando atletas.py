from datetime import date
nas = int(input('Ano de nascimento: '))
idade = date.today().year - nas
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade >= 25:
    print('Classificação: MASTER')
else:
    print('Por favor, insira uma idade válida.')
