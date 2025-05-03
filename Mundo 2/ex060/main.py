multi = 1
num = int(input('''Digite um número para
calcular seu fatorial: '''))
while num < 1:
  num = int(input('''Valor inválido, tente novamente
Digite um número para
calcular seu fatorial: '''))
print(f'Calculando {num}! =', end= ' ')
while num != 0:
  print(num, end= ' ')
  print('x ' if num > 1 else '= ', end= '')
  multi *= num
  num -= 1
print(multi)