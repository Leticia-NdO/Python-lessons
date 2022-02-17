vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('''MULTADO! Você ultrapassou o limite máximo permitido de 80km/h
e deverá pagar uma multa de R$''', (vel - 80) * 7)  # são 7 reais para cada quilômetro acima do limite.
if vel < 40:
    print('''MULTADO! Você está abaixo do limite mínimo permitido de 40km/h
e deverá pagar uma multa de R$''', (40 - vel) * 3.5)
print('Dirija com cuidado e tenha um bom dia.')

'''ALTERNATIVA 1 = RADAR'''

from random import randint
from time import sleep
sleep(5)
print('Seu carro passou no radar 🚗...')
sleep(2)
vel1 = randint(40,130)
if vel1 > 80:
    print('Você estava a {}Km/h e foi multado, o valor da multa é R${:.2f}'.format(vel1, (vel1-80)*7))
else:
    print('Sua velocidade é {}Km/h, continue respeitando os limites'.format(vel1))
