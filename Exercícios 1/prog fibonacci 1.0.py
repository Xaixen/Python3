n = int(input('quantos termo eseja mostra? '))
c = 0
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1

# print(f'{t1} -> {t2}', end='')
# for c in range(3, n):
#     t3 = t1 + t2
#     print(f' -> {t3}', end='')
#     t1 = t2
#     t2 = t3