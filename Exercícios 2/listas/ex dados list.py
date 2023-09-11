lista = []
while True:
    print('♦' * 28)
    print('PARA SAIR DIGITE 111')
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    if n == 111:
        break
lista.remove(111)
lista.sort(reverse=True)
print(f'{"FIM DO PROGRAMA":♦^30}')
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em  ordem decrecente: {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista')
