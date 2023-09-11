def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            print(f'Número {n}')
            ok = True
        else:
            print('\33[0;31mErro. Não é um número.\33[m')
        if ok:
            break
    return valor


n = leiaint('digite um numero: ')
