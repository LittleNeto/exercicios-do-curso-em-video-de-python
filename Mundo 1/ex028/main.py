from random import randint
num = int(input('Em que número eu pensei? '))
if num < 0 or num > 5:
  print('valor inválido')
else:
  comp = randint(0, 5)
  if num == comp:
    print('parabéns, você adivinhou o número')
  else:
    print(f'lamento, mas você errou. o número escolhido foi {comp}')