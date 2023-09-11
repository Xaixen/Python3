frase = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
         'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if n <= 20 and n >= 0:
        break

    print('Tente novamente.', end=' ')
print(f'O número que você digitou foi {frase[n]}.')