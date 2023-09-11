def print_especial(txt):
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


def maior_valor(*n):
    print_especial('DESCOBRINDO MAIOR VALOR')
    print(f'Analisando valores...')
    for num in n:
        print(f'{num}', end=' ')
    print(f'foram informados {len(n)} valores ao todo\n'
            f'Maior valor informado: Nº{max(n)}')


maior_valor(1, 3, 5, 2, 0)
maior_valor(2, 10, 3, 2, 7, )

