soma = menor = contp = cont = 0
bar = ' '
while True:
    print('{:-^40}'.format('LOJA PRODUTOS BARATÃO'))
    np = str(input('Nome do produto: '))
    v = float(input('Preço:R$'))
    cont += 1
    if cont == 1 or v < menor:
        menor = v
        bar = np
    soma += v
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if v >= 1000:
        contp += 1
    if resp in 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'A soma total dos produtos R${soma:.2f}\n'
      f'{contp} produto acima de R$1000\n'
      f'O produto mais barato foi {bar} que custou R${menor:.2f}')

