l = float(input('digite a largura da parede:'))
a = float(input('digite a altura da parede:'))
ar = l * a
at = ar / 2
print('A parede tem {}m² \nserá nescessário {:.2f}L de tinta'.format(ar, at))