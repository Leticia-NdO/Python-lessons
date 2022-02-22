from datetime import date
count1 = 0
count2 = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if 125 > date.today().year - ano > 18:
        count1 += 1
    elif 0 <= date.today().year - ano < 18:
        count2 += 1
print('')
print(f'Tivemos {count1} pessoas maiores de idade\nE também tivemos {count2} pessoas menores de idade')
