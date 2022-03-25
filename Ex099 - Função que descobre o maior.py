from time import sleep
def maior(*lst):
    maximo = max(lst)
    tamanho = len(lst)
    for c in range(0, len(lst)):
        print(lst[c], end=' ')
        sleep(0.5)
    print(f'foram informados, {tamanho} valores ao todo.\nO maior valor informado foi {maximo}')
    print('-=' * 30)


maior(4, 6, 4, 2, 9)
