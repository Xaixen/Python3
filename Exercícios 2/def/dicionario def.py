def notas(*n, sit=False):
    '''

    :param n: simboliza as notas dos alunos
    :param sit: Situação que a turma se encontra
    :return: retorna o resultafo do dicionario
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Regular'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(3.5, 7.7, 8.6, sit=True)
print(resp)