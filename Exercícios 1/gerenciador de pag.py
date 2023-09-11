p = float(input('Preço das compras: R$'))
print('-=' * 10)
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro ou cheque\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3 ou mais no cartão')
op = int(input('Digite uma opção: '))
if op > 4:
    print('Opção inválida, tente novamente!')
elif op == 1:
    c = p / 1.10
    print(' 10% de desconto, total a pagar R${}'.format(c))
elif op == 2:
    c = p / 1.05
    print(' 5% de desconto, total a pagar R${}'.format(c))
elif op == 3:
    c2 = p / 2
    print('Total a pagar R${}'.format(p))
    print('Sua compra será parcelada em x R${}'.format(c2))
elif op == 4:
    pa = int(input('Quantas parcelas deseja pagar ?: '))
    if pa == 1:
        c = p / 1.02
        x = c / 1
        print(' 2% de desconto, total a pagar R${}'.format(c))
        print('Sua compra será parcelada em 1x R${}'.format(x))
    elif pa == 2:
        x = p / 2
        print('Total a pagar R${}'.format(p))
        print('Sua compra será parcelada em 2x R${}'.format(x))
    else:
        c = p * 1.20
        x = c / pa
        print('20% juros, total a pagar R${}'.format(c))
        print('Sua compra será parcelada em {}x R${}'.format(pa, x))

