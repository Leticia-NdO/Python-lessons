casa = float(input('Digite o valor da casa: R$ '))
s = float(input('Digite a renda do comprador: R$ '))
anos = float(input('Quantos anos de financiamento? '))
prestação = casa/(anos*12)
if prestação < (0.3*s):
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}. \n Empréstimo APROVADO!'
          .format(casa, anos, prestação))
else:
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}. \n Empréstimo NEGADO!'
          .format(casa, anos, prestação))
