def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            return valor
        else:
            print('Erro. Digite um número inteiro válido.')
        if ok:
            break


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
