n = int(input('Escolha um número da tabuada: '))
for c in range(1, 11):
    r = n * c
    print("{} x {} = {}".format(n, c, r))
