def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'\33[0;31mERRO {entrada} Inválido!\33[m')
        else:
            valido = True
            return float(entrada)

def leiainteiro(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            print(f'Número {n}')
            ok = True
        else:
            print('\33[0;31mErro. Não é um número.\33[m')
        if ok:
            break
    return valor

