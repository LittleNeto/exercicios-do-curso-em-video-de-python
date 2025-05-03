soma = 0
for c in range(0, 6):
  num = int(input('digite um valor: '))
  if num % 2 == 0:
    soma += num
print(f'a soma é {soma}')