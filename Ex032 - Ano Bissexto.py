from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 se quiser saber do ano atual. '))
if ano == 0:
    ano = date.today().year  # date.today().year puxa o ano do PC
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # != significa diferente. Um ano bissexto é divisível por 4, e
    # não pode ser divisível por 100 e 400 ao mesmo tempo.
    print(ano, 'É BISSEXTO!')
else:
    print(ano, 'NÃO É BISSEXTO!')
