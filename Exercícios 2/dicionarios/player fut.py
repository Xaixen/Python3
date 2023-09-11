dicionario = dict()
partidas = list()
time = list()
while True:
    dicionario.clear()
    print(f'{"CADASTRO JOGADOR DE FUT":=^40}')
    dicionario['Nome'] = input('Nome do jogador: ').capitalize()
    tot = int(input('Quantas partidas jogadas? '))
    partidas.clear()
    for n in range(tot):
        partidas.append(int(input(f'{n}ºpartida: ')))
    dicionario['Total'] = sum(partidas)
    dicionario['Gols'] = partidas[:]
    time.append(dicionario.copy())
    print('-=' * 20)
    while True:
        resp = str(input('Deseja Continuar ? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!. Digite S ou N')
    if resp == "N":
        break
print('-=' * 20)
for i in dicionario.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 20)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (PARA SAIR APERTE 000): '))
    if busca == 000:
        break
    if busca > len(time):
        print(f'ERRO!. Não existe jogador com o codigo {busca}!')
    else:
        print(f"LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}:")
        for i, g in enumerate(time[busca]['Gols']):
            print((f'    No jogo {i+1} fez {g} gols.'))
        print('_' * 40)