r = str(input('Informe seu sexo: [M/F] ')).upper().strip()
while r != 'M' and r != 'F':
    r = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).upper()
print(f'Sexo {r} registrado com sucesso.')

''' ALTERNATIVA USANDO FLAG'''

flag = False

while flag == False:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        flag = True
    else:
        print('Dados inválidos. Digite novamente!')
        flag = False
print(f'Sexo {sexo} registrado com sucesso')
