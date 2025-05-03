continua = True
while continua:
  num = int(input('Quer ver a tabuada de qual valor? '))
  if num < 0:
    continua = False
  else:
    print('-' * 30)
    for c in range(1, 11):
      print(f'{num} x {c} = {num * c}')
    print('-' * 30)
print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')