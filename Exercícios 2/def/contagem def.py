def print_especial(txt):
    print(f'~' * len(txt))
    print(txt)
    print(f'~' * len(txt))


def contagem():
    from time import sleep
    print_especial('CONTAGEM DE 1 ATÉ 10')
    for n in range(11):
        print(n, end=' ')
        sleep(0.3)
    print()
    print_especial('CONTAGEM DE 10 ATÉ 0 PULANDO 2 PASSOS ')
    for nr in range(10, -1, -1):
        print(nr, end=' ')
        sleep(0.3)
    print()
    print_especial('FAÇA O SEU PERSONALIZADO')
    inicio = int(input('INÍCIO: '))
    fim = int(input('FIM: '))
    passos = int(input('PASSOS: '))
    for c in range(inicio, fim + 1, passos):
        print(c, end=' ')
        sleep(0.3)
    print()
    print('~'*20)


contagem()

