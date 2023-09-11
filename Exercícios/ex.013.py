                        #CATETOS E HIPOTENUSA
import math
c1 = float(input('comprimento do cateto oposto:'))
c2 = float(input('comprimento do cateto adjacente:'))
h = math.hypot(c1, c2)
print('A hipotenusa vai medir',h)