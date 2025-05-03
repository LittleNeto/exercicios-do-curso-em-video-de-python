num = int(input('digite um número para ver sua tabuada: '))
if num <= 0 or num > 10:
  print('não foi possível calcular a tabuada')
else:
  print('-'*12)
  for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
  print('-'*12)