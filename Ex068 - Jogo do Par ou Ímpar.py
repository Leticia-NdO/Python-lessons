import random
count = 0
print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)
while True:
    comp = random.randint(0, 10)
    jog = int(input('Diga um valor de 0 a 10: '))
    while jog > 10 or jog < 0:
        print('Por favor, insira um valor válido.')
        jog = int(input('Diga um valor de 0 a 10: '))
    lado = str(input('Par ou ímpar? [P/I] ')).upper()
    while lado != 'P' and lado != 'I':
        print('Por favor, insira um valor válido.')
        lado = str(input('Par ou ímpar? [P/I] ')).upper()
    if (comp + jog) % 2 == 0:
        print(f'Você jogou {jog} e o computador {comp}. Total de {jog+comp} DEU PAR')
        print('-='*15)
        if lado == 'P':
            print('Você VENCEU!\nVamos jogar novamente...')
            print('-=' * 15)
            count += 1
        else:
            break
    else:
        print(f'Você jogou {jog} e o computador {comp}. Total de {jog + comp} DEU ÍMPAR')
        print('-=' * 15)
        if lado == 'I':
            print('Você VENCEU!\nVamos jogar novamente...')
            print('-=' * 15)
        else:
            break
print('Você PERDEU!')
if count == 1:
    print(f'GAME OVER! Você venceu apenas 1 vez.')
else:
    print(f'GAME OVER! Você venceu {count} vezes!')
