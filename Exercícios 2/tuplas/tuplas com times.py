times = ('','Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Fluminense',
            'Fortaleza', 'Bragantino', 'Athletico-PR', 'Santos', 'Internacional', 'Corintians', 'Cuiabá', 'Bahia',
            'Goiás', 'Vasco da Gama', 'América-MG', 'Coritiba')
print('{:-^80}'.format('LISTA BRASILEIRÃO 2023'))
print(f'{times[1:5]}\n'
      f'{times[5:10]}\n'
      f'{times[10:15]}\n'
      f'{times[15:21]}')
print('{:-^80}'.format('5 PRIMEIROS NA LIDERANÇA'))
print(F'{times[1:6]}')
print('{:-^80}'.format('ZONA DE REBAIXAMENTO'))
print(f'{times[-4:]}')
print('{:-^80}'.format('TIMES EM ORDEM ALFABÉTICA'))
alfa = sorted(times)
print(f'{(alfa[1:5])}\n'
      f'{(alfa[5:10])}\n'
      f'{(alfa[10:15])}\n'
      f'{(alfa[15:21])}')
print('{:-^80}'.format(''))
print(f'Flamego na {times.index("Flamengo")}° posição.')