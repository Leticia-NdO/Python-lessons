n = str(input('Digite algo: '))
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaço? ', n.isspace()) #resultado fora da mensagem
print('É um número? ', n.isnumeric())
# existem duas maneiras de realizar essa tarefa, uma em que o resultado está contido dentro da mensagem e outro em que o resultado está fora dela.
print('É alfabético? {}'.format(n.isalpha())) #resultado dentro da mensagem
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
