def fatorial(n, fator=False):
    '''

    :param n: Indica um número para fatorar
    :param fator: Indica o cálculo na função
    :return: retorna o resultado f que indica a fatoração
    '''
    f = 1
    for c in range(n, 0, -1):
        if fator:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(3, fator=True))
help(fatorial)