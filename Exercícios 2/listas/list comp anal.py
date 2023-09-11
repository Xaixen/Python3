dados = []
pessoa = []
pesada = leve = 0
while True:
    dados.append(str(input('Digite um nome: ')).capitalize())
    dados.append(float(input('Digite o peso em KG: ')))
    resp = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
    if len(pessoa) == 0:
        pesada = dados[1]
        leve = dados[1]
    else:
        if dados[1] > pesada:
            pesada = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoa.append(dados[:])
    dados.clear()
    if resp == 'N':
        break
print(pessoa)
print(f'Foram cadastradas {len(pessoa)} pessoas.')
for p in pessoa:
    if p[1] == pesada:
        print(f'A pessoa mais pesada foi: {p[0]} com {pesada}KG')
for p in pessoa:
    if p[1] == leve:
        print(f'é a mais leve foi: {p[0]} com {leve}KG')
