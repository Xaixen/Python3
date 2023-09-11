 #exercicio - antecessor, sucessor, dobro,triplo e raiz quadrada
n = int(input('digite um número:'))
s = n + 1
a = n - 1
d = n * 2
t = n * 3
r = n**(1/2)
print('O número que você digitou é {} \nSucessor {}  Antecessor {}'.format(n, s,a))
print("o dobro {}  triplo {}  raiz quadrada {:.2f}".format(d, t, r))