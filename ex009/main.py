num = int(input('digite um número para ver sua tabuada: '))
if num <= 0 or num > 10:
  print('não foi possível calcular a tabuada')
else:
  print('-'*12)
  print(f'{num} x 1 = {num * 1}')
  print(f'{num} x 2 = {num * 2}')
  print(f'{num} x 3 = {num * 3}')
  print(f'{num} x 4 = {num * 4}')
  print(f'{num} x 5 = {num * 5}')
  print(f'{num} x 6 = {num * 6}')
  print(f'{num} x 7 = {num * 7}')
  print(f'{num} x 8 = {num * 8}')
  print(f'{num} x 9 = {num * 9}')
  print(f'{num} x 10 = {num * 10}')
  print(f'-'*12)