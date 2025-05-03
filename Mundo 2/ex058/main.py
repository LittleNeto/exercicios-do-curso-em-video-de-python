from random import randint
comp = randint(0, 10)
somador = 1
num = int(input('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Será que consegue adivinhar qual foi?
Qual é seu palpite? '''))
while num < 0 or num > 10:
  num = int(input('''Valor inválido, tente novamente
Qual é o seu palpite? '''))
while num != comp:
  somador += 1
  if num < comp:
    num = float(input('''Mais... Tente mais uma vez.
Qual o seu palpite? '''))
  elif num > comp:
    num = float(input('''Menos.. Tente mais uma vez.
Qual o seu palpite? '''))
print(f'Acertou com {somador} tentativas. Parabéns!')