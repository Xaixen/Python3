pesado = 0
leve = 0
for c in range(1,6):
    p = float(input('Qual é o peso da {}° pessoa: '.format(c)))
    if c == 1:
        pesado = p
        leve = p
    else:
        if p > pesado:
            pesado = p
        if p < leve:
            leve = p
print('O maior peso é {}KG'.format(pesado))
print('O Menor peso é {}KG'.format(leve))