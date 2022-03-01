s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:                   # Se eu colocar o s += n antes do if, ele vai somar primeiro e depois
        break                      # verificar se é 999. Colocando o s += n depois do if, faz com que o programa
    s += n                         # primeiro verifique se é 999 e depois soma. Se for 999 ele só para e nem soma.
print(f'A soma é {s}')
