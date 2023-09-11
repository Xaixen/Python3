from time import sleep
v1 = int(input('primeiro valor: '))
v2 = int(input('segundo valor: '))
op = 0
while op != 5:
    print('-=' * 15)
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    op = int(input('>>> qual e a sua opção? = '))
    if op == 1:
        s = v1 + v2
        print(f'A soma entre {v1} + {v2} são {s}')
    elif op == 2:
        m = v1 * v2
        print(f'A multiplicação entre {v1} x {v2} são {m}')
    elif op == 3:
        if v1 > v2:
            maior = v1
            print(f'Entre {v1} e {v2} o maior é {maior} ')
        else:
            maior = v2
            print(f'Entre {v1} e {v2} o maior é {maior} ')
    elif op == 4:
        v1 = int(input('primeiro valor: '))
        v2 = int(input('segundo valor: '))
    elif op == 5:
        print('Saindo...')
    else:
        print('Opção invalida, tente novamente')
    sleep(2)