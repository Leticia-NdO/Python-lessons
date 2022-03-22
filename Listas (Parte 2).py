pessoas = [['pedro', 25], ['maria', 19], ['joão', 32]] ## isso é uma lista composta: listas dentro de listas
print(pessoas[0][0])  # index 0 de pessoas, e dentro desse índice o índice 0
for p in pessoas:
    print(p)   # mostra os elementos de pessoas na forma de lista

for p in pessoas:
    print(p[0])   # mostra só os nomes

for p in pessoas:
    print(p[1])   # mostra só as idades

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')

pessoal = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoal.append(dados[:])
    dados.clear()
for p in pessoal:
    print(p)
for p in pessoal:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)
