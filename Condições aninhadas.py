"""Condições aninhadas existem para casos mais complexos em que há mais de duas opções. Assim, são condiç~eos dentro
de condições."""
n = str(input('Qual é o seu nome:'))
if n == 'Leticia':
    print('Que nome bonito, {}!'.format(n))
elif n == 'Pedro' or 'Maria' or 'João':  # elif é a junção de else e if. Significa algo como "senão (aí abrem mais
    # opções) se uma coisa, se outra". Aí no fim pode ter um else (é opcional). É possível usar várias elifs.
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia!')
