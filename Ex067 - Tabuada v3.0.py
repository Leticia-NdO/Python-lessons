while True:
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if tabu < 0:
        break
    for c in range(1, 11):
        print(f'{tabu} X {c} = {tabu*c}')
    print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
