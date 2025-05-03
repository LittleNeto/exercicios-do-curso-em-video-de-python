a1 = int(input('qual o primeiro termo? '))
r = int(input('qual a razão? '))
an = a1 + r*10
print('os 10 primeiros termos dessa PA são:')
for c in range(a1, an, r):
  print(c)