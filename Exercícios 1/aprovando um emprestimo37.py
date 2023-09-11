print('-=-' * 15)
print(' ' * 5, "\33[34;40mEMPRESTIMO CONCEDIDO OU NEGADO\33[m")
print("-=-" * 15)
v = float(input('digite o valor da casa: R$'))
s = float(input('digite seu salario: R$'))
f = int(input('Quantos anos de financiamento? = '))
pm = v / (f * 12)
print('O valor da casa de R${:.2f} em {} anos\n'
      'Prestação Mensal de R${:.2f}'.format(v, f, pm))
if s * 0.30 >= pm:
    print('O emprestimo pode se\33[32m CONCEDIDO')
else:
    print('Empréstimo\33[31m NEGADO')
