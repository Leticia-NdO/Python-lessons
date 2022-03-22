filme = {
    'título': 'StarWars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme)  # me mostra o dicionário
print('')
print(filme.values())  # me mostra os valores, ou seja, os valores atribuídos a cada chave(key)
print('')
print(filme.keys())  # me mostra as chaves, ou seja, os nomes dos índices que escolhemos
print('')
print(filme.items())  # me mostra as chaves e os valores

for k, v in filme.items():  # para cada key, e values in filme.items(), exiba:
    print(f'O {k} é {v}')
filme2 = {
    'título': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}
filme3 = {
    'título': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}
locadora = list()
locadora.append(filme)   # eu posso colocar dicionários dentro de listas, ou combinar as estruturas compostas
locadora.append(filme2)  # como eu desejar.
locadora.append(filme3)
print(locadora[0]['ano'])  # para navegar na lista, uso o índice de lista, para navegar no dicionário, uso as chaves
print(locadora[2]['título'])

pessoas = {
    'nome': 'leticia',
    'idade': 19,
    'sexo': 'F'
}
for k, v in pessoas.items():
    print(f'{k:<5} --- {v:>3}')

# estado1 = {
#     'uf': 'São Paulo',
#     'sigla': 'SP'
# }
# estado2 = {
#     'uf': 'Rio de Janeiro',
#     'sigla': 'RJ'
# }
#
# brasil = []
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite o nome do Estado: '))
    estado['Sigla'] = str(input('Digite a sigla do Estado: '))
    brasil.append(estado.copy())
    estado.clear()
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
    print('-='*15)
