total = soma = maior = menor = 0
rep = 'S'
while rep in 'Ss':
    n = int(input('digite um número:'))
    rep = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    menor = n
    total += 1
    soma += n
    if n > maior:
        maior = n
    if n <= menor:
        menor = n
media = soma / total
print(f'''Você digitou {total} vezes, a soma entre os valores são {soma}
A media ficou {media} e os maior número é {maior} e o menor número é {menor}.''')