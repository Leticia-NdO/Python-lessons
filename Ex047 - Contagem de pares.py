for c in range(2, 51, 2):
    print(c, end=' ')  # essa opção ocupa menos processamento, pois o programa nem olha para os números que estão sendo
#  pulados.

# Alternativa 2
'''for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')'''  # essa opção faz mais processamento pois ela exige que o computador passe por todos os 50
# números e calcule quais são divisíveis por dois.
