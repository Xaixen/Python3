from exercicios.uteis import cores


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(cores.cores('ERRO, digite um número inteiro valído.', 1))
            continue
        except KeyboardInterrupt:
            print(cores.cores('O usuário não repondeu todos os dados.', 1))
        else:
            return num
            break


def leiafloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print(cores.cores('ERRO, digite um número inteiro valído.', 1))
            continue
        except KeyboardInterrupt:
            print(cores.cores('O usuário não repondeu todos os dados.', 1))
        else:
            return real
            break


num = leiaint('Digite um número inteiro: ')
real = leiafloat(('Digite um número real: '))
print(f'O Número real é {real} e o número inteiro é {num}')