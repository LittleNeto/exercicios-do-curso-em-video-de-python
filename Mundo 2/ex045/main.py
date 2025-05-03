from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
palavras = ['JO', 'KEN', 'PO!!!']
escolha = choice(lista)
op = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? '''))
while op < 0 or op > 2:
  op = int(input('''Valor inválido, tente novamente
Qual a sua escolha?'''))
for c in palavras:
  print(c)
  sleep(1)
print('-=' * 11)
print(f'''Computador escolheu {escolha}
Jogador escolheu {lista[op]}''')
print('-=' * 11)
if lista[op] == escolha:
  print('EMPATE')
elif lista[op] == 'Tesoura' and escolha == 'Papel':
  print('JOGADOR VENCE')
elif lista[op] == 'Papel' and escolha == 'Pedra':
  print('JOGADOR VENCE')
elif lista[op] == 'Pedra' and escolha == 'Tesoura':
  print('JOGADOR VENCE')
elif lista[op] == 'Tesoura' and escolha == 'Pedra':
  print('COMPUTADOR VENCE')
elif lista[op] == 'Pedra' and escolha == 'Papel':
  print('COMPUTADOR VENCE')
elif lista[op] == 'Papel' and escolha == 'Tesoura':
  print('COMPUTADOR VENCE')