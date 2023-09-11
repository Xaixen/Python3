pessoa= {}
galera = []
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: ')).capitalize().strip()
    while True:
        pessoa['sexo'] = str(input('SEXO [M/ F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!, DIGITE M OU F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Deseja continuar? [S / N]: ')).upper().strip()[0]
        if resposta in "SN":
            break
        print('ERRO!, responda S ou N')
    if resposta == 'N':
        break
media = soma / len(galera)
print(f'Foram cadastradas {len(galera)}')
print(f'A soma da idade é : {soma}')
print((f'A média de idade da galera: {media}'))
print(f'Mulheres cadastras:', end='')
for p in galera:
    print(p['nome'], end=' ')
print('')
print('A lista das pessoas com a idade maior que a média')
for p in galera:
    if p['idade'] >= media:
        print('   ', end=' ')
        for c, v in p.items():
            print(f'{c} = {v}', end=' ')
print('')
print('ENCERRADO')