# Palíndromo é a frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.
from unidecode import unidecode
palavra = unidecode(str(input('Digite uma frase ou palavra: '))).upper().split()  # transformamos a variável em uma lista de palavras.
palin = list(''.join(palavra))  # ''.join(palavra) junta a lista "palavra" em uma única string, e o comando list transforma essa string em uma lista de letras.
palin.reverse()  #  o método reverse pega a lista de palavras palin e a põe de trás pra frente.
print(f'O inverso de {"".join(palavra)} é {"".join(palin)}')
if "".join(palavra) == "".join(palin):
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
# unicode retira os acentos.
