salo = float(input('Qual é o salário do funcionário? R$ '))
if salo > 1250:
    print('Quem ganhava R${:.2f} passar a ganhar R${:.2f} agora.'.format(salo, 1.1*salo))
if salo < 1250:
    print('Quem ganhava R${:.2f} passar a ganhar R${:.2f} agora.'.format(salo, 1.15*salo))
