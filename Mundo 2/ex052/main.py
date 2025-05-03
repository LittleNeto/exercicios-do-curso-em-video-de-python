soma = 0
num = int(input('digite um valor: '))
for c in range(1, num + 1):
  if num % c == 0:
    soma += 1
if soma == 2:
  print('ele é primo')
else:
  print('ele não é primo')