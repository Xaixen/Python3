
print('-=-' * 20)
print('\33[7;33;40mCONVERSÃO\33[m\n'
      '[1] BINáRIA\n'
      '[2] OCTAL\n'
      '[3] HEXADECIMAL')
print('-=-' * 20)
c = int(input('ESCOLHA UMA OPÇÃO: '))
n = int(input('DIGITE UM NÚMERO: '))
if c == 1:
    print('n°{} convertido para BINÁRIO = {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('n°{} convertido para OCTAL = {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('n°{} convertido para HEXADECiMAL = {}'.format(n, hex(n)[2:]))
else:
    print('\33[1;33mNúmero invalido!\n'
          'Por, favor! escolha de 1 a 3')
