from math import hypot
c1 = float(input('comprimento do cateto oposto: '))
c2 = float(input('comprimento do cateto adjacente: '))
print(f'a hipotenusa vai medir {hypot(c1, c2):.2f}')