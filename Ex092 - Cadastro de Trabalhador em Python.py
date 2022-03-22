from datetime import date
cadastro = {}
cadastro['Nome'] = str(input('Nome: ')).capitalize()
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = date.today().year - nascimento
cadastro['CTPS'] = int(input('Carteira de trabalho: '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação:'))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - nascimento

for k, v in cadastro.items():
    print(f'{k} tem valor {v}')
