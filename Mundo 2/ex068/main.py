from random import randint
contador = 0
continua = True
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
while continua:
  comp = randint(0, 10)
  num = int(input('Diga um valor: '))
  while num > 10 or num < 0:
    num = int(input('''Valor inválido, tente novamente
Diga um valor: '''))
  soma = num + comp
  uni = str(input('Par ou ímpar? [P/I] ')).strip().upper()
  while uni not in 'PI':
    uni = str(input('''Informação inválida, tente novamente
Par ou ímpar? [P/I] ''')).strip().upper()
  print('-' * 30)
  if soma % 2 == 0:
    print(f'você jogou {num} e o computador {comp}. Total de {soma} deu PAR')
  else:
    print(f'você jogou {num} e o computador {comp}. Total de {soma} deu ÍMPAR')
  print('-' * 30)
  if soma % 2 == 0 and uni == 'I' or soma % 2 != 0 and uni == 'P':
    print('Você PERDEU!')
    print('=-' * 30)
    continua = False
  else:
    contador += 1
    print('''Você VENCEU!
Vamos tentar novamente...''')
    print('=-' * 15)
print(f'GAME OVER! você venceu {contador} vezes')