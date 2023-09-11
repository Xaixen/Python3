from math import radians, sin, cos, tan
a = int(input('digie o ângulo que deseja:'))
print('O ângulo de {} tem o SENO de {}'.format(a, sin(radians(a))))
print('O ângulo de {} tem o COSSENO de {}'.format(a, cos(radians(a))))
print('O ângulo de {} tem o TANGENTE de {}'.format(a, tan(radians(a))))
