lista = []
impar = list()
par = list()
print("::" * 15)
print(f'{"PARA SAIR DIGITE 111":-^30}')
print("::" * 15)
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    if n == 111:
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
lista.remove(111), impar.remove(111)
print(f'A lista completa: {lista}')
print(f'Números pares : {par}')
print(f'Números impares: {impar} ')
