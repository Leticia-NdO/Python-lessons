from time import sleep
primo = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
maximo = max(primo, seg)
minimo = min(primo, seg)
menu = int(input('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
while menu != 5:
    if menu == 1:
        print(f'A soma entre {primo} e {seg} é {primo + seg}')
        print('+='*15)
        sleep(1)
        menu = int(input('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
    elif menu == 2:
        print(f'{primo} vezes {seg} é {primo*seg}')
        print('+=' * 15)
        sleep(1)
        menu = int(input('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
    elif menu == 3:
        if primo == seg:
            print('Os dois números são iguais!')
            print('+=' * 15)
            sleep(1)
            menu = int(input('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
        else:
            print(f'{maximo} é maior do que {minimo}')
            print('+=' * 15)
            sleep(1)
            menu = int(input('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
    elif menu == 4:
        print('Informe os números novamente: ')
        primo = int(input('Primeiro valor: '))
        seg = int(input('Segundo valor: '))
        maximo = max(primo, seg)
        minimo = min(primo, seg)
        menu = int(input('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
    else:
        print('Opção inválida. Tente novamente: ')
        menu = int(input('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa
>>>>>> Qual é a sua opção? '''))
print('+='*15)
print('Finalizando...')
sleep(1.5)
print('Fim do programa! Volte Sempre!')
