num = count = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    count += 1
    soma += num
print(f'Você digitou {count-1} números e a soma entre eles foi {soma-999}')
