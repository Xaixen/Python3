def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite um número inteiro valído.')
            continue
        except KeyboardInterrupt:
            print('O usuário não repondeu todos os dados.')
        else:
            return num
            break


def leiafloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO, digite um número inteiro valído.', 1)
            continue
        except KeyboardInterrupt:
            print('O usuário não repondeu todos os dados.', 1)
        else:
            return real
            break
