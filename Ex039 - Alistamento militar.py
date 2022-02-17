from datetime import date
gênero = str(input('Por favor, informe o seu sexo biológico (F/M): ')).upper().strip()
if gênero == 'M':
    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))
    if idade < 18:
        if 18 - idade == 1:
            print('Ainda falta 1 ano para o seu alistamento.')  # para o singular
        else:
            print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))  # para o plural
        print('Seu alistamento será em {}'.format(date.today().year + (18 - idade)))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE.')
    elif idade > 18:
        if idade - 18 == 1:
            print('Você já deveria ter se alistado há 1 ano.')  # para o singular
        else:
            print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))  # para o plural
            print('Seu alistamento foi em {}.'.format(date.today().year - (idade - 18)))
elif gênero == 'F':
       print('O alistamento obrigatório não se aplica a você.')
else:
    print('Por favor, digite um sexo biológico válido.')
