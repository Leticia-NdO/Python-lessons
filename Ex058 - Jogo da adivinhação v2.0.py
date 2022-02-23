from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
resposta = randint(0, 10)
palpite = int(input('Qual é o seu palpite? '))
count = 1
while palpite != resposta:
    if palpite > resposta:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
        count += 1
    else:
        print('Mais... Tente mais uma vez')
        palpite = int(input('Qual é o seu palpite? '))
        count += 1
print(f'Acertou com {count} tentativas. Parabéns!')
