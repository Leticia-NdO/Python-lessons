def fatorial(num=1, show=0):
    """
    -> Calcula o Fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
        f *= c
    return f


n = int(input('Digite o valor a ser fatorado? '))
res = str(input('Deseja exibir a conta? '))
if res in 'sSSIMsimCLAROSim':
    res = True
elif res in 'nNNÃOnãoNão':
    res = False
numfatorado = fatorial(n, res)
print(f'{numfatorado}')
