def print_especial(txt):
    print(f'-' * len(txt))
    print(txt)
    print(f'-' * len(txt))


def titulo(txt):
    print(f'-' * 40)
    print(f'{txt:^40}')
    print(f'-' * 40)


def menu(lista):
    print('--' * 20)
    print(f'{"MENU PRINCIPAL":^40}')
    print('--' * 20)
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print('--' * 20)
