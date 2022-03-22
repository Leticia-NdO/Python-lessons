num = int(input('Digite um número inteiro entre 0 e 20: '))
extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'
            'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
            'dezoito', 'dezenove', 'vinte')
while True:
    if num > 20 or num < 0:
        while 20 < num or num < 0:
            num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if 20 > num > 0:
        print(f'Você digitou o número {extensos[num]}.')
        res = str(input('Quer continuar? [S/N] ')).upper()
        if res == 'S':
            num = int(input('Digite um número inteiro entre 0 e 20: '))
        else:
            break
print('PROGRAMA ENCERRADO!')
