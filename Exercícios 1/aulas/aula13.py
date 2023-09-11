# for c in range(0, 3):
#     print('passo')
#     print('pula')
# print('passo')
# print('pega')

# for c in range(1, 101):
#     print(c)
# n = int(input('digite um valor: '))
# if n > 1000:
#     print('Fala um número menor ai vacilão')
# else:
#     for c in range(0, n+1):
#         print(c)
i = int(input('inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))
for c in range(i, f+1, p):
    print(c)