while True:
    t = 'TABUADA'
    print('==' * 10)
    print(f'{t:-^20}')
    print('==' * 10)
    n = int(input("Digite um número: "))
    if n < 0:
        break
    for c in range(1,11):
        x = n * c
        print(f'{n} x {c} = {x}')
print('Fim do programa!')