km = float(input('Digite a distância da viagem: '))
print('Você está prestes a iniciar uma viagem de', km, 'Km')
p1 = km * 0.5
p2 = km * 0.45
if km <= 200:
    print('E o preço da sua passagem será R$', p1)
else:
    print('E o preço da sua passagem será R${:.2f}'.format(p2))

'''ALTERNATIVA 1'''
distância = float(input('Qual é a distÂncia da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância < 200 else distância * 0.45  # o uso de uma estrutura in-line
print('E o preço da passagem será de R${:.2f}'.format(preço))
