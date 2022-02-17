# a linguagem python vem com poucas funcionalidades instaladas, pois se propõe a ser uma lingugagem rápida.
# Porém, é possível importar bibliotecas externas com funcionalidades específicas para cada necessidade.
# existem duas maneiras de importar bibliotecas, uma maneira generalista - usando o comando import - e uma maneira
# específica - from (biblioteca) import (comando específico dessa biblioteca).
# Por exemplo, o comadno import math. Nessa biblioteca math existem os comandos: ceil (arrendondar para cima), floor (arrendoda para baixo), trunc (exclui os decimais),
# pow (eleva a potência), sqrt (tira a raíz quadrada) e factorial (tira o fatorial de um número). Se eu quisesse usar só o sqrt eu digitaria from math import sqrt.

import math
numero1 = int(input('Digite um número: '))
raiz1 = math.sqrt(numero1) # quando usando uma biblioteca toda, primeiro indica a biblioteca e depois o especifíca o comando.
print('A raíz quadrada de {} é igual à {}.'.format(numero1, math.ceil(raiz1))) # aqui, o comando math.ceil indica que eu não
# quero que apareça a variável raiz, simplesmente. Eu quero que seja exibido essa variável arredondada para cima.

print('A SEGUIR OUTRO JEITO DE FAZER ISSO')

from math import sqrt
numero = int(input('Digite um número: '))
raiz = sqrt(numero) # Como eu já especifiquei qual comando eu quero, posso usar esse comando normalmente,sem precisar especificar a biblioteca.
print('A raíz quadrada de {} é {}.'.format(numero, raiz))

print('Sobre o random')
import random # a biblioteca random gera números pseudoaleatórios
num = random.random() # o comando random gera um número aleatório entre 0 e 1 (um float)
print(num)
print('Random de números inteiros')
import random
num = random.randint(1,10) # o comando randint gera um número inteiro pseudoaleatório
# entre os intervalos pré-estabelecidos (Retorna um inteiro aleatório N de forma que a <= N <= b.)
print(num)
