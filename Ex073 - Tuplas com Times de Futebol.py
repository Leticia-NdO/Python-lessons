times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('-+'*30)
print(f'Lista de times do brasileirão: ', end=' ')
for t in times:
    print(t, end=", ")
print('\n', '-+'*30)
print(f'Os cinco primeiros times são: ', end=' ')
for t in times[:5]:
    print(t, end=", ")
print('\n', '-+'*30)
print(f'Os 4 últimos são: ', end=' ')
for t in times[16:]:
    print(t, end=", ")
print('\n', '-+'*30)
print(f'Times em ordem alfabética: ', end=' ')
for t in sorted(times):
    print(t, end=", ")
print('\n', '-+'*30)
print(f'O Chapecoense se encontra na {times.index("Chapecoense")+1}ª posição')
