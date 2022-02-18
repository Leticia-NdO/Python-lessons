p = float(input('Qual o seu peso? (Kg): '))
h = float(input('Qual é a sua altura? (m): '))
imc = p / (h**2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Cuidado, você está em MAGREZA!')
elif imc < 25:
    print('Parabéns, você está na faixa de peso NORMAL!')
elif imc < 30:
    print('Cuidado, você está em SOBREPESO!')
elif imc < 40:
    print('Cuidado, você está em OBESIDADE!')
elif imc >= 40:
    print('Cuidado, você está em OBESIDADE GRAVE!')
