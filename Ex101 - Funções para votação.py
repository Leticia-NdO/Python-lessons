from datetime import datetime


def votar(num=0):
    from datetime import datetime
    idade1 = datetime.now().year - ano
    o = 'VOTO OBRIGATÓRIO'
    op = 'VOTO OPCIONAL'
    n = 'NÃO VOTA'
    if idade1 > 18:
        return o
    elif 16 <= idade1 < 18 or idade1 > 65:
        return op
    else:
        return n


print('-'*30)
ano = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - ano
voto = votar()
print(f'Com {idade} anos: {voto}')
