nome = str(input('digite o seu nome:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem  {} letras'.format(nome.find(' ')))