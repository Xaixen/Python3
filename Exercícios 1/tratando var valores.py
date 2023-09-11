n = total = soma = 0
while n != 999:
    n = int(input('Digite um número [999 PARA PARAR]: '))
    total += 1
    soma += n
    if n == 999:
        soma -= n
    if n == 999:
        total -= 1
print('FIM')
print(f'Você digitou {total} e a soma dos valores é {soma}')