conti = contm = contf20 = 0
while True:
    print('♦-' * 10)
    print(' CADASTRE UMA PESSOA')
    print('♦-' * 10)
    i = int(input("digite sua idade: "))
    sex = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('..' * 10)
    sn = str(input('Deseja continuar? [S/N] '))
    if i >= 18:
        conti += 1
    if sex in 'Mm':
        contm += 1
    if sex in 'Ff' and i < 20:
        contf20 += 1
    if sn in 'Nn':
        break
print(f'Foram cadastradas {conti} pessoas maiores de idade\n'
      f'{contm} Homem e {contf20} de Mulheres com menos de 20 anos')