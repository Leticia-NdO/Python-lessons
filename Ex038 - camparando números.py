primo = int(input('Primeiro número: '))
seg = int(input('Segundo número: '))
if primo > seg:
    print('O primeiro valor é maior.')
elif primo == seg:
    print('Não existe valor maior, os dois valores são IGUAIS')
else:
    print('O segundo valor é maior.')
