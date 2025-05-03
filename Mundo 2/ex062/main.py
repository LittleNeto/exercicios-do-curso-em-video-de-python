num = int(input('''Gerador de PA
-=-=-=-=-=-=-=-=-=-=
Primeiro termo: '''))
raz = int(input('Razão da PA: '))
tot = 0
cont = 0
val = 1
while tot < 10:
  print(f'{num} ->', end=' ')
  num += raz
  tot += 1
print('PAUSA')
while val != 0:
  val = int(input('Quantos termos a mais você quer mostrar? '))
  while val < 0:
    val = int(input('''Valor inválido, tente novamente
Quantos termos a mais você quer mostrar? '''))
  while cont != val:
    print(f'{num} ->', end= ' ')
    num += raz
    cont += 1
    tot += 1
  if val > 0:
    print('PAUSA')
  cont = 0
print(f'Progressão finalizada com {tot} termos mostrados')