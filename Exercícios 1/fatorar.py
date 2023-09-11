# from math import factorial
# n = int(input('Digite um número para fatorar: = '))
# f = factorial(n)

# n = int(input('Digite um número para fatorar: '))
# f = 1
# print(f"Calculando {n}! = ", end='')
# while n > 0:
#     print(n, end='')
#     print(' x ' if n > 1 else ' = ', end='')
#     f *= n
#     n -= 1
# print(f)

n = int(input('Digite um número para fatorar: '))
f = 1
for c in range(n , 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)
