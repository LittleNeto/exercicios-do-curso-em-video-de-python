ano = int(input('digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('esse ano é bissesto')
else:
  print('esse ano não é bissesto')