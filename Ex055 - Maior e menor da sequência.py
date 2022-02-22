maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        maior = peso  # o primeiro peso sempre será o maior e o menor.
        menor = peso
    else:                  # a partir do segundo (quando c não é mais 1)
        if peso > maior:   # o programa comparará os valores obtidos aos
            maior = peso   # anteriores e sempre redefinirá qual o menor
        if peso < menor:   # e qual o maior valor.
            menor = peso
print(f'O maior peso lido foi de {maior} Kg')
print(f'E o menor peso lido foi de {menor} Kg')
