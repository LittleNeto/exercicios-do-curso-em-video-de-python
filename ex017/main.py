from math import hypot
c1 = float(input('comprimento do cateto oposto: '))
c2 = float(input('comprimento do cateto adjacente: '))
print('a hipotenusa vai medir {:.2f}'.format(hypot(c1, c2)))