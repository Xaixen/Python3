tot = soma = 0
while True:
    n = int(input('Digite um numero. [999] para parar: '))
    if n == 999:
        break
    tot += 1
    soma += n
print(f'Você digitou {tot} vez(es) e a soma entre eles foram {soma}.')