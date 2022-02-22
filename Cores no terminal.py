# A partir do ANSI sequence é possível usar estilização no python sem módulos.
# o melhor código de cores para python é \033[a;b;cm onde o a representa o código do estilo(negrito, itálico, etc), o b
# representa o texto, e o c representa o background.
# Os códigos para estilo são: 0 - nenhum, 1 - negrito (bold), 4 - sublinhado (urderline), 7 - negative (inverte a cor do
# texto e do backgroung).
# Os códigos para texto são: 30 - branco, 31 - vermelho, 32 - verde, 33 - amarelho, 34 - azul, 35 - roxo, 36 - ciano,
# 37 - cinza.
# Os códigos do background: 40 - branco, 41 - vermelho, 42 - verde, 43 - amarelho, 44 - azul, 45 - roxo, 46 - ciano,
# # 47 - cinza.
print('\033[0;31molá')
print('\033[4;35molá')
