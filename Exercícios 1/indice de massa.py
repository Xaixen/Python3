kg = float(input('Digite seu peso em KG: '))
cm = float(input('Digite sua altura em centimetros: '))
imc = kg / (cm * cm)
print('Seu IMC é de {:.2f} = '.format(imc), end='')
if imc <= 18.5:
    print('\33[1;31m!Abaixo do peso!\33[m')
elif imc <= 25:
    print('\33[32mPeso ideal\33[m')
elif imc <= 30:
    print('\33[34mSobrepeso\33[m')
elif imc <= 40:
    print('\33[33mObesidade\33[m')
else:
    print('\33[1;31m!Obesidade Mórbida\33[m')