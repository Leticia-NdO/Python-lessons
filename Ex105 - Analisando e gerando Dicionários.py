def notas(*grades, sit=0):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param grades: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletim = {'total': len(grades),
            'maior': max(grades),
            'menor': min(grades),
            'média': sum(grades)/len(grades)
            }
    if sit:
        if boletim['média'] < 5:
            boletim['situação'] = 'RUIM'
        elif 7 > boletim['média'] > 5:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'BOA'

    return boletim


resp = notas(5.5, 2.5, 1.5, 10, 6.5)
print(resp)
