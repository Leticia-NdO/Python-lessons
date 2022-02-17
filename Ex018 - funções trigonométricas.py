import math
ang1 = float(input('Digite o valor do ângulo: '))
ang2 = math.radians(ang1)  # é necessário converter o valor do ângulo para radianos,
# pois as funções sin, cos e tan estão configuradas, por padrão, para receber valores em radianos.
sen = math.sin(ang2)
cos = math.cos(ang2)
tan = math.tan(ang2)
print('O valor do seno de {}° é {:.2f}: '.format(ang1, sen))
print('O valor do cosseno de {}° é {:.2f}: '.format(ang1, cos))
print('O valor da tangente de {}° é {:.2f}: '.format(ang1, tan))

print('[OUTRO JEITO DE CALCULAR AS FUNÇÕES TRIGONOMÉTRICAS]')

angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))  # dessa vez, a conversão acontece dentre da função trigonométrica.
# Isso é o aninhamento de funções.
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do seno de {} é {:.2f}'.format(angulo, seno))
print('O valor do cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('O valor da tangente de {} é {:.2f}'.format(angulo, tangente))
