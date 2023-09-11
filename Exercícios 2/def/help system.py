c = ('\33[1;30;41m', #0vermelho
    '\33[7;32;40m', #1verde
     '\33[1;36;40m', #2ciano
     '\33[7;30m' #3 Branco
)
def ajuda(função):
    help(função)

def titulo(msg, cor):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    users = str(input('Qual biblioteca deseja ajuda? '))
    if users.upper() == 'FIM':
        break
    else:
        titulo(f'ACESSANDO O MANUAL DO {users}', 2)
        ajuda(users)