                    #Operadores Aritméticos
n1 = int(input('digite um valor:'))
n2 = int(input('digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
print('A soma:{}, \no produto:{}, \na divisao:{:.1f}\n'.format(s, m, d),end='')
print("divisão inteira:{}, \npotencia:{}, \nresto da divisão:{}".format(di, e, rd))
