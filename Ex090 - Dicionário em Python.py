aluno = {}
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if 5 < aluno['Média'] < 7:
    aluno['Situação'] = 'Em recuperação'
elif aluno['Média'] > 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'{k} é igual à: {v}')
