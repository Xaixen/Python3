# a = 50
# b = 75
# c =30
print('--' * 18)
print('''CATEGORIAS DO PRODUTO EM ESTOQUE
[ 1 ] ALIMENTOS
[ 2 ] BEBIDAS
[ 3 ] LIMPEZA''')
print('--' * 18)
categoria = int(input('Digite a categoria: '))
produto = str(input('Qual o produto?: ')).strip().capitalize()
quant = int(input('Digite a quantidade necessaria: '))

if categoria and produto and quant:
    if categoria == 1:
        if quant < 50:
            print(f'Para o produto {produto} o minimo disponivel no estoque são 50 quants')
    elif categoria == 2:
        if quant < 75:
            print(f'Para o produto {produto} o minimo disponivel no estoque são 75 quants')
    elif categoria == 3:
        if quant < 30:
            print(f'Para o produto {produto} o minimo disponivel no estoque são 30 quants')
    else:
        print('Categoria invalida. Digite novamente!')
else:
    print('Preencher todas as informações!')